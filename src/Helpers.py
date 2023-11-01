import pandas as pd
import numpy as np
import json

DATA_FOLDER = "MovieSummaries/"

MOVIE_COLUMNS_TO_CLEAN = ['Fb_movie_id','Movie languages','Movie genres','Movie countries']

CHARACTER_COLUMNS_TO_CLEAN = ["Fb_movie_id", "Fb_actor_ethnicity_id", "Fb_char_id",
                               "Fb_actor_id","Freebase character/actor map ID"]

NAME_COLUMNS_TO_CLEAN = ["Fb_char_actor_id"]

def load_data(file_path):
    if (file_path == "movie.metadata.tsv"):
        df = pd.read_csv(DATA_FOLDER + "movie.metadata.tsv", sep='\t', header=None,
                 names=["Wiki_movie_id", "Fb_movie_id", "Movie name",
                        "release_date", "Movie box office revenue",
                        "Movie runtime", "Movie languages", "Movie countries", "Movie genres"])
        # Apply the clean_column function to the specified columns
        df[MOVIE_COLUMNS_TO_CLEAN] =df[MOVIE_COLUMNS_TO_CLEAN].apply(clean_column)

        # Use str.extract() to extract the year from the 'release_date' column
        df['release_date'] = df['release_date'].str.extract(r'(\d{4})')

        #Remove language in the 'Movie languages' column as it appears in every row
        df['Movie languages'] = df['Movie languages'].str.replace('language', '', case=False)

        df['Movie runtime'] = df['Movie runtime'].apply(lambda x: np.nan if x > 15000 else x)

    elif (file_path == "plot_summaries.txt"):
        df = pd.read_csv(DATA_FOLDER + "plot_summaries.txt", sep='\t', header=None, names=["Wiki_movie_id", "Summary"])

    elif (file_path == "character.metadata.tsv"):
        df = pd.read_csv(DATA_FOLDER+"character.metadata.tsv", sep='\t', header=None,
                 names=["Wiki_movie_id", "Fb_movie_id", "release_date",
                        "Character", "Actor date of birth", "Actor gender",
                        "Actor_height", "Fb_actor_ethnicity_id",
                        "Actor_name", "Actor_age", "Freebase character/actor map ID",
                        "Fb_char_id", "Fb_actor_id"])
        # Apply the clean_column function to the specified columns
        df[CHARACTER_COLUMNS_TO_CLEAN] =df[CHARACTER_COLUMNS_TO_CLEAN].apply(clean_column)

        # Use str.extract() to extract the year from the 'release_date' column
        df['release_date'] = df['release_date'].str.extract(r'(\d{4})')

        df['Actor_age'] = df['Actor_age'].apply(lambda x: np.nan if x < 0 else x)
        df['Actor_height'] = df['Actor_height'].apply(lambda x: np.nan if x > 2.5 else x)

    elif (file_path == "name.clusters.txt"):
        df = pd.read_csv(DATA_FOLDER+"name.clusters.txt", sep='\t', header=None, names=['Name', 'Fb_char_actor_id'])
        # Apply the clean_column function to the specified columns
        df[NAME_COLUMNS_TO_CLEAN] =df[NAME_COLUMNS_TO_CLEAN].apply(clean_column)
    elif (file_path == "tvtropes.clusters.txt"):
        df = pd.read_csv(DATA_FOLDER + "tvtropes.clusters.txt", delimiter='\t', header=None, names=['CharType', 'Values'])

        # Extract specific JSON values into separate columns
        df['Char'] = df['Values'].apply(lambda x: extract_json_values(x, 'char'))
        df['Movie'] = df['Values'].apply(lambda x: extract_json_values(x, 'movie'))
        df['Fb_char_actor_id'] = df['Values'].apply(lambda x: extract_json_values(x, 'id'))
        df['Actor'] = df['Values'].apply(lambda x: extract_json_values(x, 'actor'))

        # Apply the clean_column function to the specified columns
        df[NAME_COLUMNS_TO_CLEAN] =df[NAME_COLUMNS_TO_CLEAN].apply(clean_column)
        # Delete the ClusterID column
        df.drop(columns=['Values'], inplace=True)

    return df

# Define a function to remove the "/m/" prefix and codes/extra characters
def clean_column(column):
    # Remove "/m/" prefix
    column = column.str.replace('/m/', '', regex=False)
    
    # Remove codes and extra characters
    column = column.str.replace(r'"\w+":\s*', '', regex=True)  # Remove codes
    column = column.str.replace(r'[{}"]', '', regex=True)  # Remove {, }, and double quotes
    
    return column

# Define a function to extract specific JSON values
def extract_json_values(json_str, key):
    try:
        data = json.loads(json_str)
        return data.get(key, None)
    except json.JSONDecodeError:
        return None


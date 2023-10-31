import pandas as pd
import json
import re

DATA_FOLDER = "MovieSummaries/"

MOVIE_COLUMNS_TO_CLEAN = ['Freebase movie ID','Movie languages','Movie genres','Movie countries']

CHARACTER_COLUMNS_TO_CLEAN = ["Freebase movie ID", "Actor ethnicity (Freebase ID)", "Freebase character ID",
                               "Freebase actor ID","Freebase character/actor map ID"]

NAME_COLUMNS_TO_CLEAN = ["ID"]

def load_data(file_path):
    if (file_path == "movie.metadata.tsv"):
        df = pd.read_csv(DATA_FOLDER + "movie.metadata.tsv", sep='\t', header=None,
                 names=["Wikipedia movie ID", "Freebase movie ID", "Movie name",
                        "Movie release date", "Movie box office revenue",
                        "Movie runtime", "Movie languages", "Movie countries", "Movie genres"])
        # Apply the clean_column function to the specified columns
        df[MOVIE_COLUMNS_TO_CLEAN] =df[MOVIE_COLUMNS_TO_CLEAN].apply(clean_column)
    elif (file_path == "plot_summaries.txt"):
        df = pd.read_csv(DATA_FOLDER + "plot_summaries.txt", sep='\t', header=None, names=["Wikipedia movie ID", "Summary"])
    elif (file_path == "character.metadata.tsv"):
        df = pd.read_csv(DATA_FOLDER+"character.metadata.tsv", sep='\t', header=None,
                 names=["Wikipedia movie ID", "Freebase movie ID", "Movie release date",
                        "Character name", "Actor date of birth", "Actor gender",
                        "Actor height (in meters)", "Actor ethnicity (Freebase ID)",
                        "Actor name", "Actor age at movie release", "Freebase character/actor map ID",
                        "Freebase character ID", "Freebase actor ID"])
        # Apply the clean_column function to the specified columns
        df[CHARACTER_COLUMNS_TO_CLEAN] =df[CHARACTER_COLUMNS_TO_CLEAN].apply(clean_column)
    elif (file_path == "name.clusters.txt"):
        df = pd.read_csv(DATA_FOLDER+"name.clusters.txt", sep='\t', header=None, names=['Name', 'ID'])
        # Apply the clean_column function to the specified columns
        df[NAME_COLUMNS_TO_CLEAN] =df[NAME_COLUMNS_TO_CLEAN].apply(clean_column)
    elif (file_path == "tvtropes.clusters.txt"):
        df = pd.read_csv(DATA_FOLDER + "tvtropes.clusters.txt", delimiter='\t', header=None, names=['CharType', 'Values'])

        # Extract specific JSON values into separate columns
        df['Char'] = df['Values'].apply(lambda x: extract_json_values(x, 'char'))
        df['Movie'] = df['Values'].apply(lambda x: extract_json_values(x, 'movie'))
        df['ID'] = df['Values'].apply(lambda x: extract_json_values(x, 'id'))
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
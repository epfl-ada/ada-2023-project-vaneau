import pandas as pd
import numpy as np
import json

DATA_FOLDER = "data/"

MOVIE_COLUMNS_TO_CLEAN = ['Fb_movie_id', 'Movie languages', 'Movie genres', 'Movie countries']
CHARACTER_COLUMNS_TO_CLEAN = ["Fb_movie_id", "Fb_actor_ethnicity_id", "Fb_char_id", "Fb_actor_id", "Freebase character/actor map ID"]
NAME_COLUMNS_TO_CLEAN = ["Fb_char_actor_id"]

def load_data(file_path):
    """ This function loads the data and returns the respective DataFrame.
    
    Args:
        data_path (str): datafolder path

    Returns:
        data (pd.DataFrame) : the DataFrame containing the values preprocessed and cleaned
    """
    loaders = {
        "movie.metadata.tsv": load_movie_metadata,
        "plot_summaries.txt": load_plot_summaries,
        "character.metadata.tsv": load_character_metadata,
        "name.clusters.txt": load_name_clusters,
        "tvtropes.clusters.txt": load_tvtropes_clusters
    }
    
    if file_path in loaders:
        return loaders[file_path]()
    else:
        raise ValueError("Unsupported file_path: " + file_path)

def load_movie_metadata():
    # Read the csv file as a pandas dataframe
    df = pd.read_csv(DATA_FOLDER + "movie.metadata.tsv", sep='\t', header=None,
                     names=["Wiki_movie_id", "Fb_movie_id", "Movie name",
                            "release_date", "Movie box office revenue",
                            "Movie runtime", "Movie languages", "Movie countries", "Movie genres"])
    
    # Clean specified columns
    df[MOVIE_COLUMNS_TO_CLEAN] = df[MOVIE_COLUMNS_TO_CLEAN].apply(clean_column)
    
    # Extract and format the year from the 'release_date' column
    df['release_date'] = pd.to_datetime(df['release_date'], format='mixed', utc=True, errors='coerce').dt.year
    
    # Remove "language" in the 'Movie languages' column
    df['Movie languages'] = df['Movie languages'].str.replace('language', '', case=False)
    
    # Handle extreme values in 'Movie runtime'
    df['Movie runtime'] = df['Movie runtime'].apply(lambda x: np.nan if x > 15000 else x)
    
    return df

def load_plot_summaries():
    # Read the csv file as a pandas dataframe
    df = pd.read_csv(DATA_FOLDER + "plot_summaries.txt", sep='\t', header=None, names=["Wiki_movie_id", "Summary"])

    return df

def load_character_metadata():
    # Read the csv file as a pandas dataframe
    df = pd.read_csv(DATA_FOLDER + "character.metadata.tsv", sep='\t', header=None,
                     names=["Wiki_movie_id", "Fb_movie_id", "release_date",
                            "Character", "Actor date of birth", "Actor gender",
                            "Actor_height", "Fb_actor_ethnicity_id",
                            "Actor_name", "Actor_age", "Freebase character/actor map ID",
                            "Fb_char_id", "Fb_actor_id"])
    
    # Clean specified columns
    df[CHARACTER_COLUMNS_TO_CLEAN] = df[CHARACTER_COLUMNS_TO_CLEAN].apply(clean_column)
    
    # Extract and format the year from the 'release_date' column
    df['release_date'] = pd.to_datetime(df['release_date'], format='mixed', utc=True, errors='coerce').dt.year
    
    # Handle negative values in 'Actor_age' and extreme values in 'Actor_height'
    df['Actor_age'] = df['Actor_age'].apply(lambda x: np.nan if x < 0 else x)
    df['Actor_height'] = df['Actor_height'].apply(lambda x: np.nan if x > 2.5 else x)
    
    return df

def load_name_clusters():
    # Read the csv file as a pandas dataframe
    df = pd.read_csv(DATA_FOLDER + "name.clusters.txt", sep='\t', header=None, names=['Name', 'Fb_char_actor_id'])
    
    # Clean specified columns
    df[NAME_COLUMNS_TO_CLEAN] = df[NAME_COLUMNS_TO_CLEAN].apply(clean_column)
    
    return df

def load_tvtropes_clusters():
    # Read the csv file as a pandas dataframe
    df = pd.read_csv(DATA_FOLDER + "tvtropes.clusters.txt", delimiter='\t', header=None, names=['CharType', 'Values'])
    
    # Extract specific JSON values into separate columns from the column CharType
    df['Char'] = df['Values'].apply(lambda x: extract_json_values(x, 'char'))
    df['Movie'] = df['Values'].apply(lambda x: extract_json_values(x, 'movie'))
    df['Fb_char_actor_id'] = df['Values'].apply(lambda x: extract_json_values(x, 'id'))
    df['Actor'] = df['Values'].apply(lambda x: extract_json_values(x, 'actor'))
    
    # Clean specified columns
    df[NAME_COLUMNS_TO_CLEAN] = df[NAME_COLUMNS_TO_CLEAN].apply(clean_column)
    
    # Delete the Values column
    df.drop(columns=['Values'], inplace=True)
    
    return df


def clean_column(column):
    """
    This function remove the "/m/" prefix and codes/extra characters that are in the DataFrame column in argument

    """
    # Remove "/m/" prefix
    column = column.str.replace('/m/', '', regex=False)
    
    # Remove codes and extra characters
    column = column.str.replace(r'"\w+":\s*', '', regex=True)  # Remove codes
    column = column.str.replace(r'[{}"]', '', regex=True)  # Remove {, }, and double quotes
    
    return column


def extract_json_values(json_str, key):
    """
    This function extract specific JSON values
    
    """
    try:
        data = json.loads(json_str)
        return data.get(key, None)
    except json.JSONDecodeError:
        return None

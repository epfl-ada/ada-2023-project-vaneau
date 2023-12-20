import pandas as pd
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import crawling libraries
import pickle
from src.crawler.crawler import *

# Import clustering libraries
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
from collections import defaultdict


CHARACTER_DATA_PATH = "./data/character.metadata.tsv"
MOVIE_DATA_PATH = "./data/movie.metadata.tsv"
SUMMARIES_DATA_PATH = "./data/plot_summaries.txt"
NAME_DATA_PATH = "./data/name.clusters.txt"
TYPE_DATA_PATH = "./data/tvtropes.clusters.txt"

import numpy as np
import pandas as pd

def cleaningCharacters():
    '''
    Clean and preprocess character data.

    Removes characters with negative ages, sets actor's height greater than 2.5 to NaN,
    and converts date columns to the correct format.

    Returns:
    - pandas.DataFrame: A DataFrame containing cleaned and preprocessed character data.

    Example:
    >>> cleaned_characters = cleaningCharacters()
    '''

    # Load character data using a hypothetical function readCharacters()
    character = readCharacters()

    # Remove characters with negative ages
    character["Actor_age_at_movie_release"] = character["Actor_age_at_movie_release"].apply(
        lambda x: np.nan if x < 0 else x
    )

    # Set actor's height greater than 2.5 to NaN
    character["Actor_height"] = character["Actor_height"].apply(
        lambda x: np.nan if x > 2.5 else x
    )

    # Convert date columns to the correct format
    character["Movie_release_date"] = pd.to_datetime(
        character["Movie_release_date"], format="mixed", utc=True, errors="coerce"
    )
    character["Actor_date_of_birth"] = pd.to_datetime(
        character["Actor_date_of_birth"], format="mixed", utc=True, errors="coerce"
    )

    return character

import pandas as pd

def readCharacters():
    '''
    Read character data 

    Returns:
    - pandas.DataFrame: A DataFrame containing character data with specified columns.

    Example:
    >>> character_data = readCharacters()
    '''

    # Define header for the character data
    CHARACTER_HEADER = [
        "Wikipedia_movie_ID",
        "Freebase_movie_ID",
        "Movie_release_date",
        "Character_name",
        "Actor_date_of_birth",
        "Actor_gender",
        "Actor_height",
        "Actor_ethnicity",
        "Actor_name",
        "Actor_age_at_movie_release",
        "Freebase_character/actor_map_ID",
        "Freebase_character_ID",
        "Freebase_actor_ID",
    ]

    # Load character data using pandas
    character = pd.read_table(CHARACTER_DATA_PATH, header=None, names=CHARACTER_HEADER)

    return character


def readMovie():
    '''
    Read movie data and performs data preprocessing converting dates to correct format.

    Returns:
    - pandas.DataFrame: A DataFrame containing movie data with parsed and formatted columns.

    Example:
    >>> movie_data = readMovie()
    '''

    # Define header for the movie data
    MOVIE_HEADER = [
        "Wikipedia_movie_ID",
        "Freebase_movie_ID",
        "Movie_name",
        "Movie_release_date",
        "Movie_box_office_revenue",
        "Movie_runtime",
        "Movie_languages",
        "Movie_countries",
        "Movie_genres",
    ]

    # Load movie data using pandas
    movie = pd.read_table(MOVIE_DATA_PATH, header=None, names=MOVIE_HEADER)

    # Helper function to format dictionary-like strings into lists
    def format_dict(x):
        n = len(x)
        if n == 0:
            return np.nan
        else:
            return list(x.values())

    # Parse and format specific columns
    try:
        movie["Movie_genres"] = movie["Movie_genres"].apply(json.loads).apply(format_dict)
        movie["Movie_countries"] = movie["Movie_countries"].apply(json.loads).apply(format_dict)
        movie["Movie_languages"] = movie["Movie_languages"].apply(json.loads).apply(format_dict)
    except TypeError:
        print("Data has already been parsed and modified.")

    # convert dates to datetime
    movie["Movie_release_date"] = pd.to_datetime(
        movie["Movie_release_date"], format="mixed", utc=True, errors="coerce"
    )
    # Exclude movies that are too long
    movie = cleanMovie(movie)

    return movie

def cleanMovie(movie):
    '''
    Excludes movies with runtime < 15000min (longest movie we found) 
    '''

    # Data cleaning
    movie["Movie_runtime"] = movie["Movie_runtime"].apply(
        lambda x: np.nan if 1 > x or x > 15000 else x
    )
    return movie

import pandas as pd

def readCharacterType():
    '''
    Read character types data and perform necessary data transformations.

    Returns:
    - pandas.DataFrame: A DataFrame containing character type data with specified columns.

    Example:
    >>> character_type_data = readCharacterType()
    '''

    # Load character types data using pandas
    character_type = pd.read_table(
        TYPE_DATA_PATH, header=None, names=["Character_type", "Instance"]
    )

    # Drop unnecessary column
    character_type.drop(columns="Instance", inplace=True)

    # Rename columns for consistency
    character_type.rename(
        columns={
            "char": "Character_name",
            "movie": "Movie_name",
            "id": "Freebase_character/actor_map_ID",
            "actor": "Actor_name",
        },
        inplace=True,
    )

    return character_type

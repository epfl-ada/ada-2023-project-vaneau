import pandas as pd
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import copy
from scipy.spatial import distance

# Import crawling libraries
import pickle
from src.crawler.crawler import *

# Import clustering libraries
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
from collections import defaultdict
from pyclustering.cluster.kmedoids import kmedoids
from sklearn.cluster import KMeans

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

def transition_matrix_genres(data):
    """
    Computes transition probabilities between movie genres for actors' roles across their careers.

    Parameters:
    data (pd.DataFrame): with actor and movie genre information

    Returns:
    transition_matrix (pd.DataFrame): Transition probability matrix
    """
    categories = [
        "Drama",
        "Comedy",
        "Thriller",
        "Action",
        "Family",
        "SF/Horror",
        "Romance",
        "BW/Silent",
        "History",
        "Culture",
        "Musical",
        "Sports",
    ]

    transition_matrix = pd.DataFrame(
        0, columns=categories, index=categories, dtype=float
    )

    for _, actor_data in data.groupby(level=0):
        previous_categories = [None, None, None]
        for _, row in actor_data.iterrows():
            genres = [row["First_Genre"], row["Second_Genre"], row["Third_Genre"]]
            for i, previous_genre in enumerate(previous_categories):
                for genre in genres:
                    if previous_genre and genre:
                        transition_matrix.at[previous_genre, genre] += 1
                previous_categories[i] = genres[i]

    return transition_matrix.div(transition_matrix.sum(axis=1), axis=0).fillna(0)


def display_transition_mat(P, legend):
    """
    Visualizes transition probability matrices as heatmaps based on the provided matrix and legend.

    Parameters:
    P (pd.Dataframe): Transition probability matrix
    legend (string): specifying the genre for the heatmap ('men' or 'women')

    Returns:
    Visualization of the transition probability matrix as a heatmap
    """
    plt.figure(figsize=(10, 8))
    # Change the colors of the heatmap accoding to the genre of the actor
    cmap = "YlGnBu" if legend == "men" else ("Reds" if legend == "women" else "Greens")
    
    # Change the title accoding to the genre of the actor
    title = (
        f"Transition Probability Matrix Heatmap of {legend}"
        if legend != "men" and legend != "women"
        else f"Transition Probability Matrix Heatmap of {legend} actors"
    )

    # Plot the heatmap
    sns.heatmap(P, cmap=cmap, annot=True, fmt=".2f", cbar=True, linewidths=0.5)
    plt.title(title)
    plt.xlabel("The next role is likely to be ...")
    plt.ylabel("If the last role was ...")
    plt.show()

def plotGenreDistributionFirstMovie(grouped):

    # Filter the data for the first film
    first_film_data = grouped[grouped["Film_Index"] == 1]

    # Initialize an empty DataFrame to store the genre distributions
    summed_genre_distribution = pd.DataFrame()

    # Loop over the three genres
    for col in ["First_Genre", "Second_Genre", "Third_Genre"]:
        genre_distribution = (
            first_film_data.pivot_table(
                index=col, columns="Actor gender", values="Actor_name", aggfunc="count"
            )
            .fillna(0)
            .astype(int)
        )

        summed_genre_distribution = summed_genre_distribution.add(
            genre_distribution, fill_value=0
        )

    # Calculate the total sum of genres for both genders
    total_sum_F = summed_genre_distribution["F"].sum()
    total_sum_M = summed_genre_distribution["M"].sum()

    # Calculate the density for 'M' and 'F'
    male_density = summed_genre_distribution["M"] / total_sum_M
    female_density = summed_genre_distribution["F"] / total_sum_F

    # Plotting the histogram for summed_genre_distribution
    plt.figure(figsize=(12, 8))

    # Bar width and positions for better visualization
    bar_width = 0.35
    index = np.arange(len(summed_genre_distribution.index))

    # Plotting the histogram with density on the y-axis
    plt.bar(
        index - bar_width / 2,
        male_density,
        bar_width,
        alpha=0.7,
        color="blue",
        label="Male",
    )
    plt.bar(
        index + bar_width / 2,
        female_density,
        bar_width,
        alpha=0.7,
        color="red",
        label="Female",
    )

    plt.xlabel("Genres")
    plt.ylabel("Density")
    plt.title("Density of genre distribution for each gender in their first movie")
    plt.xticks(index, summed_genre_distribution.index, rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.show()

def readCharacterData():
    # Preprocess the data
    CHAR_PATH = "./data/full_characters_final.pkl"
    nlp_data = pd.read_pickle(CHAR_PATH)

    # Drop duplicated movies
    nlp_data.drop_duplicates(subset=["Wikipedia_movie_ID"], inplace=True)

    # Relevant columns from nlp_data
    columns_name_nlp = [
        "Actor_name",
        "MainCharType",
        "Actor gender",
        "Actor date of birth",
        "Actor_age",
        "Fb_actor_id",
        "Wikipedia_movie_ID",
        "Fb_movie_id",
        "Probabilities",
    ]

    # Merge relevant columns with movie data
    merged_data = pd.merge(
        nlp_data[columns_name_nlp],
        movie[["Wikipedia_movie_ID", "Movie_release_date", "Movie_main_genres"]],
        on="Wikipedia_movie_ID",
        how="left",
    )

    # Sort data by 'Fb_actor_id', 'Movie_release_date'
    merged_data.sort_values(["Fb_actor_id", "Movie_release_date"], inplace=True)

    # Calculate film index for each actor based on major roles and release date
    merged_data["Film_Index"] = merged_data.groupby("Fb_actor_id").cumcount() + 1

    # Count number of films per actor
    films_per_actor = merged_data["Actor_name"].value_counts()

    # Add a column with the number of films each actor played in
    merged_data["Num_films_played"] = merged_data["Actor_name"].map(films_per_actor)

    # Group data by actor name and sort by movie release date
    grouped = merged_data.groupby("Actor_name").apply(
        lambda x: x.sort_values("Movie_release_date")
    )

    # Extract the first three genres for transition matrix
    grouped["First_Genre"] = grouped["Movie_main_genres"].apply(
        lambda x: x[0] if isinstance(x, list) and len(x) > 0 else None
    )
    grouped["Second_Genre"] = grouped["Movie_main_genres"].apply(
        lambda x: x[1] if isinstance(x, list) and len(x) > 1 else None
    )
    grouped["Third_Genre"] = grouped["Movie_main_genres"].apply(
        lambda x: x[2] if isinstance(x, list) and len(x) > 2 else None
    )

    return grouped

def vectorize_genres(list_genres, genres_dict):
    if not (type(list_genres) is list):
        return np.array([0.0] * len(genres_dict))
    else:
        result = np.array([0.0] * len(genres_dict))
        for genre in list_genres:
            result[genres_dict[genre]] = 1.0
        result /= np.linalg.norm(result)
        return result
    
def plotPCA():
    fig = plt.figure(figsize=(10, 8))
    n = 5
    ax = fig.subplots(n, n)
    for i in range(n):
        plt.subplot(n, n, i * (n + 1) + 1)
        plt.hist(transformed_data[:, i])
        for j in range(i + 1, n):
            plt.subplot(n, n, n * i + j + 1)
            plt.hexbin(
                transformed_data[:, i],
                transformed_data[:, j],
                bins="log",
                cmap="Blues",
            )
    plt.tight_layout()


def clusterPCA(transformed_data):
    nb_cluster_list = np.arange(1, 200, 10)
    residual_sum_of_square_list = []
    for nb_cluster in nb_cluster_list:
        k_means = KMeans(n_clusters=nb_cluster, n_init=5)
        residual_sum_of_square = 0.0
        k_means.fit(transformed_data)
        for i_label in range(len(k_means.labels_)):
            centroid = k_means.cluster_centers_[k_means.labels_[i_label]]
            residual_sum_of_square += ((transformed_data[i_label, :] - centroid) ** 2).sum()
        residual_sum_of_square_list.append(residual_sum_of_square)
    return residual_sum_of_square_list, nb_cluster_list

def plot_clusters_and_histogram(cluster_date_mean, cluster_date_std, index_sort, figsize=(15, 6)):
    """
    Plot statistics of clusters across years and a histogram of cluster mean date.
    """

    # Create a figure with two subplots side by side
    plt.figure(figsize=figsize)

    # First subplot: Line plot of cluster mean date across years
    plt.subplot(1, 2, 1)
    plt.plot(cluster_date_mean.values[index_sort])
    plt.fill_between(
        np.arange(len(cluster_date_mean)),
        (cluster_date_mean - cluster_date_std).values[index_sort],
        (cluster_date_mean + cluster_date_std).values[index_sort],
        color="b",
        alpha=0.1,
    )
    plt.xlabel("Cluster sorted by mean date year")
    plt.ylabel("Mean date year")
    plt.title("When do clusters appear ?")

    # Second subplot: Histogram of cluster mean date
    plt.subplot(1, 2, 2)
    sns.histplot(cluster_date_mean, kde=True)
    plt.xlabel("Mean date year")
    plt.title("Distribution of Cluster Mean Date")

    # Adjust layout to prevent subplot overlap
    plt.tight_layout()

    # Show the combined plot
    plt.show()

def compute_shift_significance_age(group, prev_years, future_years):
    significance_values = []

    for i in range(len(group)):
        current_age = group.iloc[i]["Actor_age_at_movie_release"]
        current_vector = group.iloc[i].drop("Actor_age_at_movie_release").values[0]

        # Calculate shift significance for the current age
        prev_age_data = group[
            (group["Actor_age_at_movie_release"] < current_age)
            & (group["Actor_age_at_movie_release"] >= current_age - prev_years)
        ]
        future_age_data = group[
            (group["Actor_age_at_movie_release"] > current_age)
            & (group["Actor_age_at_movie_release"] <= current_age + future_years)
        ]

        if len(prev_age_data) > 0 and len(future_age_data) > 0:
            prev_distances = [
                distance.cosine(current_vector, vec[0])
                for vec in prev_age_data.drop(
                    "Actor_age_at_movie_release", axis=1
                ).values
            ]
            avg_prev_distance = np.mean(prev_distances)
            std_prev_distance = np.std(prev_distances)

            future_distances = [
                distance.cosine(current_vector, vec[0])
                for vec in future_age_data.drop(
                    "Actor_age_at_movie_release", axis=1
                ).values
            ]
            std_future_distance = np.std(future_distances)

            significance = avg_prev_distance / (
                1 + std_future_distance * std_prev_distance
            )
            # significance = np.std(prev_distances+future_distances)
            significance_values.append((current_age, significance))

    return pd.DataFrame(
        significance_values,
        columns=["Actor_age_at_movie_release", "Shift_Significance"],
    ).set_index("Actor_age_at_movie_release")

def actor_genre_year(actor):
    result = []
    for index, row in character_movie[character_movie["Actor_name"] == actor][
        ["Movie_main_genres", "Actor_age_at_movie_release"]
    ].iterrows():
        sublist = row["Movie_main_genres"]
        for genre in sublist:
            result.append((genre, row["Actor_age_at_movie_release"]))
    return pd.DataFrame(result, columns=["genre", "age"])

def readInLevensteinData():

    # Preprocess the data
    CHAR_PATH = "./generated/full_characters_final"
    nlp_data = pd.read_pickle(CHAR_PATH)
    probabilities = nlp_data.iloc[-2]["Probabilities"]

    # Assuming your DataFrame is named df
    df = nlp_data.dropna(subset=["Probabilities", "Actor_age"])
    print(df.shape)
    desired_columns = [
        "Actor_name",
        "MainCharType",
        "Actor gender",
        "Actor date of birth",
        "Actor_age",
        "Fb_actor_id",
        "Wikipedia_movie_ID",
        "Fb_movie_id",
        "Probabilities",
    ]
    df = df[desired_columns]
    merged_data = pd.merge(
        df,
        movie[["Wikipedia_movie_ID", "Movie_release_date", "Movie_main_genres"]],
        on="Wikipedia_movie_ID",
        how="left",
    )

    # Get rid of rows where 'Movie_main_genres' is NaN
    merged_data.dropna(subset=["Movie_main_genres"], inplace=True)

    # Add the Film_index colum
    # Sort the DataFrame by 'Freebase_actor_ID', 'Actor_age', 'Character', and 'Movie_release_date'
    merged_data.sort_values(
        ["Fb_actor_id", "Actor_age", "Movie_release_date"], inplace=True
    )

    # Calculate the i-th film for each actor based on major roles and movie release date
    merged_data["Film_Index"] = (
        merged_data.groupby("Fb_actor_id").cumcount()
        + 1  # Adding 1 to start indexing from 1 instead of 0
    )

    # Counting the number of films per actor
    films_per_actor = merged_data["Actor_name"].value_counts()

    # Adding a new column with the number of films each actor played in
    merged_data["Num_films_played"] = merged_data["Actor_name"].map(films_per_actor)

    # Group the data by actor name and sort by movie release date
    grouped = merged_data.groupby("Actor_name").apply(
        lambda x: x.sort_values("Movie_release_date")
    )

    return grouped


def encode_career_genres(df):
    actors_summary = []

    for actor, actor_group in df.groupby(level=0):
        nb_films_played = actor_group["Num_films_played"].values[0]

        actor_summary = {
            "Actor_name": actor,
            "Gender": actor_group["Actor gender"].values[0],
            "Num_films_played_with_known_genres": nb_films_played,
            "Fb_actor_ID": actor_group["Fb_actor_id"].values[0],
        }

        career_code = ""

        if nb_films_played > 2:
            # We encode one character for each triplet of consecutive movies in the actor's career
            for i in range(nb_films_played - 2):
                genres_played_over_three_movies = []
                # Add genres of previous movie
                genres_played_over_three_movies.extend(
                    actor_group["Movie_main_genres"].values[i]
                )
                # Add genres of following movie
                genres_played_over_three_movies.extend(
                    actor_group["Movie_main_genres"].values[i + 1]
                )
                # Add genres of following movie of the previous one
                genres_played_over_three_movies.extend(
                    actor_group["Movie_main_genres"].values[i + 2]
                )
                # Use the Counter subclass to count occurences of each genre in the list
                occ_by_genre = Counter(genres_played_over_three_movies)
                score_by_genre = {}
                # Use weights
                for _, (genre, score) in enumerate(occ_by_genre.items()):
                    score_by_genre[genre] = score * weights[genre]
                # Get dominant genre
                dominant_genre = max(score_by_genre, key=score_by_genre.get)
                career_code += genres_encoding_dic.get(dominant_genre, "0")

        else:  # Actor has played in only one movie
            career_code = genres_encoding_dict.get(
                actor_group.iloc[0, "Movie_main_genres"][0], "0"
            )

        actor_summary["Career_code"] = career_code

        actors_summary.append(actor_summary)

    summary_df = pd.DataFrame(actors_summary)

    return summary_df


def vectorize_roles_normalized(list_of_roles):
    "Takes a list of roles of any length, returns a normalized vector"

    dico = {
        "Complex Personalities": 0,
        "Adventurers and Heroes": 0,
        "Stereotypes and Tropes": 0,
        "Occupation and Professions": 0,
        "Moral Ambiguity and Antagonists": 0,
        "Everyday Characters and Tropes": 0,
        "Emotional and Romantic Tropes": 0,
    }

    # Count the number of roles played in each of the seven character tropes (MainCharTypes)
    for trope in list_of_roles:
        dico[trope] += 1

    vector = [value for key, value in dico.items()]

    # Normalize
    tot = sum(vector)
    norm_vector = [v / tot for v in vector]

    return norm_vector


def total_cost(centers, clusters, distance_matrix):
    cost = 0
    for index, cluster in enumerate(clusters):
        center = centers[index]
        for point in cluster:
            cost += distance_matrix[center, point]
    return cost
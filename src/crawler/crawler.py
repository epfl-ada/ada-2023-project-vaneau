import requests
import pandas as pd
import numpy as np
import math
from urllib.parse import quote
import json
import concurrent.futures
import pickle

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NmFkOWYzNjBiNWRjYWM0Y2U3NWIwOGExYjlmN2ZjNCIsInN1YiI6IjY1NGJiMDY5ZmQ0ZjgwMDEzY2ViMTgzNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NhqQyd6b913CVIYrZofXA9XL07yXtAfsVI1A7s4MBmM",
}


def make_request(url):
    raw_response = requests.get(url, headers=headers).text
    response = json.loads(raw_response)
    return response


def get_identifier(name, year):
    encoded_movie = quote(name)
    url = f"https://api.themoviedb.org/3/search/movie?query={encoded_movie}&include_adult=false&language=en-US&page=1&year={year}"
    response = make_request(url)
    results = response.get("results", [])
    if results:
        id = results[0].get("id", 0)
        return id
    else:
        return 0


def get_movie_details(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    response = make_request(url)
    return response


def get_movie_credits(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"
    response = make_request(url)
    response = response.get("cast")
    return response


def get_external_identifier(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/external_ids"
    response = make_request(url)
    return response


def get_movie(name, year):
    id = get_identifier(name, year)
    if id:
        details = get_movie_details(id)
        credits = get_movie_credits(id)
        ids = get_external_identifier(id)
        return [details, credits, ids]

    else:
        return [None, None, None]


def changeNA(value):
    if value is None:
        return pd.NA
    else:
        return value


def zeroToNA(value):
    if value is None or (value is pd.NA):
        return pd.NA
    elif abs(value) < 1e-7:
        return pd.NA
    else:
        return value


def extractRevenue(value):
    if not (value is None) and not (math.isnan(value)):
        return value.get("revenue", pd.NA)
    else:
        return pd.NA


def extractBudget(value):
    if not (value is None) and not (math.isnan(value)):
        return value.get("budget", pd.NA)
    else:
        return pd.NA


def process_chunk(start, end, movie_df):
    for i in range(start, end):
        name = movie_df.loc[i, 1]
        year = movie_df.loc[i, "year"]
        try:
            details, credits, ids = get_movie(name, year)
            movie_df.loc[i, "details"] = str(details)
            movie_df.loc[i, "credits"] = str(credits)
            movie_df.loc[i, "ids"] = str(ids)

            if not (i % 99):
                print(f"iteration: {i}", " details: ", details, " ids: ", ids)
            if not (i % 999):
                with open(f"./iterations/crawling_{i}.obj", "wb") as file:
                    pickle.dump(movie_df, file)
        except Exception as error:
            print(f"iteration: {i}, error: {error}")

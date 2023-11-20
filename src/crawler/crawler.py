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
        id = results[0].get('id', 0)
        return (id)
    else:
        return (0)

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
    evalued = eval(value)
    if not evalued:
        return (pd.NA)
    else:
        return (value)


def extractRevenue(value):
    if type(value) != pd._libs.missing.NAType:
        evalued = eval(value)
        return (evalued.get('revenue', pd.NA))
    else:
        return (pd.NA)


def extractRevenue(value):
    if type(value) != pd._libs.missing.NAType:
        evalued = eval(value)
        return (evalued.get('revenue', pd.NA))
    else:
        return (pd.NA)


def extractRevenue(value):
    if type(value) != pd._libs.missing.NAType:
        evalued = eval(value)
        return (evalued.get('revenue', pd.NA))
    else:
        return (pd.NA)
      
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
            print(f'iteration: {i}, error: {error}')

def extractCountry(row):
    not_found = '--'
    details = row['details']
    if type(details) != pd._libs.missing.NAType:
        details = eval(row['details'])
        prod = details.get('production_countries', -1)
        if prod:
            country = prod[-1].get('iso_3166_1', not_found)
            return (country)
        return not_found
    return not_found


def extractRoles(row):
    '''
    Extracts the different cast roles from TMDB into their own 
    categories.
    Could be improved performance wise
    '''

    roles = {'Acting': [], 'Crew': [], 'Directing': []}
    if row:
        row = eval(row)
        for character in row:
            role = character.get('known_for_department', 'NoRole')
            roles.get(role, []).append(character.get('name'))
    return(pd.Series([roles['Acting'], roles['Crew'], roles['Directing']]))

def extractProductionCompanies(row):
    production_companies = []
    if row:
        row = eval(row)
        companies = row.get('production_companies', [])
        for company in companies:
            production_companies.append(company.get('name','none'))
    return(production_companies)

def extractPopularityRating(row):
    rating, votes = None, 0
    if row:
        row = eval(row)
        rating = row.get('vote_average', None)
        votes = row.get('vote_count', 0)
    return(pd.Series([rating,votes]))

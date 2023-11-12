import numpy as np

CATEGORIZED_GENRES = {
    "Drama": [
        "Drama",
        "Romantic drama",
        "Period piece",
        "Comedy-drama",
        "Family drama",
        "Political drama",
        "Melodrama",
        "Crime Drama",
        "Costume drama",
    ],
    "Comedy": [
        "Comedy",
        "Comedy film",
        "Romantic comedy",
        "Comedy-drama",
        "Black comedy",
        "Parody",
        "Slapstick",
    ],
    "Romance": ["Romance Film", "Romantic drama", "Romantic comedy"],
    "Black-and-white": ["Black-and-white"],
    "Action": ["Action", "Adventure", "Action/Adventure", "Action Thrillers", "Spy"],
    "Thriller": [
        "Thriller",
        "Crime Fiction",
        "Crime Thriller",
        "Psychological thriller",
        "Suspense",
        "Film noir",
        "Action Thrillers",
        "Spy",
    ],
    "Short Film": ["Short Film"],
    "World Cinema": ["World Cinema"],
    "Indie": ["Indie"],
    "Documentary": ["Documentary", "Docudrama", "Concert film", "Rockumentary"],
    "Horror": ["Horror", "Slasher"],
    "Silent film": ["Silent film"],
    "Family": ["Family Film", "Children's/Family", "Teen", "Children's"],
    "Musical": ["Musical", "Music"],
    "Animation": ["Animation"],
    "Mystery": ["Mystery"],
    "Science Fiction": ["Science Fiction", "Fantasy", "Supernatural"],
    "War": ["War film"],
    "Asian Cinema": [
        "Japanese Movies",
        "Chinese Movies",
        "Filipino Movies",
        "Tamil cinema",
    ],
    "Western": ["Western", "Spaghetti Western", "Revisionist Western"],
    "Film adaptation": ["Film adaptation"],
    "Biography": [
        "Biography",
        "Biographical film",
        "Biopic [feature]",
        "Coming of age",
    ],
    "Bollywood": ["Bollywood"],
    "Sports": ["Sports", "Martial Arts Film"],
    "LGBT": ["LGBT", "Gay Themed", "Gay", "Gay Interest"],
    "Television movie": ["Television movie"],
    "History": ["Period piece", "History", "Historical fiction"],
    "Culture": ["Cult", "Culture & Society", "Art film"],
    "Satire": ["Satire"],
}

OLD_TO_NEW_GENRES = {
    "Thriller": ["Thriller"],
    "Science Fiction": ["Science Fiction"],
    "Horror": ["Horror"],
    "Adventure": ["Action"],
    "Supernatural": ["Science Fiction"],
    "Action": ["Action"],
    "Mystery": ["Mystery"],
    "Biographical film": ["Biography"],
    "Drama": ["Drama"],
    "Crime Drama": ["Drama"],
    "Crime Fiction": ["Thriller"],
    "Psychological thriller": ["Thriller"],
    "Short Film": ["Short Film"],
    "Silent film": ["Silent film"],
    "Indie": ["Indie"],
    "Black-and-white": ["Black-and-white"],
    "Comedy": ["Comedy"],
    "Family Film": ["Family"],
    "Fantasy": ["Science Fiction"],
    "Musical": ["Musical"],
    "Japanese Movies": ["Asian Cinema"],
    "Action/Adventure": ["Action"],
    "Romantic comedy": ["Comedy", "Romance"],
    "Comedy-drama": ["Drama", "Comedy"],
    "Romantic drama": ["Drama", "Romance"],
    "Romance Film": ["Romance"],
    "Costume drama": ["Drama"],
    "War film": ["War"],
    "Period piece": ["Drama", "History"],
    "Film adaptation": ["Film adaptation"],
    "Animation": ["Animation"],
    "Children's/Family": ["Family"],
    "Comedy film": ["Comedy"],
    "Coming of age": ["Biography"],
    "Suspense": ["Thriller"],
    "Crime Thriller": ["Thriller"],
    "Black comedy": ["Comedy"],
    "Bollywood": ["Bollywood"],
    "Martial Arts Film": ["Sports"],
    "Chinese Movies": ["Asian Cinema"],
    "Western": ["Western"],
    "Parody": ["Comedy"],
    "Cult": ["Culture"],
    "Slapstick": ["Comedy"],
    "Biopic [feature]": ["Biography"],
    "Sports": ["Sports"],
    "Political drama": ["Drama"],
    "Historical fiction": ["History"],
    "Culture & Society": ["Culture"],
    "Biography": ["Biography"],
    "Documentary": ["Documentary"],
    "Television movie": ["Television movie"],
    "Satire": ["Satire"],
    "Action Thrillers": ["Action", "Thriller"],
    "Slasher": ["Horror"],
    "Film noir": ["Thriller"],
    "History": ["History"],
    "LGBT": ["LGBT"],
    "Music": ["Musical"],
    "Melodrama": ["Drama"],
    "Concert film": ["Documentary"],
    "Docudrama": ["Documentary"],
    "Teen": ["Family"],
    "Art film": ["Culture"],
    "Filipino Movies": ["Asian Cinema"],
    "Spy": ["Action", "Thriller"],
    "Gay": ["LGBT"],
    "Gay Interest": ["LGBT"],
    "Gay Themed": ["LGBT"],
    "Rockumentary": ["Documentary"],
    "Children's": ["Family"],
    "Spaghetti Western": ["Western"],
    "Revisionist Western": ["Western"],
    "Tamil cinema": ["Asian Cinema"],
}


def clean_genres(genre_list, dict_genres):
    categorized_result = []

    for genre in genre_list:
        for main_genre, sub_genres in dict_genres.items():
            if genre in sub_genres:
                if main_genre not in categorized_result:
                    categorized_result.append(main_genre)
    if len(categorized_result) == 0:
        return np.nan
    return categorized_result

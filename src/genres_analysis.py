import numpy as np

CATEGORIZED_GENRES = {
    "Drama": ["Drama","Romantic drama","Period piece","Comedy-drama",
              "Family drama","Political drama","Melodrama","Crime Drama","Costume drama"],
    "Comedy": ["Comedy","Comedy film","Romantic comedy","Comedy-drama","Black comedy","Parody","Slapstick"],
    "Romance": ["Romance Film","Romantic drama","Romantic comedy"],
    "Black-and-white": ["Black-and-white"],
    "Action": ["Action", "Adventure","Action/Adventure","Action Thrillers","Spy"],
    "Thriller": ["Thriller","Crime Fiction","Crime Thriller","Psychological thriller","Suspense","Film noir","Action Thrillers","Spy"],
    "Short Film": ["Short Film"],
    "World Cinema": ["World Cinema"],
    "Indie": ["Indie"],
    "Documentary": ["Documentary", "Docudrama", "Concert film", "Rockumentary"],
    "Horror": ["Horror","Slasher"],
    "Silent film": ["Silent film"],
    "Family": ["Family Film","Children's/Family","Teen","Children's"],
    "Musical": ["Musical","Music"],
    "Animation": ["Animation"],
    "Mystery": ["Mystery"],
    "Science Fiction": ["Science Fiction","Fantasy","Supernatural"],
    "War": ["War film"],
    "Asian Cinema": ["Japanese Movies", "Chinese Movies", "Filipino Movies", "Tamil cinema"],
    "Western": ["Western", "Spaghetti Western", "Revisionist Western"],
    "Film adaptation": ["Film adaptation"],
    "Biography": ["Biography","Biographical film","Biopic [feature]","Coming of age"],
    "Bollywood": ["Bollywood"],
    "Sports": ["Sports","Martial Arts Film"],
    "LGBT": ["LGBT", "Gay Themed", "Gay", "Gay Interest"],
    "Television movie": ["Television movie"],
    "History": ["Period piece","History","Historical fiction"],
    "Culture": ["Cult","Culture & Society","Art film"],
    "Satire": ["Satire"]
    }

def clean_genres(genre_list,dict_genres):
    categorized_result = []

    for genre in genre_list:
        for main_genre, sub_genres in dict_genres.items():
            if genre in sub_genres:
                if main_genre not in categorized_result:
                    categorized_result.append(main_genre)
    if len(categorized_result)==0:
        return np.nan
    return categorized_result

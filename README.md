# Gendered trajectories across movie genres

# [Data Story here](https://epfl-ada.github.io/ada-2023-project-vaneau/)
# Shifting Roles: Decoding Hollywood's Career Evolution

## Abstract

**TODO**


## Research questions

- Can we define a career path through the evolution of genres of the movies an actor has played in ?

- Are there significant differences in genre trajectories between genders?

## Methods

- **Genres clustering** and **dimensionality reduction** (pre-analytical step) : in the movie dataset, 363 genres are used. This makes the data very sparse and too difficult to interpret regarding what our goal is. By classifying movies into a smaller number of genres, we increase the number of datapoints per class, making our following analysis more relevant. Two methods are tested : dentrogram based on co-occurences and PCA (compute abstract "eigengenres" and keep the ones that explain the most of our movie dataset)

- **Markov chain for timeseries evolution** : for each actor, keep track of the order of the movies he/she played in, and use this to infer typical transitions between genres from a movie to the following one  (transition matrix). As the choice of the next movie genre for an actor might not only depend of the very previous one, but of his career overall, different memory sizes for Markov chains might be tested.

- **NLP** : embeddings of movie synopsis thanks to BERT model (not used in final version)
- **Crawling** : get additional data on box-office revenues and movie budgets (was not used in final version.)





## Contribution to the work in the team

- **Augustin** : website + PCA on the genres
- **Ben** : web crawling + introduction/conclusion
- **Erwann** : Markov chains
- **Lucas** : Levenshtein distance + nlp
- **Romain** : genre clustering + shift time series



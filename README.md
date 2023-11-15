# ada-2023-project-vaneau

# Title

## Abstract
*should be 150 words* What’s the motivation behind your project? What story would you like to tell, and why?

The motivation for our project stems from a surprising disparity: when looking at the distribution of roles based on actors' ages, the “golden age” is about 40 years old for men but is only 25 years old for women.

Such a gap might relate to different career developments and begs the question : are there traditional career paths in the movie industry ?

To answer it, restraining ourselves to Hollywood, we first explore the typical jumps between movie genres that actors operate during their career through transition matrices.

Then, we focus on the type of characters actors are asked to play, using the same tool. As our TV tropes dataset lacks in data, we hope to enlarge it through role characterization thanks to NLP technics performed on movie synopsis.

Eventually, we dive into correlations between an actor's first big success at the box-office and the aftermath for its career development.

(150 words)

NOTE :  *Restraining ourselves to Hollywood : only American movies or any actors that played in an American movie… but could have played in other countries as well ? *

-----

The goal of our study is to determine if Hollywood is still innovative, creative, or ambitious. To determine this hard to measure feature, we are going to look at several characteristics of the movies.

First considering movie genres, we observe the predominant ones through the year. The use of an evolutionary tree enables to better visualize it and see the combinations that have been use. This analyze gives the breaking points in history and the patterns between. Therefore, we can see if Hollywood is focusing on only a small number of genres.

Second dwelling into the actors, we look at the diversity of actors used. Looking at the character type evolution over time (linked to movie genres evolution), we determine if it is linked to actors’ development. We see if some actors become very popular thanks to Hollywood evolution.


## Research questions
 *A list of research questions you would like to address during the project.*


## Proposed additional datasets

- @Ben : additional data on box-office revenues and movie budgets, thanks to TMDb API
- Dataset correction : retrieve actor's ethnicity based on the corresponding freebaseID

## Methods

- Markov chain for timeseries evolution : for each actor, keep track of the order of the movies he/she played in, and use this to infer typical transitions between genres from a movie to the following one  (transition matrix). As the choice of the next movie genre for an actor might not only depend of the very previous one, but of his career overall, different memory sizes for Markov chains should be tested.
- Genres clustering and dimensionality reduction (pre-analytical step) : in the movie dataset, 363 genres are used. This makes the data very sparse and too difficult to interpret regarding what our goal is. By classifying movies into a smaller number of genres, we increase the number of datapoints per class, making our following analysis more relevant. Two methods are tested : dentrogram based on co-occurences (not satisfying) and PCA (compute abstract "eigengenres" and keep the ones that most explain our movie dataset)
- NLP : embeddings of movie synopsis thanks to BERT model
- Crawling : get additional data on box-office revenues and movie budgets

## Proposed timeline

## Organisation within the team

## Question for TAs


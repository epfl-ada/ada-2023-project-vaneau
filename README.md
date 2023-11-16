# ada-2023-project-vaneau

# Title

## Abstract

The motivation for our project stems from a surprising disparity: when looking at the distribution of roles based on actors' ages, the “golden age” is about 40 years old for men but is only 25 years old for women.

Such a gap might relate to different career developments and begs the question : are there traditional career paths in the movie industry ?

To answer it, restraining ourselves to Hollywood, we first explore the typical jumps between movie genres that actors/actresses operate during their career through transition matrices.

Then, we focus on the type of characters actors/actresses are asked to play, using the same tool. As our TV tropes dataset lacks in data, we hope to enlarge it through role characterization thanks to NLP technics performed on movie synopsis.

Eventually, we dive into correlations between an actor's first big success at the box-office and the aftermath for its career development.


## Research questions

What are the notable differences, if any, between the career trajectories of men and women in Hollywood? How do gender-based factors impact opportunities, roles, and longevity in the industry?

Is there a correlation between the genres actors engage with and the subsequent movies they appear in? Do actors tend to be typecast based on the genres they initially perform in, and how does this influence their career paths?

To what extent do roles in blockbuster films shape an actor's career trajectory in Hollywood?


## Proposed additional datasets

- Additional data on box-office revenues, movie budgets and other details, using TMDb API
- Dataset correction : retrieve actors' ethnicities based on the freebase IDs


## Methods

- Markov chain for timeseries evolution : for each actor, keep track of the order of the movies he/she played in, and use this to infer typical transitions between genres from a movie to the following one  (transition matrix). As the choice of the next movie genre for an actor might not only depend of the very previous one, but of his career overall, different memory sizes for Markov chains might be tested.
- Genres clustering and dimensionality reduction (pre-analytical step) : in the movie dataset, 363 genres are used. This makes the data very sparse and too difficult to interpret regarding what our goal is. By classifying movies into a smaller number of genres, we increase the number of datapoints per class, making our following analysis more relevant. Two methods are tested : dentrogram based on co-occurences (not satisfying) and PCA (compute abstract "eigengenres" and keep the ones that explain the most of our movie dataset)
- NLP : embeddings of movie synopsis thanks to BERT model
- Crawling : get additional data on box-office revenues and movie budgets


## Proposed timeline (3 weeks starting in December)

week 1 - Start with the Genres clustering, Finalize the movie crawling, Prepare the pipeline for the Markov chain analysis
week 2 - Perform the Markov chain analysis and the NLP on movie embeddings
week 3 - Write the data story and build the website in parallel, Clean the github repository


## Organisation within the team

- Markov chain for timeseries evolution: Erwann
- Genres clustering and dimensionality reduction: Romain and Augustin
- NLP: Lucas
- Crawling and analysis of correlation between career path and movie revenues of the first film: Ben


## Question for TAs


# Genders and genres
<!-- Intro by Ben -->
TODO BEN

Key question : **How do actors of different genders evolve through different genres ?**

# Characterizing genres

A first look at our data more than 360 genres, therefore it seems relevant to reduce this diversity to have a more consistent analysis after.

## Genre clustering
<!-- Romain -->

A first idea to reduce the number of genres is to do clustering and then define main genres by hand. Therefore we need to define a distance between each genre. As it appears that a movie is defined by several genres, the co-occurrence of genres will be used to quantify their proximity (high co-occurrence means close genres).

A naive approach would be to directly do a clustering on the 363 genres. However,this clustering is not satisfying due to the nature of our data: one genre can be expressed in several ways (ex: “Comedy and Comedy film”) and one genre can represent in reality several genres (ex: “Comedy-drama”). A manual filtering has to be done before clustering.

We filter the genres by not taking into account the genres with less than 500 movies (it does not significantly lower the number of films with genres) and by gathering the others into 30 custom main genres by hand. Looking now at the co-occurrence matrix, the cluster appears and it is confirmed by the dendrogram (figure: dendrogram). The threshold of the clustering algorithm is chosen such that we have a dozen of main genres (figure: main genre value counts).

Looking at the repartition of genres along time, clear trends appear like the fall of Black & White and silent movies (figure: Proportion of movies of given genre along time)


## Creating "Eigengenres" - PCA analysis
<!-- Augustin -->
TODO AUGUSTIN


# Defining genre evolution through the career - Markov chains
<!-- Erwann -->
TODO ERWANN


# Comparing career timelines among actors

We have a good description of the career of an actor through the transition matrix. However, this description is a summary of a career, we want now to look at the evolution of the actor through its life by looking at shifts in genres played.

## Shift time series
<!-- Romain -->
TODO ROMAIN


## Using the Levenshtein distance
<!-- Lucas -->
TODO LUCAS


# Conclusion
<!-- Ben -->
TODO BEN
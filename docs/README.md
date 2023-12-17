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
The task of reducing the number of genres can also be seen as a dimensionality reduction task, for which we have one great technique : Principal Component Analysis. Its idea is to project each movie onto all its genres (one-hot encoding) and then find the directions that explains the most variance of the dataset. Hence, the found directions : the so-called eigengenres help us define fewer dimensions to describe the movie genres while keeping most of the information.

The explained variance from a specific eigengenre can be deduced from its eigenvalue. Ranking those according to the latter value will enable us to select only the most significant eigengenres. 


<img src="/ada-2023-project-vaneau/assets/img/eigengenre_explained_variance.png" style="display: block; margin: auto;" />

This figure shows that with only 52 eigengenres we can keep 90% of the information contained in the dataset.

Visualizing those 52 eigengenres gives us the following plot:

<img title="Eigengenres visualization" alt="Shows increasing added variance among eigenvectors from PCA" src="/img/eigengenre_visualization.png">

If we take the third eigengenre from the left for instance, it groups genres that we would have fitted together : namely ‘silent_films’, ‘black_and_white’, and ‘short_films’.

Another observation is that genres that are rarely used are not significant in establishing eigenvectors.



# Defining genre evolution through the career - Markov chains
<!-- Erwann -->
TODO ERWANN


# Comparing career timelines among actors

We have a good description of the career of an actor through the transition matrix. However, this description is a summary of a career, we want now to look at the evolution of the actor through its life by looking at shifts in genres played.

## Shift time series
<!-- Romain -->
This method aims to characterize the change in genres played through a scalar number each year the actor played. To do that we first translate the genre obtained after the clustering for each movie into a vector of size the number of main genres and values 1 if the movie belongs to the genre, 0 otherwise. Then, for each age at which the actor played we compute the mean vector and we try to detect shifts in these vectors.

The scalar value used to quantify the shift is at the heart of this method. In our analysis, we use, at a given age, the films three years before and after this age to detect the shift. We compute the mean cosine distance between the vector of the current age studied and the vectors of the 3 previous years and to balance this value we use the standard deviation of the distance between the current age vector and those of the surrounding years.

This method works quite well for actors with long careers (figure: mel blanc). But it does not reveal any difference between men and women's career paths.



## Using the Levenshtein distance
<!-- Lucas -->
TODO LUCAS


# Conclusion
<!-- Ben -->
TODO BEN
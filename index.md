---
layout: post
title:  "Gendered trajectories across movie genres"
author: Ben, Lucas, Romain, Erwann, and Augustin
cover:  "/assets/movie_banner.jpg"
---

<!-- Intro by Ben -->
**INTRODUCTION : TODO BEN**

Key question : **How do actors of different genders evolve through different genres in the movie industry?**

# Characterizing genres

A first look at our data more than **360** genres, therefore it seems relevant to reduce this diversity to have a more consistent analysis after.

## Genre clustering
<!-- Romain -->

A first idea to reduce the number of genres is to do clustering and then define main genres by hand. Therefore we need to define a distance between each genre. As it appears that a movie is defined by several genres, **the co-occurrence of genres will be used to quantify their proximity** (high co-occurrence means close genres).

A naive approach would be to directly do a clustering on the 363 genres. However,this clustering is not satisfying due to the **nature of our data**: one genre can be expressed in several ways (ex: “Comedy and Comedy film”) and one genre can represent in reality several genres (ex: “Comedy-drama”). A manual filtering has to be done before clustering.

We **filter** the genres by not taking into account the genres with less than 500 movies (it does not significantly lower the number of films with genres) and by gathering the others into 30 custom main genres **by hand**. Looking now at the co-occurrence matrix, the **cluster appears** and it is confirmed by the dendrogram. The threshold of the clustering algorithm is chosen such that we have a **dozen of main genres**.

<div align="center">
<img title="Main genre clustering dendrogram" alt="Main genre clustering dendrogram" src="images/dendrogram_clusters.png" align="center">
</div>


Looking at the repartition of genres along time, **clear trends appear** like the fall of Black & White and silent movies. 

<div align="center">
<img title="Proportion of movies of given genre along time" alt="FIGURE TO ADD" src="images/genres_through_time.png" align="center">
</div>


## Creating "Eigengenres" - PCA analysis
<!-- Augustin -->
The task of reducing the number of genres can also be seen as a dimensionality reduction task, for which we have one great technique : **Principal Component Analysis**. Its idea is to project each movie onto all its genres (one-hot encoding) and then find the directions that explains the most variance of the dataset. Hence, the found directions : the so-called **eigengenres** help us define fewer dimensions to describe the movie genres while keeping most of the information.

The explained variance from a specific eigengenre can be deduced from its eigenvalue. Ranking those according to the latter value will enable us to select only the most significant eigengenres. 

<div align="center">
<img title="Explained variance" alt="Explained variance" src="images/eigengenre_explained_variance.png" align="center">
</div>

This figure shows that with only **52** eigengenres we can keep **90% of the information** contained in the dataset.

Visualizing those 52 eigengenres gives us the following plot:
<div align="center">
<img title="Eigengenres visualization" alt="Eigengenres visualization" src="images/eigengenre_visualization.png" >
</div>

If we take the third eigengenre from the left for instance, it groups genres that we would have fitted together : namely ‘silent_films’, ‘black_and_white’, and ‘short_films’. This eigengenre probably discriminates between old and new movies.

Another observation is that genres that are rarely used are not significant in established eigenvectors.



# Defining genre evolution through the career - Markov chains
<!-- Erwann -->
To delve into the dynamics of actor careers, we will try to see the trends in actors shifts in terms of genres during their career. To study that, we will use a transition matrix with a one step memory length. The goal is to be able to study if some genres are absorbent, i.e. if you start playing in these kinds of genres, you would do so during your whole career and if some are closer in a sense that you’re very likely to play them one after the other.

This approach would help actors decide on their career and forecast their potential future movie genres. If I start playing in a given genre, what would be the next genre I would play in?

## 1. Initial Genre Distribution
Initially, we plot the distribution (for each gender) of genres concerning lead roles. This unveils the initial spread across different genres.

<div align="center">
<img title="initial_distribution_genres" alt="FIGURE TO ADD" src="images/todo.png" align="center">
</div>

The distributions generally align, except in instances such as action films (Which men are relatively more likely to play) and romance films (where women are more likely to play).

## 2. Actor Transition Matrices
Moving forward, we generate transition matrices for actors, capturing the shifts between each role. The matrix outlines transitions, acknowledging the challenge of studying career shifts at a granular, one-step interval which will be discussed later.

<div align="center">
<img title="male_MC" alt="Markov transition matrix for male actors" src="images/male_MC.png" align="center">
</div>
<div align="center">
<img title="female_MC" alt="Markov transition matrix for female actors" src="images/female_MC.png" align="center">
</div>

Notably, there's a consistent high probability of remaining within the same genre. (coefficient in the diagonal). Commonly shared attractors across genders include Drama, Comedy, and Thriller genres. However, men tend to show a preference for Action, while women lean more toward romantic films.

These transition matrices also outline the closeness of genres. For example, the Drama and Thriller genres are closer than Drama and Comedy as even if the Comedy genre is more prevalent in the dataset than the Thriller genre, people would be more likely to transition from Drama to Thriller movies.

## Assessment of Averaged Matrices

   - The distributed matrices are averaged by aggregating actors' career paths within each gender group. To gauge the relevancy of these averaged matrices, we measure the distance between each actor's transition matrix and their gender's average matrix (we focus on actors who played in more than 5 movies otherwise the transition matrix is not very relevant).
   - To maintain the accuracy of calculations, we address instances where a row in an actor's transition matrix is entirely zero. In such cases, we replace these zero rows with the equivalent rows from the averaged matrix.


<div align="center">
<img title="froebius_norm" alt="Frobenius norm" src="images/frobenius_norm.png" align="center">
</div>

Using boxplots and t-tests, we observe that the Frobenius distance is significantly (p-value equals to 3e-26) higher for women compared to men. As a consequence, we can state that women who have a long career (more than 5 movies) tend to get a more unique career than their male counterparts.

Consequently, this divergence highlights fewer conventional gender transitions for women, indicating a more distinctive and atypical trajectory in their careers.


# Comparing career timelines among actors

We have a good description of the career of an actor through the transition matrix. However, this description is a summary of a career, we want now to look at the evolution of the actor through its life by looking at shifts in genres played.

## Shift time series
<!-- Romain -->
This method aims to characterize the change in genres played through a **scalar number each year the actor played**. To do that we first translate the genre obtained after the clustering for each movie into a vector of size the number of main genres and values 1 if the movie belongs to the genre, 0 otherwise. Then, for each age at which the actor played we compute the mean vector and we try to **detect shifts** in these vectors.

The scalar value used to quantify the shift is at the heart of this method. In our analysis, we use, at a given age, the films three years before and after this age to detect the shift. We compute the **mean cosine distance** between the vector of the current age studied and the vectors of the 3 previous years and to balance this value we use the **standard deviation** of the distance between the current age vector and those of the surrounding years.

This method works quite well for actors with long careers as for Brad Pitt and Sandra Bullock. 


<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width * 1.5, initial-scale=1.0">
  <title>Two Images Side by Side</title>
  <style>
    .image-container {
      display: flex;
    }

    .image-container img {
      width: 100%; /* Adjust the width as needed */
      height: auto;
    }
  </style>
</head>
<body>


<div class="image-container">
  <div>
    <div align=center>Brad Pitt</div>
    <img src="images/brad_pitt.png" alt="Image 1">
  </div>

  <div>
    <div align=center>Sandra Bullock</div>
    <img src="images/sandra_bullock.png" alt="Image 1">
  </div>
</div>

</body>
</html>


But it does not reveal any difference between men and women's career paths. Maybe the difference is not significant but it can also be due to a lack of actors with very long careers or a lack of movies in careers of the actors in our data.

<div align="center">
<img title="Genders comparison of shift trends" alt="Genders comparison of shift trends"  src="images/shift_significance_gender.png" align="center">
</div>




## Using the Levenshtein distance
<!-- Lucas -->
**TODO LUCAS**


# Conclusion
<!-- Ben -->
**TODO BEN**
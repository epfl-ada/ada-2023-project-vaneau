---
layout: post
title:  "Once upon a time..."
author: Melanie Brtan, Yehya El Hassan, Antoine Métivier, Etienne Monnin
cover:  "/assets/logo.jpg"
---

Movies have the unique ability to take us on an emotional journey and transport us to different worlds. Whether we're laughing at the antics of a comedy, rooting for the hero in an action flick, or shedding a tear at a heart-wrenching drama, the silver screen has the power to move us in ways that few other forms of entertainment can. 

The film industry is a multi-billion dollar business, with millions of people around the globe flocking to theaters each year to be entertained and touched by the magic of movies. Movies have the power to shape and reflect culture and society, and some films become cultural touchstones that leave a lasting impact on the world. No matter what genre you prefer or what kind of story you enjoy, there is a movie out there for everyone to love and cherish.

![storry telling image](/assets/story_telling.jpeg)

Have you ever been completely captivated by a movie, hanging on every twist and turn of the plot until the very end? That's the power of a well-crafted narrative. But have you ever stopped to think about the types of stories that tend to capture our attention and hold it until the credits roll? In this blog, we set out to investigate the most popular narratives in the film industry, how profitable they are, and how these storylines evolve over time.

To do this, we will examine the movie plots in the CMU Movie Corpus dataset and split them into sentences. We will then perform sentiment analysis on each sentence to construct the various movie arcs and analyze the emotions present in each film. This will allow us to see how these emotions evolve throughout the course of the movie and understand the most prevalent narrative arcs.

Join us as we delve into the world of movie storytelling and uncover the secrets of the most compelling plots. Who knows, maybe we'll even discover the formula for the perfect movie!

## Let us tell you a little story about data

The CMU Movie Summary Corpus Dataset consists of 42,306 plot summaries and its meta data from movies, released in 1893 until 2013. It varies from drama and comedy all the way to fantasy and musicals. 

{% include genres.html %}
Drama, Comedy, Thriller/Action, Romance, and Horror are the kings and queens of the genre world! No shocker there, right? These categories always come out on top and dominate the charts. They're just too darn popular to ignore! In fact this can be visualized by the following pie chart that presents the distribution of the genres present in at least 5 movies in the top 100 rated movies. 

{% include pie_distribution.html %}

We focused on analyzing four datasets of the genres; drama, comedy, thriller/action, and horror. Horror was chosen over romance because romantic movies often overlap with both drama and comedy in their genre classification. The corresponding dataset we constructed consists of:

| Genre | Dataset Size |
| --- | --- |
| Action | 2476 |
| Horror | 1273 |
| Drama | 7511|
| Comedy | 4602 |


### Movie arcs
The emotional story arc of a movie plot refers to the way the emotions of the characters and the audience change over the course of the film. It is often depicted through a character's journey as they experience a range of emotions, including happiness, sadness, anger, fear, and others.

There are many different variations on the emotional story arc, and the specific emotions that are evoked can vary widely depending on the genre and themes of the film. However, at its core, the emotional story arc is about exploring the emotional experiences of the characters and the way those emotions change and evolve over the course of the story. An American writer Kurt Vonnegut characterized the main story plots into 6 different types: 

 * **Rags to Riches** in which the protagonist rises to success 
 * **Riches to Rags** in which the protagonist falls from success
 * **Man in a Hole** in which the protagonist falls and then rises again 
 * **Icarus** in which the protagonist rises and then falls
 * **Cinderella** in which the protagonist rises, falls, and then rises again
 * **Oedipus** in which the protagonist falls, rises, and then falls again

A pretty interresting video showing Kurt Vonnegut discribing the characterizations can be found [here](https://www.youtube.com/watch?v=oP3c1h8v2ZQ&t=1s "here")

Accordingly, in our analysis, we construct the movie arcs as follows. Let us consider the following plot 

>"<span style="color:red">The film opens in 1991, with the funeral of a World War II veteran</span>. <span style="color:green">The man's daughter Marie delivers the eulogy to a church full of veterans who knew and loved her father, while her mother Ethel Ann is sitting out on the church porch, smoking and nursing a hangover </span>. <span style="color:green"> When Ethel Ann begins acting strangely, only her friend Jack  seems to understand why. It quickly emerges that there is a lot Marie does not know about her mother's past and the true story of her love life </span>. <span style="color:green"> The movie flips to a time when this mother was young, lively, and optimistic</span>. <span style="color:green"> She is in love with a young farmer, Teddy Gordon, who goes off to war with his best friends Jack, Gregory, Smith  and Chuck, but not all of them make it back alive</span>. <span style="color:green"> The plot lines intertwine with the story of a young Ulsterman in Belfast, Jimmy, who finds a ring in the wreckage of a crashed B-17 and is determined to return it to the woman who once owned it</span>. <span style="color:red"> Inadvertently caught up in cross-border troubles, Jimmy flees Belfast, travelling to Michigan to give Ethel the ring. <span style="color:orange"> Ethel reveals a wall covered in souvenirs of Teddy, which Jack and Chuck boarded up for her in 1944</span>. <span style="color:red"> Marie is shocked and furious to learn that her mother loved not Chuck, but Teddy's memory </span>. <span style="color:orange"> Ethel travels to Belfast with Jimmy</span>. <span style="color:orange">She holds the hand of a dying British soldier caught in a car-bomb attack</span>. <span style="color:green"> Quinlan  tells Ethel that he was on the hill when Teddy died, and that Teddy's dying words freed Ethel from her promise to love him forever </span>. <span style="color:green">Joining Ethel in Belfast, Jack admits that he has always loved her </span>. <span style="color:green">They begin a romance. </span>" - <span style = "color:#333">Closing the Ring, 2007.</span>

We do sentiment analysis on each line in the plot. As a result, the above plot has been marked with green meaning positive, orange neutral, and red denoting negative. The sentiment scores are saved in two formats: continuous scores and discrete classifications. The discrete class representation will be utilized to classify the type of movie, as will be detailed later. The resultant emotion arc is formed.

{% include emotional_arc.html %}

We created emotional arcs for all the movies in the dataset. The following visualization shows the emotional arcs for a randomly choosen movie in every genre.

{% include emotional_arcs_various.html %}

Visualizing the emotional arc of a single movie may not accurately represent the overall trend for a genre. To get a more accurate picture, it can be helpful to calculate the average sentiment scores for all the movies in the genre.

{% include typical_emotional_arcs_various.html %}

Did you see those plots? They are absolutely mesmerizing! I can't stop staring at them. Do you know why? 

By closely observing the typical movie arcs, we can see that the typical **Action** movie follows a **"Cinderella"** story arc, while a typical **Drama** movie falls between a **"Man in a Hole"** and **"Cinderella"** story arcs. A typical **Comedy** movie on the otherhand follows a **"Man in a Hole"** and the typical **Horror** movie follows a **"Oedipus"** story arc.

The results accurately reflect reality. To demonstrate this, let's compare them to the drama movie "Parasite," released in 2019. "Parasite" follows a poor family who initially lives peacefully but becomes intertwined with a wealthy family. As the movie progresses, increasingly dramatic events unfold, culminating in a murder by a member of the poor family. This marks the most negative point in the movie. The poor family then goes into hiding until the end of the movie, when they are finally free. This can be accurately depicted with the Drama Movie Arc! 

As humans, we crave happy endings and the results reflect this desire. All four genres, even horror, though less clearly, demonstrate an increase in score at the end of the movie. 

### A Deeper Dive into each Typical Story arc

The story arcs in different genres can vary significantly. To identify the most common arcs within a genre, we used Time series Kmeans clustering and the Tslearn Library with the soft dynamic time wrapping distance metric. After running the clustering algorithm, each movie in the genre is assigned to a cluster. By finding the barycenter of these clusters, we were able to determine the representative story arc for each cluster.

The representative story arcs for the 3 different clusters found in the Action genre are:

{% include Action_clusters.html %}


The representative story arcs for the 4 different clusters found in the Drama genre are:

{% include Drama_clusters.html %}

The representative story arcs for the 3 different clusters found in the Comedy genre are:

{% include Comedy_clusters.html %}

The representative story arcs for the 3 different clusters found in the Horror genre are:

{% include Horror_clusters.html %}

By manually examining the representative clusters, we can label each timeseries with the labels provided by Kurt Vonnegut. The clustering process resulted in a clear separation of the datapoints, with no single cluster dominating the majority of the data
 
 {% include cluster_labels_info.html %}
  
We used the tslearn library to cluster the emotional arcs of movies by genre using two different representations of time series data and the Silhouette score to evaluate the quality of the clusters and choose the optimal number of clusters. 

{% include silhoutte.html %}

According to the silhouette graph, the optimal number of clusters for action movies is 3, for drama movies is 4, for comedy movies is 3, and for horror movies is 3. Additionally, using discrete features rather than continuous features results in a higher silhouette score. Therefore, we use the resulting number of clusters and discrete features to perform timeseries clustering.

You may be wondering which cluster within each genre is the most successful in terms of profitability and IMDB rating. Let's continue uncovering the perfect recipe for a successful movie in each genre. 

### The Emotional Influence of Movies: How Does Sentiment Affect Success?
To uncover the key ingredients for a successful movie, it's important to consider whether there are higher-level features that can impact a film's success, such as the presence of emotions. What is the impact of non-emotional movies on their success compared to movies that do include emotions? Do positive or negative emotions play a particularly significant role in determining a movie's success?
  
To analyze this, we will first classify the movies. A movie can be classified as positive, neutral, or negative if over 50% of the sentences in the movie are assigned one of these sentiment values (positive +1 / neutral 0 /negative -1). We can further categorize these movies as emotional (including both positive and negative movies) or non-emotional (consisting only of neutral movies).

{% include emo_pl.html %}

As shown above, clearly more emotional movies exist in every genre. Whereas the negative movies dominate for all all genres except for Drama. Does this mean, that the demand for movies with negative sentiments is higher than for positive movies? To include the viewer’s ratings, an additional dataset from IMDb was used. So, we can compare the mean rating for emotional and non-emotional movies in every genre:

{% include bars_ratings_emo_nonemo.html %}

As well as for the ratings of positive and negative movies:

{% include bars_ratings_pn.html %}
  
It's interesting to see that drama is rated higher than the horror. Some possible reasons for why drama might be more highly rated could include:

 * Drama films often explore complex, relatable themes and emotions, which can be highly compelling for many viewers.
 * Many drama films are based on true stories or historical events, which can be highly engaging for viewers who are interested in learning more about the world around them.

On the other hand, there could be a variety of reasons why horror films are not as highly rated as drama films. Some possible reasons could include:

  * Horror films are designed to be scary and unsettling, which can be off-putting for some viewers.
  * Horror films often feature graphic violence or gore, which can be too much for some people to handle.

#### Is it possible for a film to excel without tugging at our heartstrings?
We conducted statistical tests to investigate whether the presence of emotions in a movie impacts its success, as measured by its IMDB rating. To compare the success of emotional and non-emotional movies, we conducted a matched study by pairing candidates from each group with similar runtime and absolute emotion scores. We examined the correlation between emotions and ratings for each film genre and obtained p-values to gauge the confidence level of our findings.

Unfortunately, we did not observe any significant effect, as none of the p-values were smaller than or equal to 0.05. Although there are fewer non-emotional movies compared to emotional ones, some non-emotional films have still managed to achieve success. It's possible that this is due to other factors or features besides emotion.
  
{% include em_pm.html %}

#### Okay then...! How about: positive or negative themed movies?
As we can see from the p-values, our analysis has uncovered a significant impact of emotions on movie ratings in the Action and Drama genres! Our findings indicate that negative movies in these genres tend to be rated higher than positive movies.

It is worth noting that our analysis did not reveal a correlation between emotions and ratings in the Horror and Comedy genres. This may be because the sentiment analysis we conducted, which was based on the movie plot descriptions, does not accurately reflect the emotions experienced during the movie itself. For example, the jokes in a comedy movie may not be conveyed in the plot description.

### Let's proceed! ...Let us add the Movie Arcs into our Analysis.
Movie clusters within the same genre can be evaluated by visualizing their average ratings. This can help us find the most popular and highly rated movies within a genre. Try exploring your favorite genres and see which clusters come out on top.

{% include cluster_ratings.html %}

### Ratings
  
The bar plots show that there is no clear favorite among the clusters in the Action and Horror genres. However, in the Drama and Comedy genres, there is a noticeable difference in ratings between the clusters, as indicated by the P-values displayed below. In particular, the *'Man in the Hole'* story arc (represented by cluster 3 in both genres) has the highest ratings in both the *Drama* and *Comedy genres*.

Is it any surprise that we all want to see the main character triumph over their struggles and find happiness in the end? It's what we love!

{% include most_rated_arc.html %}


### Revenue
While ratings give us an idea of a movie's critical reception, revenues provide insight into its financial performance. Based on the data we've gathered on the most common movie arcs in each genre, we want to determine which arc is most likely to predict success. To do this, we have analyzed the box office sales of each arc over time, calculating the confidence level and p-value to determine which arc has the highest sales and whether that result is statistically significant. 
  
To evaluate the profitability of the movie arcs, we divided the dataset into four periods based on the number of movies in each period, rather than the length of time. This allowed us to analyze the profitability of the arcs using a consistent sample size, even though the time periods were not of equal length.
  
A visualization of the evolution of box office revenue distribution among the various clusters of **Action** movies:
{% include Action_revenues.html %}

A visualization of the evolution of box office revenue distribution among the various clusters of **Horror** movies:
{% include Horror_revenues.html %}

 A visualization of the evolution of box office revenue distribution among the various clusters of **Drama** movies:
{% include Drama_revenues.html %}

 A visualization of the evolution of box office revenue distribution among the various clusters of **Comedy** movies:
{% include Comedy_revenues.html %}
  
The statistical test's significance value, with the null hypothesis being that all cluster distributions have the same mean, is
  {% include most_profitable_arc.html %}
 
The analysis shows that Box Office revenues have been increasing over time. This suggests that the cinema is earning more revenue across all genres. Additionally, the statistical test found that there are several clusters where the mean values differ significantly. This suggests that the revenues for different genres do not have the same mean value. Specifically, considering a signifinace level of 0.05:
  
In the **Action** genre: 
  * During period 2, the cluster labeled "Cinderella" was the more profitable than the cluster labeled "Man in the Hole". 
  * In period 3, the cluster labeled "Oedipus + Rags to Riches" competes with the cluster labeled "Cinderella," while the cluster labeled "Man in the Hole" remains much lower in profitability.
  * In periods 1 and 4, the profitability of the three clusters becomes more similar and there is no significant difference in which cluster is more profitable.

In the **Horror** genre: 
  * During Period 1 and 4, the profitability of the three clusters becomes more similar and there is no significant difference in which cluster is more profitable. On other hand, in period 2 and 3, the Oepidus movie arc is the least profitable movie arc.
  
In the **Drama** genre: 
 * During period 1, the cluster labeled "Rags to Riches" was the least profitable, while the clusters labeled "Man in the Hole" and "Oedipus + Rags to Riches" were competing for the top spot in terms of profitability.
 * During period 2 and period 3,  the profitability of the four clusters becomes more similar and there is no significant difference in which cluster is more profitable.
  * During period 4, the clusters labeled "Rags to Riches" and "Cinderella" were the least profitable, while the clusters labeled "Man in the Hole" and "Oedipus + Rags to Riches" were competing for the top spot in terms of profitability.
    
 In the **Comedy** genre: 
  * During period 3 and 4, the cluster labelled "Man in the hole" was the most profitable among all the other clusters. While in period 2, the profitability of the three clusters becomes more similar and there is no significant difference in which cluster is more profitable.

By comparing the revenue and rating results, we see that the cluster labeled "Man in the Hole" has both higher ratings and higher profitability in both the drama and comedy genres where significant differences were found compared to other clusters. This suggests that this cluster is particularly successful in these genres.
 
### Conclusion
  
This is truly a remarkable finding! By conducting sentiment analysis on every line of a movie's plot and clustering the story arcs, we were able to uncover valuable insights into the various plots present in the movie industry over a century of data. 
  
One key insight we gained is that emotions play a different role in various genres. For example, we found that negative-themed movies tend to have higher IMDB ratings compared to positive-themed movies in the genres of action and drama, while the difference was less significant in comedy and horror. We also discovered that emotional-themed movies are more common than non-emotional movies, but there was no significant difference in ratings between the two. 

Furthemore, the success of different story arcs was also varied, with some clusters achieving much greater fame and success compared to others. The cluster labeled "Man in the Hole" had higher ratings in both comedy and drama, while "Cinderella" was successful in action movies. On the other hand, the cluster labeled "Rags to Riches" had much lower fame and success in the drama genre. The oedipus narrative is the least profitable in the horror category, demonstrating that even in horror films, a happy ending is more financially beneficial. Finally, we observed that box office revenues have been increasing over time, indicating the ongoing success of movies in providing us with joy and entertainment.
  
![storry telling image](/assets/fun_meme.jpg){:height="500" width="500"}
  
In conclusion, this analysis has demonstrated the power of using data and statistical techniques to uncover trends and patterns in the movie industry. However, it is important to acknowledge the limitations of this approach. One potential weakness is that the plot summary may not capture the richness of the movie script, potentially leading to inaccurate conclusions about the story arc of various movies. Additionally, it is important to remember that hypothesis testing should not be used as a definitive tool for making conclusions, but rather as a preliminary and exploratory tool. Despite these limitations, we believe that this is what makes data science such a fascinating field – the importance of being cautious and skeptical of our findings. Needless to say, ADA rules!  
  
#### References
[1] Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

[2] https://tslearn.readthedocs.io/en/stable/

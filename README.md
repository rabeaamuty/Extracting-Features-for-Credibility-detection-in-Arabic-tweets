This work was done in order to finish my M.S thesis, which is about Credibility Detection in Arabic Tweets.

This project was done along two phases:

First Phase:
Include extracting the general (User and Content) features from Arabic tweets; We use the source code that included in Extracting-Features-From-Tweets folder in addition to use of sintement analysis by applying the code from GitHub (arabic_sentiment_analysis) which is available on https://github.com/MohamedAbdalkader/arabic_sentiment_analysis/blob/master/SA_l.py

Second phase:
We added two new features to increase the credibility detection of Arabic tweets; the two features are depending on using the google search and google translate and take the similarity scores to add them to the first features.:

1- Comparison of the similarity between "screenname" and "name" of the author: Here the "screenname" may be written in Arabic or English letters.
2 - search for the "text" of the tweet in Google After the exception of the first results -which are ads- then, looking for the ratio of similarity tweet with the first ten results and take the highest proportion and the average of the ratios of similarity to the first ten search results in Google.


The source code is applying the following processing on A data set (tweets.json) that we used which is  a set of [9,000 tweets] was collected and annotated by [El-ballouli et al. (2017): El Ballouli R, El-Hajj W, Ghandour A, Elbassuoni S, Hajj H, Shaban K (2017) CAT: Credibility Analysis of Arabic Content on Twitter. In: Proceedings of the Third Arabic Natural Language Processing Workshop, pp 62-71].

 The first file of the dataset, "tweets.json," contains 9,000 detailed tweets in the Arabic language.
 The second file, "annotation.json," contains the “tweet-id” and class for each tweet (credible or non-credible)


# Predicting Social Unrest based on live and past Tweets

## Problem Statement

The goal is to observe events with the present and historical data and predict events of social unrest and plot them on live maps using geolocation of tweets. Since the COVID era, there has
been increased interest in using social media to anticipate social
unrest. While efforts have been made toward automated unrest
prediction, we focus on filtering the vast volume of tweets to
identify tweets relevant to unrest, which can be provided to
downstream users for further analysis.

## Data

Using snscarpe module we can extract tweets based on geolocation, user and time. Based on the location input by the user we extract the tweets and run the NLP model for predicting social unrest.

## Requirement

- pip install python
- pip install folium
- pip install snscrape
- pip install pandas
- pip install opencage (download API key from: [link][https://opencagedata.com]{:hreflang="es"})
- pip install tweetnlp
- pip install numpy
- pip install matplotlib


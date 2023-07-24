# Predicting Social Unrest based on live and past Tweets
<img width="1440" alt="spark" src="https://github.com/shreysharma13/SPARK-CSD345/assets/87754709/b1087f1b-8314-4719-888c-9a457cb440df">


## Problem Statement

The goal is to observe events with the present and historical data and predict events of social unrest and plot them on live maps using geolocation of tweets. Since the COVID era, there has
been increased interest in using social media to anticipate social
unrest. While efforts have been made toward automated unrest
prediction, we focus on filtering the vast volume of tweets to
identify tweets relevant to unrest, which can be provided to
downstream users for further analysis.
<img width="827" alt="Screenshot 2022-12-10 at 10 16 28 PM" src="https://github.com/shreysharma13/SPARK-CSD345/assets/87754709/093cb237-a97b-4421-a42e-65d86c0c0234">

## Data

Using snscarpe module we can extract tweets based on geolocation, user and time. Based on the location input by the user we extract the tweets and run the NLP model for predicting social unrest.
<img width="710" alt="Screenshot 2022-11-30 at 7 16 53 PM" src="https://github.com/shreysharma13/SPARK-CSD345/assets/87754709/4938e2b2-16b9-4c1b-a756-020e122c343a">
<img width="710" alt="Screenshot 2022-11-30 at 7 16 12 PM" src="https://github.com/shreysharma13/SPARK-CSD345/assets/87754709/28c642eb-3437-45a6-9625-7d203403be2f">
<img width="1440" alt="Screenshot 2022-11-30 at 7 15 14 PM" src="https://github.com/shreysharma13/SPARK-CSD345/assets/87754709/82c99e79-e468-46c4-889d-ae9b294e1f00">

## Requirement

- pip install python
- pip install folium
- pip install snscrape
- pip install pandas
- pip install opencage (download API key from: [link][https://opencagedata.com]{:hreflang="es"})
- pip install tweetnlp
- pip install numpy
- pip install matplotlib


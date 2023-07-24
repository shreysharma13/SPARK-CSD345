import math
import snscrape.modules.twitter as sntwitter
import pandas as pd
from time import sleep
from datetime import datetime
import os
import tweetnlp
# import spacy
import folium
from folium import plugins
# # from spacy_langdetect import LanguageDetector
from folium.plugins import HeatMap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.figure(figsize=(9,10))
import altair as alt

import numpy as np
from opencage.geocoder import OpenCageGeocode
key = 'fb00964336e84e2aa9659244bb9b4e66'  # get api key from:  https://opencagedata.com
#add your own api key
# http://127.0.0.1:5000

def map_maker(keyword,from_date,to_date,region,radius):
    tweets_list2 = []
    tweets_list3 = []
    sentiment = []
    scatter = []
    model1 = tweetnlp.load('hate')
    model2 = tweetnlp.load('offensive')
    model3 = tweetnlp.load('sentiment_multilingual')
    good_ct, bad_ct = 0,0

    # geo = {"Andhra Pradesh":"15.9129, 79.7400, 200km", "Arunachal Pradesh":"28.2180, 94.7278, 200km", "Assam":"26.2006, 92.9376, 200km", "Bihar":"25.0961, 85.3131, 200km", "Chhattisgarh":"21.2787, 81.8661, 200km","Goa":"15.2993, 74.1240, 70km", "Gujarat":"22.2587, 71.1924, 150km", "Himachal Pradesh":"31.1048, 77.1734, 150km", "Haryana":"29.0588, 76.0856, 150km", "Jammu and Kashmir":"33.2778, 75.3412, 150km","Jharkhand":"23.6102, 85.2799, 150km", "Karnataka":"15.3173, 75.7139, 150km", "Kerala":"10.8505, 76.2711, 150km", "Madhya Pradesh":"22.9734, 78.6569, 150km", "Maharashtra":"19.7515, 75.7139, 150km","Manipur":"24.6637, 93.9063, 150km", "Meghalaya":"25.4670, 91.3662, 150km", "Mizoram":"23.1645, 92.9376, 150km", "Odisha":"20.9517, 85.0985, 150km","Punjab":"31.1471, 75.3412, 150km", "Rajasthan":"27.0238, 74.2179, 150km", "Sikkim":"27.5330, 88.5122, 150km", "Tamil Nadu":"11.1271, 78.6569, 150km", "Telangana":"18.1124, 79.0193, 150km","Tripura":"23.9408, 91.9882, 150km", "Uttar Pradesh":"26.8467, 80.9462, 150km", "Uttarakhand":"30.0668, 79.0193, 150km", "West Bengal":"22.9868, 87.8550, 150km","Punjab":"31.1471, 75.3412, 150km", "Andaman and Nicobar Islands":"11.7401, 92.6586, 150km", "Puducherry":"11.9416, 79.8083, 150km", "New Delhi":"28.6139, 77.2090, 100km"}
    # loc = geo[region]
    geocoder = OpenCageGeocode(key)
    query = region
    results = geocoder.geocode(query)
    lat_for_map = results[0]['geometry']['lat']
    lng_for_map = results[0]['geometry']['lng']
    print (lat_for_map, lng_for_map)
    loc = str(lat_for_map) +", "+ str(lng_for_map) + ", " + radius +"km"
    print(loc)
    print(from_date)
    print(to_date)
    lats_longs = []
    # temp = '( ' + keyword + ') geocode:' + loc + ' since:' + from_date + ' until:' + to_date
    # print(temp)
    count=0
    count_hate = 0
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('({}) geocode:"{}" since:{} until:{}'.format(keyword,loc,from_date,to_date)).get_items()):
        if count > 1000:
            break
        try :

            # print(i,tweet.content)
            # print(i,"###\n", [tweet.coordinates.latitude, tweet.coordinates.longitude])
            hate_check = model1.hate(tweet.content)
            if hate_check['label'] != 'not-hate':
                count=count+1
                count_hate +=1
                tweets_list2.append([tweet.content, tweet.coordinates.latitude, tweet.coordinates.longitude])
                lats_longs.append([tweet.coordinates.latitude, tweet.coordinates.longitude])
                print(count)
                print(tweet)
            elif model2.offensive(tweet.content)['label'] == 'offensive':
                count=count+1
                count_hate +=1
                tweets_list2.append([tweet.content, tweet.coordinates.latitude, tweet.coordinates.longitude])
                lats_longs.append([tweet.coordinates.latitude, tweet.coordinates.longitude])
                print(count)
                print(tweet)
            temp = model3.sentiment(tweet.content)
            if temp['label'] == 'negative':
                tweets_list2.append([tweet.content, tweet.coordinates.latitude, tweet.coordinates.longitude])
                lats_longs.append([tweet.coordinates.latitude, tweet.coordinates.longitude])
                # sentiment.append(-temp['probability'])
                count+=1
                print(count)
                print(tweet)
                bad_ct +=1
            else:
                # sentiment.append(temp['probability'])
                good_ct +=1
                print("tweet not found negative")
            scatter.append([hate_check['probability'], temp['probability']])
        except AttributeError:
            print("discard tweet , had no attributes")
    print("**************",count_hate)
    #tweets_df2 = pd.DataFrame(tweets_list2, columns=['Text', 'Latitide','Longitude'])
    tweets_df3 = pd.DataFrame(tweets_list2, columns=['Text', 'Latitude','Longitude'])
    #tweets_df2.to_csv("twitter data_hate_offensive.csv",index=False)
    tweets_df3.to_csv("twitter data_bad.csv",index=False)
    tweets_df4 = pd.DataFrame(sentiment, columns=['sentiment'])
    tweets_df4.to_csv("twitter sentiment.csv")

    # print(lats_longs)
    # map1 = folium.Map(location = [lat_for_map, lng_for_map], zoom_start = 5)
    #
    # map2 = folium.Map(location = [lat_for_map, lng_for_map], tiles="Stamen Watercolor", width="%100", height="%100",zoom_start=5)
    # # map2 = folium.Map(location = [28.7041, 77.1025], tiles="cartodbdark_matter", width="%100", height="%100",zoom_start=5)
    # map3 = folium.Map(location = [lat_for_map, lng_for_map], tiles="cartodbdark_matter", width="%100", height="%100",zoom_start=5)
    # folium.raster_layers.TileLayer('CartoDB Positron').add_to(map3)
    # folium.LayerControl().add_to(map3)
    # minimap = plugins.MiniMap(toggle_display=True)
    # map3.add_child(minimap)


    dt = {}
    data = {}
    for l in lats_longs:
        hash = math.sqrt(l[0]**2 + l[1]**2)
        data[hash] = l
        if hash in dt:
            dt[hash] +=1
        else:
            dt[hash] = 1

    unrest = folium.Map(location=[lat_for_map, lng_for_map], tiles='cartodbdark_matter', zoom_start = 5)

    # folium.Marker(
    #     location=[lat_for_map, lng_for_map],
    #     popup= region,
    #     icon=folium.Icon(color='red', icon='info-sign')
    # ).add_to(unrest)

    source = pd.read_csv("twitter data_bad.csv")
    base = alt.Chart(source).mark_line().encode(
        alt.X("Latitude", axis=alt.Axis(title="Latitude")),
        alt.Y("Longitude", axis=alt.Axis(title="Longitude"))
    )
    vega = folium.features.VegaLite(base, width="%100",height="%100")
    graph_popup = folium.Popup()
    vega.add_to(graph_popup)

    tooltip = "Click Me!!!"
    folium.Marker(title = "Region:- " + str(region),location=[lat_for_map, lng_for_map], popup=graph_popup, tooltip=tooltip).add_to(unrest)

    plugins.Fullscreen(
        position='topleft',
        title='Expand me',
        title_cancel='Exit me',
        force_separate_button=True
    ).add_to(unrest)


    fg = folium.FeatureGroup(name='Incidents of Social unrest')
    unrest.add_child(fg)

    g1 = plugins.FeatureGroupSubGroup(fg, 'HeatMap')
    unrest.add_child(g1)

    g2 = plugins.FeatureGroupSubGroup(fg, 'Overlap')
    unrest.add_child(g2)

    g3 = plugins.FeatureGroupSubGroup(fg, 'Area')
    unrest.add_child(g3)
    print(lats_longs)
    for i in range(len(lats_longs)):
        folium.CircleMarker(location=[lats_longs[i][0], lats_longs[i][1]],radius=3, fill=True,opacity=0.1,fill_opacity=0.25,fill_color="blue",color="green").add_to(g2)
    for i in dt:
        print(data[i], dt[i])
        if dt[i]> 20:
            folium.CircleMarker(location=data[i],radius=2 + 5,fill=True,opacity=0.5,fill_opacity=0.6,fill_color="blue",color="green").add_to(g3)
        else:
            folium.CircleMarker(location=data[i],radius=2 + dt[i]/5,fill=True,opacity=0.5,fill_opacity=0.6,fill_color="blue",color="green").add_to(g3)

    folium.LayerControl(collapsed=False).add_to(unrest)

    HeatMap(lats_longs).add_to(g1)
    unrest.save("templates/map1.html")
    # unrest.save("templates/map2.html")
    # unrest.save("templates/map3.html")

    # map1.save("templates/map1.html")
    # map2.save("templates/map2.html")
    # map3.save("templates/map3.html")
    print("!!!!!")

    y = np.array([good_ct, bad_ct])
    plt.clf()
    plt.pie(y)
    plt.legend(y)
    plt.savefig("/Users/shreysharma/Desktop/coding/Flask_practice/virtualenv_csd345/static/images/graph1.png")
    plt.clf()
    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True

    for tweet in scatter:
        x = tweet[0]
        y = tweet[1]
        plt.plot(x, y, marker = "o")
        plt.xlabel("Probability of negative")
        plt.ylabel("Ptobability of hate or offensive")

    plt.savefig("/Users/shreysharma/Desktop/coding/Flask_practice/virtualenv_csd345/static/images/graph2.png")
    plt.clf()
    time = np.arange(len(lats_longs))
    one = []
    sec = []

    for i in range(len(lats_longs)):
        one.append(lats_longs[i][0])
    for i in range(len(lats_longs)):
        sec.append(lats_longs[i][1])
    income = np.array(one)
    expenses = np.array(sec)
    fig, ax = plt.subplots(figsize=(9, 10))

# Plot lines
    ax.plot(time, income, color="green")
    ax.plot(time, expenses, color="red")

    # Fill area when income > expenses with green
    ax.fill_between(
        time, income, expenses, where=(income > expenses),
        interpolate=True, color="green", alpha=0.25,
        label="Positive"
    )

    # Fill area when income <= expenses with red
    ax.fill_between(
        time, income, expenses, where=(income <= expenses),
        interpolate=True, color="red", alpha=0.25,
        label="Negative"
    )
    plt.savefig("/Users/shreysharma/Desktop/coding/Flask_practice/virtualenv_csd345/static/images/graph3.png")
    plt.clf()






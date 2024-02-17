# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:42:05 2020

@author: Ridhima
"""

import pandas as pd
import matplotlib.pyplot as plt
import nltk
import numpy as np
import tweepy 

pd.options.display.max_columns = 50
pd.options.display.max_rows= 50
pd.options.display.width= 120
 
consumer_key = '2CF0SjF91irHA3xzSRJwhMiJF'
consumer_secret = 'ERNMd3a05M39IZgK1B8C6VeIfFauFMxvfY17LxiTD9omlNha0K'
access_token = '908720407682875393-DkzbECIw8z6Alp3axpLgv3njJ1zcjAU'
access_secret = 'ZMcWhoSNdYFUwT8aItpYrIg95cGJgYD2zfjerxhqfsstu'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
# Extract 50 tweets based on the keyword
results = []
i=0
for tweet in tweepy.Cursor(api.search, q='Taiz', lang="en").items():
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        results.append(tweet)
        id = tweet.id
        i=i+1
        if i==50:
            break
print (len(results))

# Store the tweets in a dataframe
def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])

    # Processing Tweet Data

    data_set["text"] = [tweet.text for tweet in results] #text of tweet
    data_set["created_at"] = [tweet.created_at for tweet in results] #when the tweet was created
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results] #number of retweets
    data_set["favorite_count"] = [tweet.favorite_count for tweet in results] #number of favourites
    data_set["source"] = [tweet.source for tweet in results] #source of the tweet
    data_set["length"] = [len(tweet.text) for tweet in results] #number of characters in tweet

    # Processing User Data
    data_set["user_id"] = [tweet.author.id for tweet in results] #id of the author
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results] 
    data_set["user_name"] = [tweet.author.name for tweet in results]
    data_set["user_created_at"] = [tweet.author.created_at for tweet in results] #age of user account
    data_set["user_description"] = [tweet.author.description for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results] #number of followers
    data_set["user_friends_count"] = [tweet.author.friends_count for tweet in results] #number of friends
    data_set["user_location"] = [tweet.author.location for tweet in results] #user has a location in profile?
    data_set["user_statuses_count"] = [tweet.author.statuses_count for tweet in results] #number of statuses
    data_set["user_verified"] = [tweet.author.verified for tweet in results] #user is verified?
    data_set["user_url"] = [tweet.author.url for tweet in results] #user has a URL?


    

    return data_set
data_set = process_results(results)

#df=pd.read_csv("D://HillaryClintonTweets.csv")
data_set["number_of_QuestionMarks"] = ""
data_set["user_has_url?"] = ""
data_set["user_has_url?"] = np.where(data_set["user_url"].isnull(), 'No', 'Yes')
data_set.to_csv("D://FinalDataset.csv", index=False, encoding='utf-8')
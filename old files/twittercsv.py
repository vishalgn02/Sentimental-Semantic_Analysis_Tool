import csv
import json
import re
import tweepy
import sys
from tweepy import OAuthHandler

consumer_key = "D4QJKs6I6hJxtG77GHnGdqgUa"
consumer_secret = "bpRgmsEh5mVk6TebWOWqDOvJH563wPyTiuBD0dPBF5jxI8F9WE"
access_key = "1130180130767159301-itoWmjWPPH1qoLDXCYy101u1Y5XFrM"
access_secret = "i4HYUcKFq8G8MLqI4qWJGKx44iQI5kwkeVpKc5UE5EQQc"
parameters = ["created_at", "text", "location", "retweeted", "retweet_count"]
#writing the required parameters unto csv file
with open("file1.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(parameters)


def cleaning(string):
    #removing url
    text = [re.sub(r'^https?:\/\/.*[\r\n]*', ' ', k, flags=re.MULTILINE) for k in string.split(" ")]
    text = " ".join(text)
    #removing smileys
    text2 = [k.encode('ascii', 'ignore').decode('ascii') for k in text.split(" ")]
    text2 = " ".join(text2)
    #removing special tags
    text3 = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in text2.split(" ")]
    text3 = " ".join(text3)
    return text3


def tweet(keyword):
    lead = tweepy.OAuthHandler(consumer_key, consumer_secret)
    lead.set_access_token(access_key, access_secret)
    #wait function to wait beacuse twitter wont give tweets at a timw
    api = tweepy.API(lead, wait_on_rate_limit=True)
    tweets = tweepy.Cursor(api.search, q=keyword).items(3050)
    for line in tweets:
        list = []
        #sending the data to cleaning and storing them in a list
        param1 = cleaning(line._json["created_at"])
        param2 = cleaning(line._json["text"])
        param3 = cleaning(line._json["user"]["location"])
        list.append(param1)
        list.append(param2)
        list.append(param3)
        list.append(line._json["retweeted"])
        list.append(line._json["retweet_count"])
        print(line._json)
        with open("file1.csv", "a", newline='', encoding="utf-8-sig") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(list)


tweet("Canada OR University OR Dalhousie University OR Halifax OR Canada Education")


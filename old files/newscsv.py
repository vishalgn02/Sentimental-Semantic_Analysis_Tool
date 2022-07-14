import json
import re
import csv

from newsapi import NewsApiClient

parameters = ["author", "title", "description", "content"]
with open("file2.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(parameters)

# can write single function for cleaning but to reduce for loop for single word I have written two functions
def cleaning_para(string):
    #removing url from  sentence
    text = [re.sub(r'^https?:\/\/.*[\r\n]*', ' ', i, flags=re.MULTILINE) for i in string.split(" ")]
    text = " ".join(text)
    #removing smillies from sentence
    text2 = [i.encode('ascii', 'ignore').decode('ascii') for i in text.split(" ")]
    text2 = " ".join(text2)
    #removing specials tags from sentence
    text3 = [re.sub(r"[^a-zA-Z0-9]+", ' ', i) for i in text2.split(" ")]
    text3 = " ".join(text3)
    return text3


def cleaning_single(string):
    #removing url from word
    text = re.sub(r'^https?:\/\/.*[\r\n]*', ' ', string, flags=re.MULTILINE)
    #removing smilies from word
    text2 = text.encode('ascii', 'ignore').decode('ascii')
    #removing special tags from word
    text3 = re.sub(r"[^a-zA-Z0-9]+", ' ', text2)
    return text3


def new(keyword):
    # print(keyword)
    newsapi = NewsApiClient(api_key='e5780fb8ee6d4782bd8d54c48f9e3012')
    all_articles = newsapi.get_everything(q=keyword,
                                          language='en',
                                          sort_by='popularity')

    # print(all_articles["articles"])
    for line in all_articles["articles"]:
        list = []
        #certains authors values are none so sending them for cleaning is useless
        if (line["author"] != None):
            param1 = cleaning_single(line["author"])
        else:
            param1 = None
        param2 = cleaning_para(line["title"])
        param3 = cleaning_para(line["description"])
        if (line["content"] != None):
            param4 = cleaning_para(line["content"])
        else:
            param4 = None
        list.append(param1)
        list.append(param2)
        list.append(param3)
        list.append(param4)
        with open("file2.csv", "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(list)


new("Canada")
new("University")
new("Dalhousie University")
new("Halifax")
new("Canada Education")
new("Moncton")
new("Toronto")

import json
import csv
import requests
import re
movie_url = "http://www.omdbapi.com/?apikey=37b44c7e"
def cleaning_special_tags(data):
    text = [re.sub(r"[^a-zA-Z0-9]+", '', str(k)) for k in data]
    return  text



def movies(keyword):
    #creating a flag to write key values only for one time in the csv
    if(keyword == "Canada"):
        count = 0
    else:
        count =1
    for i in range(1,50):
      response = requests.get(url=movie_url, params={"s": keyword,"page":i})
      if("Search" in response.json().keys()):
        print(response.json())
        search = response.json()["Search"]
        #for each movie taking id and passing it to get whole data of the movie
        for line in search:
           response1 = requests.get(url=movie_url, params={"i": line["imdbID"]})
           values= response1.json().values()
           keys = response1.json().keys()
           values = cleaning_special_tags(list(values))

           with open("file_movies.csv", "a", encoding="utf-8-sig",newline='') as file:
               csv_writer = csv.writer(file)
               if(count == 0):
                   csv_writer.writerow(list(keys))
                   count= 1
               csv_writer.writerow(values)



movies("Canada")
movies("University")
movies("Moncton")
movies("Halifax")
movies("Toronto")
movies("Vancouver")
movies("Alberta")
movies("Niagara")

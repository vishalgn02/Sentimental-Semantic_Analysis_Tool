import math
import  os
import csv
import mmap
#creating directory for storing files
os.makedirs("directory")
#intializing keywords count
canada = 0
University = 0
Dalhousie = 0
halifax = 0
business = 0

#reading files which contains the cleaned data of news
with open("news.csv", "r",encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    count = 0
    for line in csv_reader:
        count = count+1
        filename = "file"+str(count)
        #creating files and storing data
        with open(os.path.join("directory",filename), "a", newline='') as csv_file:
            mylist = []
            mylist.append(line["title"])
            mylist.append(line["description"])
            mylist.append(line["content"])
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(mylist)
for file in os.listdir("directory"):
    #print(file)
    with open(os.path.join("directory",file), "r", encoding='utf-8-sig') as file:

        for line in file:
            while ("," in line):
                line = line.replace(",", " ")
            #print(line)
            if "Canada" in line:
                canada = canada+1
            if "University" in line:
                University = University+1
            if "Dalhousie University" in line:
                Dalhousie = Dalhousie+1
            if "Halifax" in line:
                halifax = halifax+1
            if "business" in line:
                business = business +1

#creating table1
with open("table1.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Total documents","700"])
    parameters = ["Search query","Document containg the term(df)","N/df","log(N/df)"]
    csv_writer.writerow(parameters)
    canada_parameter = ["Canada",canada,round(700/canada,2), round(math.log(700/canada,10),2)]
    csv_writer.writerow(canada_parameter)
    university_parameter = ["university",University,round(700/University,2),round(math.log(700/University,10),2)]
    csv_writer.writerow(university_parameter)
    dalhousie_parameter = ["Dalhousie University",Dalhousie,round(700/Dalhousie,2),round(math.log(700/Dalhousie,10),2)]
    csv_writer.writerow(dalhousie_parameter)
    halifax_parameter = ["Halifax",halifax,round(700/halifax,2),round(math.log(700/halifax,10),2)]
    csv_writer.writerow(halifax_parameter)
    business_parameter = ["business",business,round(700/business,2),round(math.log(700/business,10),2)]
    csv_writer.writerow(business_parameter)
#creating table 2
with open("table2.csv", "a", newline='') as csv_file:
     csv_writer = csv.writer(csv_file)
     csv_writer.writerow(["Term","Canada"])
     parameters = ["Document Name","total words(m)","frequency(f)"]
     csv_writer.writerow(parameters)
     frequency = 0
     required_filename = ""
     highest_canada_count = 0
     highest_count_filename = ""
     for file in os.listdir("directory"):
          canada_count = 0
          ylist = []
          ylist.append(file)
          with open(os.path.join("directory",file), "r", encoding='utf-8-sig') as file:
               for line in file:
                  while ("," in line):
                       line = line.replace(",", " ")
                  list1 = line.split(" ")
                  #removing empty words
                  while("" in list1):
                    list1.remove("")
                  ylist.append(len(list1))
                  #counting frequency
                  while("Canada" in list1):
                      canada_count = canada_count +1
                      list1.remove("Canada")
                  if(highest_canada_count<canada_count):
                      highest_canada_count = canada_count
                      highest_count_filename = ylist[0]
                  ylist.append(canada_count)
                  if(canada_count != 0):
                      csv_writer.writerow(ylist)
                      frequency_dummy = round(ylist[2]/ylist[1],2)
                      if(frequency<frequency_dummy):
                          frequency = frequency_dummy
                          required_filename = ylist[0]
     print("The highest frequency is:",highest_canada_count,"It is contained in the file:",highest_count_filename)
     print("The highest relative frequency is:",frequency,"It is contained in the file:",required_filename)


import csv
positive = []
negative = []
#writing parameters in file1
parameters = ["Tweet","message","Match","polarity"]
with open("file1.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(parameters)
#writing parameters in file2
parameters_2 = ["Tweet","Match","word polarity"]
with open("file2.csv", "a", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(parameters_2)
# reading positive and negative words into list
with open("words.csv", "r",encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        if line["Positive"] != "":positive.append(line["Positive"])
        if line["Negative"] != "":negative.append(line["Negative"])
#taking tweet data
with open("tweet_data_1.csv", "r",encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    count = 0
    for line in csv_reader:
        final_list = []
        final_list_2 = []
        count = count+1
        final_list.append(count)
        final_list_2.append(count)
        final_list.append(line["Tweet"])
        #print(line["Tweet"])
        line = line["Tweet"].split(" ")
        dict1 = {}
        #creating bag of words
        for word in line:
            word = word.lower()
            if word in dict1:
                dict1[word] = dict1[word]+1
            else:
                dict1[word] = 1
        matchpostive = {}
        matchnegative = {}
        print(dict1)
        #matching bag of words with positive and negative
        for word in dict1:

            if word in positive:
                matchpostive.update({word:dict1[word]})
            if word in negative:
                matchnegative.update({word:dict1[word]})
        #print(matchpostive)
        #print(matchnegative)
        #creating list of postive and negative words for each tweet
        required_positive = []
        required_negative = []
        for i in matchpostive:
            for j in range(matchpostive[i]):
                required_positive.append(i)
        for i in matchnegative:
            for j in range(matchnegative[i]):
                required_negative.append(i)
        matchpostive_count = 0
        matchnegative_count = 0
        for i in list(matchpostive.values()):
            matchpostive_count = matchpostive_count+i
        for i in list(matchnegative.values()):
            matchnegative_count = matchnegative_count+i
        #writing list into the file based upon positive and negative words
        with open("file1.csv", "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if(matchpostive_count>matchnegative_count):
                word = ''
                for i in matchpostive:
                    word = word+", "+i
                for i in matchnegative:
                    word = word +", "+ i
                final_list.append(word[1:].strip())
                final_list.append("positive")
                csv_writer.writerow(final_list)
            elif(matchnegative_count>matchpostive_count):
                word = ''
                for i in matchpostive:
                    word = word+", "+i
                for i in matchnegative:
                    word = word +", "+ i
                final_list.append(word[1:].strip())
                final_list.append("negative")
                csv_writer.writerow(final_list)
            else:
                word = ''
                for i in matchpostive:
                    word = word + ", " + i
                for i in matchnegative:
                    word = word + ", " + i
                final_list.append(word[1:].strip())
                final_list.append("neutral")
                csv_writer.writerow(final_list)
        #writing list of words and their polarity
        with open("file2.csv", "a", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for i in required_positive:
                final_list_2.append(i)
                final_list_2.append("positive")
                csv_writer.writerow(final_list_2)
                final_list_2.remove(i)
                final_list_2.remove("positive")
            for i in required_negative:
                final_list_2.append(i)
                final_list_2.append("negative")
                csv_writer.writerow(final_list_2)
                final_list_2.remove(i)
                final_list_2.remove("negative")



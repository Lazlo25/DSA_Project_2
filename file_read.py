import pandas as pd

setval = pd.read_csv('dataset.csv')

word_list = setval.values.tolist()
words = []
for x in word_list:
    words.extend(x)


data = []
for x in range (0,len(words),21):
    dict = {"artist" : words[x+2], "album" : words[x+3], "song":words[x+4], "popularity": words[x+5]}
    data.append(dict)

#print(data[0])
#print(data[1])



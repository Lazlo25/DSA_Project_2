import time
import plotly.graph_objects as show
import bucket_sort
import merge_sort
import pandas as pd

from merge_sort import merge_sort_iterative

#organizing the dataset
setval = pd.read_csv('dataset.csv')

word_list = setval.values.tolist()
words = []
for x in word_list:
    words.extend(x)


data = []
for x in range (0,len(words),21):
    dict = {"artist" : words[x+2], "album" : words[x+3], "song":words[x+4], "popularity": words[x+5]}
    data.append(dict)


#actually displaying the data
m_arr = data.copy()
b_arr = data.copy()

#measureing the sorting times

start = time.time()
#merge_sort_iterative(m_arr)
merge_time = time.time() - start

start = time.time()
#bucket_sort(b_arr)
bucket_time = time.time() - start


#display
algorithms = ['Merge Sort', 'Bucket Sort']
times = [merge_time, bucket_time]

fig = show.Figure(data=[show.Bar(x=algorithms, y=times)])

fig.update_layout(
    title="Sorting Performance Comparison",
    xaxis_title="Algorithm",
    yaxis_title="Time (seconds)"
)

fig.show()
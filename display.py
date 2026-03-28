import time
import plotly.graph_objects as go
from bucket_sort import bucket_sort
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
    temp = {"artist" : words[x+2], "album" : words[x+3], "song":words[x+4], "popularity": words[x+5]}
    data.append(temp)


#actually displaying the data
m_arr = data.copy()
b_arr = data.copy()

#measureing the sorting times

start = time.time()
m_return = merge_sort_iterative(m_arr, "popularity")
merge_time = time.time() - start
m_result = pd.DataFrame(m_return)
m_result.to_csv('merge_result')

start = time.time()
b_return = bucket_sort(b_arr, "popularity")
bucket_time = time.time() - start
b_result = pd.DataFrame(b_return)
b_result.to_csv('bucket_result')


#display
algorithms = ['Merge Sort', 'Bucket Sort']
times = [merge_time, bucket_time]

fig = go.Figure(data=[go.Bar(x=algorithms, y=times)])

fig.update_layout(
    title="Sorting Performance Comparison",
    xaxis_title="Algorithm",
    yaxis_title="Time (seconds)"
)

fig.show()


# def make_table(input, title):
#     return show.Table(
#         header=dict(values=["Artist", "Album", "Song","Popularity"]),
#         cells=dict(values=[
#             [d['artist'] for d in input],
#             [d['album'] for d in input],
#             [d['song'] for d in input],
#             [d['popularity'] for d in input]
#         ]),
#         name=title
#     )
#
# fig = show.Figure(data=[
#     make_table(data, "Original"),
# ])
#
# fig.update_layout(title="Before Sorting")
# fig.show()
#
# fig2 = show.Figure(data=[
#     make_table(m_arr, "Merge Sort"),
# ])
#
# fig2.update_layout(title="After Merge Sort")
# fig2.show()
#
# fig.show()
# Source: https://github.com/EML4U/Clustering/blob/1bebd2e9febec60245cc2ef66a5324b9dcd9497e/amazon_movie_sorter.py
# Author: https://github.com/Slothologist
#
# Reads movies.txt.gz
# Sorts data by date
# Stores as pickle
# - list of keys: helpfulness, score, time, number
# - list of texts (concatenated fields summary and text)

import os
import pickle
from datetime import datetime
import yaml
from classes.amazon_reviews_reader import AmazonReviewsReader
import time

amazon_gz_file    = "data/movies/movies.txt.gz"
amazon_raw_file = "data/clustering/amazon_raw.pickle"
max_docs        = -1  # -1 for all

text_list = []
key_list = []
ident = []

timeBegin = time.time()
print("Begin", time.asctime())
print("Reading", amazon_gz_file)

for item in AmazonReviewsReader(amazon_gz_file, "fields", max_docs=max_docs):
    ident.append(item['helpfulness'])
    ident.append(int(float(item['score']))-1)  # change rating to better conform to classifier required format
    ident.append(datetime.fromtimestamp(int(item['time'])))
    ident.append(item['number'])
    key_list.append(ident)
    ident = []
    text_list.append((item['summary'] + " " + item['text']).replace('<br />', ' '))

text_list, key_list = (list(t) for t in zip(*sorted(zip(text_list, key_list), key=lambda x: x[1][-2])))

# add internal id
internal_id = 0
for key in key_list:
    key.append(internal_id)
    internal_id += 1
    
print("Writing", amazon_raw_file)
with open(amazon_raw_file, 'wb') as handle:
    pickle.dump((text_list, key_list), handle)

print("Runtime (secs)", time.time()-timeBegin)

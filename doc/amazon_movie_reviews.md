# Explaining Drift in Text Data with Document Embeddings

## Amazon movie reviews

### Reading data

Use the file [amazon_pickle_reader.py](../access/amazon_pickle_reader.py).

To create an instance, specify the directory containing prepared pickle files.
The instance will store data read from pickle files in memory.
The pickle files will be read on first data access, not when creating the instance.

```python
data = AmazonPickleReader('/tmp/directory-with-pickle-files/')

```

#### Accessing texts

Texts are available for the IDs [0, 7911683].

```python
print('first text: ', data.get_text(0)[:100])       # 100 characters of first text
print('last text:  ', data.get_text(-1)[:100])      # 100 characters of last text
print('last text:  ', data.get_text(7911683)[:100]) # 100 characters of last text

# first text:  The everyday man at war &quot;The Cruel Sea&quot; gives an excellent account of the real war at sea,
# last text:   Little darlings looking I saw this movie when I was in high school and loved Tatum O'neal and Kristy
# last text:   Little darlings looking I saw this movie when I was in high school and loved Tatum O'neal and Kristy
```

Regarding to the original file, the texts are taken from the fields 'summary' and 'text',
see [code](https://github.com/EML4U/ExplainingDriftTextEmbeddings/blob/a9d833ba28fb46959901d081b44338f3c8499ec9/data/amazon_movie_sorter.py#L36).

#### Accessing BoW50 embeddings (Bag of Words with 50 dimensions)

Texts are available for the IDs [84090, 7911683], as the first 3 years are not included.

```python
print('first bow50: ', data.get_bow50(84090)[:5],   '...') # 5 numbers of first bow50
print('last bow50:  ', data.get_bow50(7911683)[:5], '...') # 5 numbers of last bow50

# first bow50:  [-0.24985783  0.16864878  0.02703895 -0.11902861 -0.12623635] ...
# last bow50:   [-0.0483431  -0.698007    0.29450932  0.3002716   0.35189843] ...
```

Be aware that the same texts do not result in the same embeddings.
But they are more similar.

```python
from sklearn.metrics.pairwise import pairwise_distances
sameA1 = 84107
sameA2 = 84119
print('sameA1 text:  ', data.get_text(sameA1)[:100])
print('sameA2 text:  ', data.get_text(sameA2)[:100])
print('sameA1 bow50: ', data.get_bow50(sameA1)[:5])
print('sameA2 bow50: ', data.get_bow50(sameA2)[:5])

# sameA1 text:   Might have been profound for it's time but... When I pay almost 30. for a DVD I expect alot, especia
# sameA2 text:   Might have been profound for it's time but... When I pay almost 30. for a DVD I expect alot, especia
# sameA1 bow50:  [-0.02514367 -0.29414916  0.40210924 -0.09406912 -0.51019126]
# sameA2 bow50:  [ 0.04848728 -0.2670002   0.3912263  -0.07553244 -0.46337175]
    
sameB1 = 84201
sameB2 = 84206
print('sameB1 text:  ', data.get_text(sameB1)[:100])
print('sameB2 text:  ', data.get_text(sameB2)[:100])
print('sameB1 bow50: ', data.get_bow50(sameB1)[:5])
print('sameB2 bow50: ', data.get_bow50(sameB2)[:5])

# sameB1 text:   Must not be ignored &quot;Salo&quot; is one of the most controversial and debatable films of the cen
# sameB2 text:   Must not be ignored &quot;Salo&quot; is one of the most controversial and debatable films of the cen
# sameB1 bow50:  [ 0.6617752   0.4826813   0.21395582 -0.2834527   0.05723236]
# sameB2 bow50:  [ 0.7021096   0.38454628  0.20149517 -0.29684734  0.05091358]
    
print('distance sameA1 sameA2', pairwise_distances([data.get_bow50(sameA1)], [data.get_bow50(sameA2)]))
print('distance sameB1 sameB2', pairwise_distances([data.get_bow50(sameB1)], [data.get_bow50(sameB2)]))
print('distance sameA1 sameB1', pairwise_distances([data.get_bow50(sameA1)], [data.get_bow50(sameB1)]))
print('distance sameA2 sameB2', pairwise_distances([data.get_bow50(sameA2)], [data.get_bow50(sameB2)]))

# distance sameA1 sameA2 [[0.28922]]
# distance sameB1 sameB2 [[0.3078685]]
# distance sameA1 sameB1 [[3.7674677]]
# distance sameA2 sameB2 [[3.812414]]
```

#### Accessing metadata

Metadata is available for both, text (raw) and bow50.
Equal IDs result in equal metadata.

```python
print('metadata first text:  ', data.get_text(0,      metadata=True))
print('metadata text  84090: ', data.get_text(84090,  metadata=True))
print('metadata bow50 84090: ', data.get_bow50(84090, metadata=True))
print('metadata last text:   ', data.get_text(-1,     metadata=True))

# metadata first text:   ['2/2', 4, datetime.datetime(1997, 8, 20, 2, 0), 2381344, 0]
# metadata text  84090:  ['2/3', 3, datetime.datetime(2000, 1, 1, 1, 0), 1771, 84090]
# metadata bow50 84090:  ['2/3', 3, datetime.datetime(2000, 1, 1, 1, 0), 1771, 84090]
# metadata last text:    ['0/0', 3, datetime.datetime(2012, 10, 25, 2, 0), 7908990, 7911683]
```

The metadata keys are:

- [0] helpfulness
- [1] score [0, 4] (corresponding to [1, 5] stars)
- [2] date
- [3] entry number in original file from stanford.edu
- [4] id

The keys were created in [amazon_movie_sorter.py](https://github.com/EML4U/ExplainingDriftTextEmbeddings/blob/a9d833ba28fb46959901d081b44338f3c8499ec9/data/amazon_movie_sorter.py#L30).

### Generation of embeddings

The embeddings were generated using:

- [../transformation/amazon_movie_sorter.py](../transformation/amazon_movie_sorter.py)
    - uses `amazon_reviews_reader.py`
    - writes `amazon_raw.pickle`
- [../transformation/amazon_reviews_reader.py](../transformation/amazon_reviews_reader.py)
    - reads movies.txt.gz (original file)
- [../transformation/generator_amazon_movie_embeddings.py](../transformation/generator_amazon_movie_embeddings.py)
    - reads `amazon_raw.pickle`
    - uses `doc_to_vec.py`
    - writes `amazon_bow_50.pickle`
- [../transformation/doc_to_vec.py](../transformation/doc_to_vec.py)
    - uses model(s) available at [FTP](https://hobbitdata.informatik.uni-leipzig.de/EML4U/2021-05-17-Amazon-Doc2Vec/)

### Source data

The original data can be downloaded here:

- [https://snap.stanford.edu/data/web-Movies.html](https://snap.stanford.edu/data/web-Movies.html)
- [https://snap.stanford.edu/data/movies.txt.gz](https://snap.stanford.edu/data/movies.txt.gz)

### Data insights

![](images/amazon_movie_reviews-overview.svg)

[Image source](https://github.com/EML4U/Drift-detector-comparison/tree/main/figures/amazon-overview)
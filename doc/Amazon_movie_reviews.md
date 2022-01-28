# Explaining Drift in Text Data with Document Embeddings

## Amazon movie reviews

### Embeddings

The embeddings were generated using:

- [../data/amazon_movie_sorter.py](../data/amazon_movie_sorter.py) writes `amazon_raw.pickle`, uses `amazon_reviews_reader.py`
- [../data/amazon_reviews_reader.py](../data/amazon_reviews_reader.py)
- [../data/generator_amazon_movie_embeddings.py](../data/generator_amazon_movie_embeddings.py) reads `amazon_raw.pickle`, writes `amazon_bow_50.pickle`

### Source data

The original data can be downloaded here:

- [https://snap.stanford.edu/data/web-Movies.html](https://snap.stanford.edu/data/web-Movies.html)
- [https://snap.stanford.edu/data/movies.txt.gz](https://snap.stanford.edu/data/movies.txt.gz)
# Explaining Drift in Text Data with Document Embeddings

## Amazon movie reviews

### Generation of embeddings

The embeddings were generated using:

- [../data/amazon_movie_sorter.py](../data/amazon_movie_sorter.py)
    - uses `amazon_reviews_reader.py`
    - writes `amazon_raw.pickle`
- [../data/amazon_reviews_reader.py](../data/amazon_reviews_reader.py)
    - reads movies.txt.gz (original file)
- [../data/generator_amazon_movie_embeddings.py](../data/generator_amazon_movie_embeddings.py)
    - reads `amazon_raw.pickle`
    - uses `doc_to_vec.py`
    - writes `amazon_bow_50.pickle`
- [../data/doc_to_vec.py](../data/doc_to_vec.py)
    - uses model(s) available at [FTP](https://hobbitdata.informatik.uni-leipzig.de/EML4U/2021-05-17-Amazon-Doc2Vec/)

### Source data

The original data can be downloaded here:

- [https://snap.stanford.edu/data/web-Movies.html](https://snap.stanford.edu/data/web-Movies.html)
- [https://snap.stanford.edu/data/movies.txt.gz](https://snap.stanford.edu/data/movies.txt.gz)

### Data insights

![](images/amazon_movie_reviews-overview.svg)

[Image source](https://github.com/EML4U/Drift-detector-comparison/tree/main/figures/amazon-overview)
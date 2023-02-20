# Explaining Drift in Text Data with Document Embeddings

This repository provides a software pipeline in order to explain drift between two sets of documents using embeddings.

First experiments indicate that [BERT document embeddings](experiments/dev_pipeline-bert.ipynb) outperform [Doc2Vec document embeddings](experiments/dev_pipeline-doc2vec.ipynb).

## Documentation

- How to configure [file storage](doc/notebooks/file_storage.ipynb) and the default directory to read data
- Amazon movie reviews
    - [Data overview](doc/amazon_movie_reviews.md)
    - How to read with [Amazon Pickle_Reader](doc/notebooks/amazon_pickle_reader.ipynb) and access texts, embeddings, metadata
    - How to read with [Amazon Pickle_Splitter](doc/notebooks/amazon_pickle_splitter.ipynb) and get items, which are equally splitted 
    - Data is currently stored at [Google Drive](https://drive.google.com/drive/folders/1NdfbAkH-YRpHul4uwsIN3_O5T_VQmGY1)
- How to [store interim results](doc/notebooks/interim_storage.ipynb)
- How to [reduce dimensions](doc/notebooks/reduction.ipynb)
- How to create [Wordclouds](doc/notebooks/wordcloud.ipynb)

## Developer Information

- Goal: Reusable, complete and documented code (good for developers, reviewers, everyone)
- If you add new classes, please provide minimal code examples, put them into the `doc` directory and add a link above.
- Directories
    - `doc`: Documentation (e.g. how to read data)
    - `experiments` Jupyter notebooks (e.g. combine class instances into a process generating explanations)
    - `transformation`: Classes for data transformation (e.g. create embeddings, reduce dimensions)
    - `access`: Classes for data access (e.g. read or split embeddings)
    - `explanations`: Classes for the explanation process (e.g. handling ml models, generate explanations)
    - `scripts`: Small sets of commands (e.g. to synchronize repositories)
- How to name your code: [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)

## Acknowledgments

This  work  has  been  supported  by  the  German  FederalMinistry of Education and Research (BMBF) within the project [EML4U](https://eml4u.github.io/) under the grant no 01IS19080B.
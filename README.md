# Explaining Drift in Text Data with Document Embeddings

## Documentation

- Data: Currently stored at [Google Drive](https://drive.google.com/drive/folders/1NdfbAkH-YRpHul4uwsIN3_O5T_VQmGY1)
- Data access
- How to access [Amazon movie reviews](doc/amazon_movie_reviews.md)
- How to get [Amazon movie reviews](doc/notebooks/amazon_pickle_splitter.ipynb) items, which are equally splitted 
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

This  work  has  been  supported  by  the  German  FederalMinistry of Education and Research (BMBF) within the project [EML4U](https://eml4u.github.io/) under the grant no 01IS19080 A and B.

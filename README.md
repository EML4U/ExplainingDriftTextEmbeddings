# Explaining Drift in Text Data with Document Embeddings

## Documentation

- Data: Currently stored at [Google Drive](https://drive.google.com/drive/folders/1NdfbAkH-YRpHul4uwsIN3_O5T_VQmGY1)
- How to access [Amazon movie reviews](doc/amazon_movie_reviews.md)
- How to [reduce dimensions](doc/notebooks/reduction.ipynb)
- How to create [Wordclouds](doc/notebooks/wordcloud.ipynb)

## Developer Information

- Goal: Reusable, complete and documented code (good for developers, reviewers, everyone)
- If you add new classes, please provide minimal code examples, put them into the `doc` directory and add a link above.
- Directories
    - `data`: Classes for data access and generation (e.g. create, modify, read embeddings)
    - `doc`: Documentation (e.g. how to read data)
    - `explanations`: Classes for the explanation process (e.g. handling ml models, generate explanations)
    - `notebooks` User interface (e.g. combine class instances into a process generating explanations)
    - `scripts`: Small sets of commands (e.g. to synchronize repositories)
- How to name your code: [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)

## Acknowledgments

This  work  has  been  supported  by  the  German  FederalMinistry of Education and Research (BMBF) within the project [EML4U](https://eml4u.github.io/) under the grant no 01IS19080 A and B.

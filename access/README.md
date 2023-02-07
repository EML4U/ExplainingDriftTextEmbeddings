# File overview

## Readers

- **reader_interface.py**  
  Interface for readers to implement
- **amazon_doc2vec_reader.py**  
  Implements the reader interface for Amazon Doc2Vec tests
- **amore_doc2vec_reader.py**  
  Implements the reader interface for AMORE Doc2Vec

## Utilities

- **amazon_pickle_reader.py**  
  Reader for Amazon pickle files containing texts and Doc2Vec embeddings
- **amore_reader.py**  
  Reader for AMORE benchmark text files
- **file_storage.py**  
  Files locations for reusage
- **interim_storage.py**  
  Methods to write and load interim results

# Data structure

- Each **dataset** contains two distributions.
- Each **distribution** has an ID and contains a set of items.
- Each **item**:
    - has an ID.
    - is available as **text**.
    - has least one **embedding** vector.
from .reader_interface import ReaderInterface
from .amazon_pickle_reader import AmazonPickleReader
from .amore_reader import AmoreReader
import pickle

class AmoreDoctovecReader(ReaderInterface):
    """
    Reads Amazon Movie Reviews texts and Doc2Vec embeddings.
    Note: Years 1997 to 1999 are not included in the embeddings.
    Data is available at: https://hobbitdata.informatik.uni-leipzig.de/EML4U/2022-02-05-DriftExplanationPaper/
    Distribution IDs file is available at: https://hobbitdata.informatik.uni-leipzig.de/EML4U/2022-06-09-AMORE-Tests/
    """
    
    def __init__(self):
        self.data = None
    
    def initialize(self, options):
        """
        Options:
        'data_directory': Directory containing the files amazon_raw.pickle and amazon_bow_50.pickle.
        'amore_directory': Directory containing text files of AMORE benchmark.
        'amore_benchmark_id': ID of AMORE benchmark, e.g. '1'.
        """
        self.amore_directory = options['amore_directory']
        self.amore_benchmark_id = options['amore_benchmark_id']
        self.amazon_pickle_reader = AmazonPickleReader(options['data_directory'])
        print('AMORE directory:                   ', self.amore_directory)
        print('AMORE benchmark ID:                ', self.amore_benchmark_id)
        print('AmoreDoctovecReader data directory:', options['data_directory'])
    
    def get_distribution_ids(self):
        """
        Returns a list of available distribution IDs.
        Convention: Distribution IDs should be integers starting at 0.
        """
        return list(self.load_data().keys())
    
    def get_item_ids(self, distribution_id):
        """Returns a list of item IDs for a given distribution ID."""
        return self.load_data()[distribution_id]
    
    def get_text(self, dataset_id):
        """Returns the text for the given item ID."""
        raw_id = self.amazon_pickle_reader.get_raw_id(dataset_id)
        return self.amazon_pickle_reader.get_text(raw_id)

    def get_embeddings(self, dataset_id):
        """Returns an embeddings vector for the given item ID."""
        raw_id = self.amazon_pickle_reader.get_raw_id(dataset_id)
        return self.amazon_pickle_reader.get_bow50(raw_id)

    def get_dimensions(self):
        """Returns the number of embeddings dimensions"""
        return len(self.get_embeddings(self.get_item_ids(self.get_distribution_ids()[0])[0]))
    
    def load_data(self):
        """Loads data and caches in a dictionary distributionID-to-itemID"""
        if(self.data is None):
            print('Loading embeddngs')
            self.data = {}
            reader = AmoreReader(self.amore_directory)
            self.data[0] = reader.get_set_a_ids(self.amore_benchmark_id)
            self.data[1] = reader.get_set_b_ids(self.amore_benchmark_id)
        return self.data
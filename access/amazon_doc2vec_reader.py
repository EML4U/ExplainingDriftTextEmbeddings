from .reader_interface import ReaderInterface
from .amazon_pickle_reader import AmazonPickleReader
import pickle

class AmoreDoctovecReader(ReaderInterface):
    """
    Reads Amazon Movie Reviews texts and Doc2Vec embeddings.
    Note: Years 1997 to 1999 are not included in the embeddings.
    Data is available at: https://hobbitdata.informatik.uni-leipzig.de/EML4U/2022-02-05-DriftExplanationPaper/
    Distribution IDs file is available at: https://hobbitdata.informatik.uni-leipzig.de/EML4U/2022-06-09-AMORE-Tests/
    """
    
    def __init__(self):
        self.distribution_ids = None
    
    def initialize(self, options):
        """
        Options:
        'data_directory': Directory containing the files amazon_raw.pickle and amazon_bow_50.pickle.
        'distributions_file': File containing the file amore_test_1.pickle.
        """
        self.distributions_file = options['distributions_file']
        self.amazon_pickle_reader = AmazonPickleReader(options['data_directory'])
        print('AmoreDoctovecReader distributions file:', self.distributions_file)
        print('AmoreDoctovecReader data directory:    ', options['data_directory'])
    
    def get_distribution_ids(self):
        """
        Returns a list of available distribution IDs.
        Convention: Distribution IDs should be integers starting at 0.
        """
        return list(self.get_distributions().keys())
    
    def get_item_ids(self, distribution_id):
        """Returns a list of item IDs for a given distribution ID."""
        return self.get_distributions()[distribution_id]
    
    def get_text(self, dataset_id):
        """Returns the text for the given item ID."""
        raw_id = self.amazon_pickle_reader.get_raw_id(dataset_id)
        return self.amazon_pickle_reader.get_text(raw_id)

    def get_embeddings(self, dataset_id):
        """Returns an embeddings vector for the given item ID."""
        raw_id = self.amazon_pickle_reader.get_raw_id(dataset_id)
        return self.amazon_pickle_reader.get_bow50(raw_id)
    
    def get_distributions(self):
        """Loads and caches distribution IDs"""
        if(self.distribution_ids is None):
            print('AmoreDoctovecReader: Loading distribution file:', self.distributions_file)
            with open(self.distributions_file, "rb") as f:
                self.distribution_ids = pickle.load(f)
        return self.distribution_ids
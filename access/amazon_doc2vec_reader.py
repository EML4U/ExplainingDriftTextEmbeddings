class AmoreDoctovecReader(ReaderInterface):
    """
    Reads Amazon Movie Reviews texts and Doc2Vec embeddings.
    Data is available at: https://hobbitdata.informatik.uni-leipzig.de/EML4U/2022-02-05-DriftExplanationPaper/
    """
    
    def initialize(self, options):
        """
        Options:
        'data_directory': Directory containing the files amazon_raw.pickle and amazon_bow_50.pickle.
        'distributions_file': File containing the file amore_test_1.pickle.
        """
        self.amazon_pickle_reader = AmazonPickleReader(options['data_directory'])
        pass
    
    def get_distribution_ids(self):
        """Returns a list of available distribution IDs."""
        pass
    
    def get_dataset_ids(self, distribution_id):
        """Returns a list of dataset IDs for a given distribution ID."""
        pass

    def get_text(self, distribution_id, dataset_id):
        """Returns the text for the given IDs."""
        pass

    def get_embeddings(self, distribution_id, dataset_id):
        """Returns an embeddings vector for given IDs."""
        pass
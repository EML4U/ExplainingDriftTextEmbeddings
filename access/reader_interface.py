class ReaderInterface:
    """
    Common methods to access data.
    To use different types of embeddings, implement this interface multiple times in individual classes.
    Please document how data can be accessed, e.g. a FTP URL.
    """
    
    def initialize(self, options):
        """
        Initializes reader with options in dictionary.
        
        Options:
        'key': description
        """
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
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
        """
        Returns a list of available distribution IDs.
        Convention: Distribution IDs should be integers starting at 0.
        """
        pass
    
    def get_item_ids(self, distribution_id):
        """Returns a list of item IDs for a given distribution ID."""
        pass

    def get_text(self, item_id):
        """Returns the text for the given dataset ID."""
        pass

    def get_embeddings(self, item_id):
        """Returns an embeddings vector for the given dataset ID."""
        pass

    def get_dimensions(self):
        """Returns the number of embeddings dimensions."""
        pass
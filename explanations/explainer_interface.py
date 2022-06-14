class ExplainerInterface:
    """
    Common methods to explain drift.
    """
    
    def initialize(self, options):
        """
        Initializes reader with options in dictionary.
        
        Options:
        'key': description
        """
        pass
    
    def get_token_list(self, dist_a, dist_b, item_ids_a, item_ids_b, reader):
        """
        Compares items of distribution A with items of distribution B.
        Returns a dictionary of words and scores for tokens.
        """
        pass
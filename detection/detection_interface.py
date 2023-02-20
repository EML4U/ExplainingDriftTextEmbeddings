class DetectionInterface:
    """
    Common methods to select data.
    """
    
    def initialize(self, options):
        """
        Initializes selection with options in dictionary.
        
        Options:
        'key': description
        """
        pass
    
    def set_reader(self):
        """
        Sets a ReaderInterface implementation to access data.
        """
        pass
    
    def select_item_ids(self, distribution_a_id, distribution_b_id):
        """Detects and returns a list of dataset IDs of distribution B."""
        pass
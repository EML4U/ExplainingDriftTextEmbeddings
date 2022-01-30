# Reader for preprocessed Amazon movie reviews.
# Reads pickle files and holds data in memory.
#
# The preprocessed data was sorted by time and rounded by hour [1], resulting in new identifiers "raw_id".
# The BoW-50 data does not contain 84,090 entries, mainly (by rounding) from reviews between 1997 and 1999.
# Author: https://github.com/adibaba
#
# Example:
# data = AmazonPickleReader('/tmp/')
# print(data.get_text(84090))
# print(data.get_bow50(84090))
# print(data.get_text(84090, metadata=True))
# print(data.get_bow50(84090, metadata=True))
#
# Metadata keys:
# [0] helpfulness
# [1] score [0, 4] (corresponding to [1, 5] stars)
# [2] date
# [3] entry number in original file from stanford.edu
# [4] id

import pickle

class AmazonPickleReader:
    
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.filename_raw   = 'amazon_raw.pickle'
        self.filename_bow50 = 'amazon_bow_50.pickle'
        self.data_raw   = None
        self.data_bow50 = None

    def set_filename_raw(filename):
        self.filename_raw = filename
        
    def set_filename_bow_50(filename):
        self.filename_bow50 = filename
        
    def get_all_raw(self):
        if(self.data_raw is None):
            with open(self.data_directory + self.filename_raw, 'rb') as handle:
                self.data_raw = pickle.load(handle)
        return self.data_raw
    
    def get_all_bow50(self):
        if(self.data_bow50 is None):
            with open(self.data_directory + self.filename_bow50, 'rb') as handle:
                self.data_bow50 = pickle.load(handle)
        return self.data_bow50

    def get_text(self, raw_id, metadata=False):
        if metadata:
            return self.get_all_raw()[1][raw_id]
        else:
            return self.get_all_raw()[0][raw_id]
    
    def get_bow50(self, raw_id, metadata=False):
        # 1997 to 1999 not included
        bow50_id = raw_id - 84090
        if(bow50_id < 0):
            raise IndexError('list index out of range: ' + str(raw_id))
        if metadata:
            return self.get_all_bow50()["data"][1][bow50_id]
        else:
            return self.get_all_bow50()["data"][0][bow50_id]

# Reader which gets the same number of indexes for every year-star combination
# Author: https://github.com/adibaba

from .amazon_pickle_reader import AmazonPickleReader

class AmazonPickleSplitter(AmazonPickleReader):
    
    def __init__(self, data_directory):
        super().__init__(data_directory)

    def get_data_splits(self, years=None, stars=None, max_items=-1):
        
        # Initialize settings
        if(years is None):
            years = [year for year in range(1997, 2012+1)] 
        if(stars is None):
            stars = [star for star in range(0, 4+1)] 

        # Initialize results
        results = {}
        for year in years:
            results[year] = {}
            for star in stars:
                results[year][star] = []

        # Get IDs
        for item in super().get_all_raw()[1]:
            score = item[AmazonPickleSplitter.META_SCORE]
            year  = item[AmazonPickleSplitter.META_DATE].year
            id_   = item[AmazonPickleSplitter.META_ID]

            if(year not in years):
                continue
            if(score not in stars):
                continue
            if(len(results[year][score]) >= max_items and max_items!=-1):
                continue

            results[year][score].append(id_)

        return results
    
    def print_overview(self):

        results = {}
        years = [year for year in range(1997, 2012+1)] 
        stars = [star for star in range(0, 4+1)] 
        for year in years:
            results[year] = {}
            for star in stars:
                results[year][star] = 0
                
        for item in super().get_all_raw()[1]:
            score = item[AmazonPickleSplitter.META_SCORE]
            year  = item[AmazonPickleSplitter.META_DATE].year
            id_   = item[AmazonPickleSplitter.META_ID]
            results[year][score] += 1
        
        for year in years:
            print(str(year) + '\t', end='')
        print()
        for star in stars:
            for year in years:
                print(str(results[year][star]) + '\t', end='')
            print(str(star))
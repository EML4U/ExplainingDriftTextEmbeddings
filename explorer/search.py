import re

class Search:
    
    def initialize(self, options):
        """
        Initializes reader with options in dictionary.
        
        Options:
        'reader': reader implementation to access data
        """
        self.reader = options['reader']
    
    def search(self, query, item_ids=None, max=-1):
        results = {}
        i = 0
        for item_id in item_ids:
            if re.findall(query, self.reader.get_text(item_id)):
                results[item_id] = self.reader.get_text(item_id)
                max -= 1
            
            i += 1
            if max == 0:
                break
                
        print('Searched in', i, 'items')
        print('Found', len(results), 'items (' + str(round(100*len(results)/i, 2)), '%)')
        return results
            
    def print_results(self, results, max=-1):
        for result in results.items():
            print(result[0], result[1], '\n')
            max -= 1
            if max == 0:
                break
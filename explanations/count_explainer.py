from .explainer_interface import ExplainerInterface
from collections import Counter
from gensim.utils import simple_preprocess
from wordcloud import STOPWORDS

class CountExplainer(ExplainerInterface):
    """
    Explainer based on counted tokens.
    """
    
    def initialize(self, options):
        """
        Initializes reader with options in dictionary.
        
        Options:
        'max_results': Number of max results to be retruned by get_token_dict
        """
        self.max_results = options['max_results']
        print('CountExplainer max_results:', self.max_results)
    
    
    def get_token_dict(self, item_ids_a, item_ids_b, reader):
        """
        Compares items of distribution A with items of distribution B.
        Returns a dictionary of words and scores for tokens.
        """
        
        # Collect texts
        texts_a = []
        for item_id in item_ids_a:
            texts_a.append(reader.get_text(item_id))
        texts_b = []
        for item_id in item_ids_b:
            texts_b.append(reader.get_text(item_id))

        # Get tokens from texts
        tokens_a = self.get_tokens(texts_a)
        tokens_b = self.get_tokens(texts_b)
        
        # Remove tokens which occur often in both distributions
        tokens = self.remove_tokens(tokens_a, tokens_b)
        
        # Sort by value
        sorted_tuples = sorted(tokens.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}
        
        # Return top values
        max_items = self.max_results
        token_weights = {}
        for item in sorted_dict.items():
            token_weights[item[0]] = item[1]
            max_items -= 1
            if(max_items == 0):
                break
        return token_weights
        
    
    # https://radimrehurek.com/gensim/utils.html#gensim.utils.simple_preprocess
    def get_tokens(self, texts, stopwords=STOPWORDS, min_len=2, max_len=15):
        tokens = []
        for text in texts:
            tokens += simple_preprocess(text, min_len=min_len, max_len=max_len)
        tokens = [w for w in tokens if w not in stopwords]
        return Counter(tokens)

    
    def remove_tokens(self, counter, counter_remove, factor=2):
        dict_ = {}
        for token in counter.keys():
            if(token in counter_remove):
                if(counter[token] >= counter_remove[token] * factor):
                    dict_[token] = counter[token]
        return Counter(dict_)
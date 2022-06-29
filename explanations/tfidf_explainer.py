from .explainer_interface import ExplainerInterface
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import _stop_words

class TfidfExplainer(ExplainerInterface):
    """
    Common methods to explain drift.
    See: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
    See: https://scikit-learn.org/stable/modules/feature_extraction.html
    See: https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a
    See: https://developpaper.com/instructions-for-using-python-scipy-sparse-matrix/
    """
    
    def initialize(self, options):
        """
        Initializes reader with options in dictionary.
        
        Options:
        'max_results': Number of max results to be retruned by get_token_dict
        """
        self.max_results = options['max_results']
        print('TfidfExplainer max_results:', self.max_results)
    
    
    def get_token_dict(self, item_ids_a, item_ids_b, reader):
        """
        Compares items of distribution A with items of distribution B.
        Returns a dictionary of words and scores for tokens.
        """
        
        # Collect item texts
        items_a = []
        for item_id in item_ids_a:
            items_a.append(reader.get_text(item_id))
        items_b = []
        for item_id in item_ids_b:
            items_b.append(reader.get_text(item_id))
        
        # TF-IDF
        vectorizer = TfidfVectorizer(stop_words=_stop_words.ENGLISH_STOP_WORDS)
        fit = vectorizer.fit(items_a + items_b)
        feature_names = vectorizer.get_feature_names()
        
        # Weighted TF-IDF values
        doc_term_matrix_a = vectorizer.transform(items_a)
        doc_term_matrix_b = vectorizer.transform(items_b)
        tokens_scores_a = self.get_weighted_tokens(doc_term_matrix_a, len(feature_names))
        tokens_scores_b = self.get_weighted_tokens(doc_term_matrix_b, len(feature_names))
        
        # Compare
        compared = {}
        for item_a in tokens_scores_a.items():
            compared[item_a[0]] = item_a[1] - tokens_scores_b.get(item_a[0], 0)
        
        # Sort by TF-IDF values
        sorted_tuples = sorted(compared.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = {k: v for k, v in sorted_tuples}

        # Token IDs to tokens, limit by given maximum
        max_items = self.max_results
        token_weights = {}
        for item in sorted_dict.items():
            token_weights[feature_names[item[0]]] = item[1]
            max_items -= 1
            if(max_items == 0):
                break
        
        return token_weights
    
    def get_weighted_tokens(self, doc_term_matrix, tokens_size):
        c = doc_term_matrix.tocoo()

        # Sum up TF-IDF values of single tokens in doc-term-matrix (cluster of docs)
        counter_tokens = {}
        counter_itidf  = {}
        for i in range(len(c.data)):
            token_index = c.col[i]
            tfidf_value = c.data[i]
            #counter_tokens[token_index] = counter_tokens.get(token_index, 0) + 1
            counter_itidf[token_index]  = counter_itidf.get(token_index, 0) + tfidf_value

        # TODO: Dividing every result by the same number makes no sense; does not change overall result -> modify
        results = {}
        for token_index in counter_itidf:
            # Bad solution:
            # Mean could be improved to reflect in how many docs a token appears (TODO)
            #results[token_index] = counter_itidf[token_index] / counter_tokens[token_index]
            
            results[token_index] = counter_itidf[token_index] / tokens_size
        
        return results
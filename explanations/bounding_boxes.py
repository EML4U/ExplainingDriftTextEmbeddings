import numpy as np

class BoundingBoxes:
    
    def __init__(self):
        self.dimension_values = []
        self.min_ = []
        self.max_ = []
    
    # All in one
    def execute(embeddings_dict, percentile):
        for embedding in embeddings_dict.values:
            self.add_embedding(embedding)
        self.update_boundaries(percentile)
        dimensions = {}
        for embedding in embeddings_dict.items:
            dimensions[emdedding[0]] = self.get_number_of_enclosed_dimensions(embedding[1])
        return dimensions

    # (1) Collect values of single dimensions/indexes of embeddings.
    def add_embedding(self, embedding):
        # Create data structure
        if not self.dimension_values:
            for i in embedding:
                self.dimension_values.append([])
        # Collect values of single dimensions
        for i in range(len(embedding)):
            self.dimension_values[i].append(embedding[i])

    # (2) Use values of single dimensions to calculate min/max.
    #     Regions can be shrinked by percentiles.
    def update_boundaries(self, percentile):
        self.min_ = []
        self.max_ = []
        for index, value in enumerate(self.dimension_values):
            q1, q3 = np.percentile(value, [percentile, 100-percentile])
            self.min_.append(q1)
            self.max_.append(q3)

    # (3) A counter which is incremented, if an embedding value of another(!) 
    # distribution is inside the previously calculated boundaries.
    def get_number_of_enclosed_dimensions(self, embedding):
        included = 0
        for index, value in enumerate(embedding):
            if(value >= self.min_[index] and value <= self.max_[index]):
                included += 1
        return included
    
    def get_min(self):
        return self.min_
    
    def get_max(self):
        return self.max_
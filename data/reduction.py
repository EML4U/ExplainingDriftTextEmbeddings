# This class provides basic methods to transform embedding dimensions.
# The used components (sklearn/umap) provide more extensive configurations.
# If you require additional settings, please consider to not use this class instead of editing it.
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap.umap_ as umap_
import timeit

class Reduction:
    
    # https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
    def pca_fit(self, fit_data, dimensions=2, print_time=False):
        time_begin = timeit.default_timer()
        self.pca_instance = PCA(n_components=dimensions)
        self.pca_instance.fit(fit_data)
        if(print_time):
            print('PCA fit seconds:', timeit.default_timer() - time_begin)
    
    def pca_transform(self, transform_data, print_time=False):
        time_begin = timeit.default_timer()
        result = self.pca_instance.transform(transform_data)
        if(print_time):
            print('PCA seconds:', timeit.default_timer() - time_begin)
        return result

    
    # https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
    def tsne_fit(self, fit_data, dimensions=2, print_time=False):
        time_begin = timeit.default_timer()
        self.tsne_instance = TSNE(n_components=dimensions)
        self.tsne_instance.fit(fit_data)
        if(print_time):
            print('t-SNE fit seconds:', timeit.default_timer() - time_begin)
    
    def tsne_transform(self, transform_data, dimensions=2, print_time=False):
        time_begin = timeit.default_timer()
        result = self.tsne_instance.fit_transform(transform_data)
        if(print_time):
            print('t-SNE transform seconds:', timeit.default_timer() - time_begin)
        return result
    
    
    # https://umap-learn.readthedocs.io/en/latest/api.html#umap.umap_.UMAP.fit_transform
    def umap_fit(self, fit_data, dimensions=2, print_time=False):
        time_begin = timeit.default_timer()
        self.umap_instance = umap_.UMAP(n_components=dimensions)
        self.umap_instance.fit(fit_data)
        if(print_time):
            print('UMAP fit seconds:', timeit.default_timer() - time_begin)
    
    def umap_transform(self, transform_data, print_time=False):
        time_begin = timeit.default_timer()
        result = self.umap_instance.transform(transform_data)
        if(print_time):
            print('UMAP seconds:', timeit.default_timer() - time_begin)
        return result
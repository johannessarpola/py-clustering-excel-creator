from typing import List


class Identified(object):
    id = ''

    def __init__(self, id):
        self.id = id

    def asDict(self):
        d = {}
        d['id'] = self.id
        return d


class InputCluster(Identified):
    categories = {}

    def __init__(self, id, categories):
        super().__init__(id)
        self.categories = categories


class InputClustering(Identified):
    clusters = []
    silhouette = 0.0

    def __init__(self, id, clusters, silhouette, original_silhouette, purity_score, running_time_ms):
        super().__init__(id)
        self.clusters = clusters
        self.silhouette = silhouette
        self.original_silhouette = original_silhouette
        self.purity_score = purity_score
        self.running_time_ms = running_time_ms

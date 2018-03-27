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

    def __init__(self, id, clusters, silhouette):
        super().__init__(id)
        self.clusters = clusters
        self.silhouette = silhouette

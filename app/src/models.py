class Identified(object):
    id = ''

    def __init__(self, id):
        self.id = id

    def asDict(self):
        d = {}
        d['id'] = self.id
        return d


class InputClustering(Identified):
    clusters = []

    def __init__(self, id, clusters):
        super().__init__(id)
        self.clusters = clusters


class InputCluster(Identified):
    categories = {}

    def __init__(self, id, categories):
        super().__init__(id)
        self.categories = categories

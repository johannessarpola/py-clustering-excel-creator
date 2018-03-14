
class ClusteringResult(object):
    id = ""
    clusters = []

    def __init__(self, id, clusters) -> None:
        self.id = id
        self.clusters = clusters

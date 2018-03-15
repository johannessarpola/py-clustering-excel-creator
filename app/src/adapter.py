from src import models
from typing import List

def json_to_clustering_result(json) -> models.InputClustering:
    id = json["id"]
    clusters = list(map(lambda e: json_to_cluster(e), json["clusters"]))
    return models.InputClustering(id, clusters)


def json_to_cluster(json) -> models.InputCluster:
    id = json["id"]
    categories = json["categories"]
    return models.InputCluster(id, categories)


def multiple_results_from_json(json) -> List[models.InputClustering]:
    crs = list(map(lambda obj: json_to_clustering_result(obj), json))
    return crs


def results_to_excel(results):
    print("not done")

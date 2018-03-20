from app.src import models
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
    """
    Takes in multiple json files which contain InputClustering-type data
    :param json:
    :return:
    """
    all_crs = []
    for res_obj in json:
        o = list(map(lambda obj: json_to_clustering_result(obj), res_obj))
        all_crs.append(o)
    return all_crs

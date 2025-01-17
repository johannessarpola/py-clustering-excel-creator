from app.src import models
from typing import List


def json_to_clustering_result(json) -> models.InputClustering:
    id = json["id"]
    silhouette = json["silhouette"]
    original_silhoutte = json["original_silhouette"]
    purity_score = json["purity_score"]
    running_time_ms = json["running_time (ms)"]
    clusters = list(map(lambda e: json_to_cluster(e), json["clusters"]))
    return models.InputClustering(id, clusters, silhouette, original_silhoutte, purity_score, running_time_ms)


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
        o.sort(key=lambda x: x.id)
        all_crs.append(o)
    return all_crs

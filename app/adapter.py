import json
from . import models

def json_to_result(json):
    id = json["id"]
    content = json["clusters"]
    return models.ClusteringResult(id, content)

def multiple_results_from_json(json):
    results = list(map(lambda obj: json_to_result(obj), json))
    return results

def results_to_excel(results):
    print("not done")

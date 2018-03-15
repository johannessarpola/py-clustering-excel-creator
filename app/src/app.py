import os
import json
import multiprocessing as mp
from app.src import input_output as io
from app.src import adapter


def relative_resource(path):
    dir = os.path.dirname(__file__)
    res = os.path.join(dir, "resources")
    actual_path = os.path.join(res, path)
    return actual_path


def main():
    jsons = io.get_jsons_from_folder('.data/')
    all_crs = adapter.multiple_results_from_json(jsons)
    for crs in all_crs:
        # todo
        adapter.append_results_to_excel(crs, None)
    print("app")


if __name__ == '__main__':
    main()
    print("done!")

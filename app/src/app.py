import os
import json
import multiprocessing as mp
from app.src import input_output as io
from app.src import adapter
from app.src import excel_output as out

def relative_resource(path):
    dir = os.path.dirname(__file__)
    res = os.path.join(dir, "resources")
    actual_path = os.path.join(res, path)
    return actual_path

def main():
    jsons = io.get_jsons_from_folder('.data/')
    all_crs = adapter.multiple_results_from_json(jsons)
    fd = out.FormattingData(1, 3, 1)
    out.multiple_results_to_excels(fd, all_crs)
    print("app")


if __name__ == '__main__':
    main()
    print("done!")

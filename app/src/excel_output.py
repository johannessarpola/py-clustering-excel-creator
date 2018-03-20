from app.src import models
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet import Worksheet
from datetime import datetime
from typing import List

def extract_category_titles_from_cluster(cl):
    category_titles = set(cl.clusters[0].categories)
    return category_titles


class FormattingData(object):
    start_column = 0
    start_row = 0
    padding = 0

    def __init__(self, start_column,
                 start_row,
                 padding):
        self.start_column = start_column
        self.start_row = start_row
        self.padding = padding


def multiple_results_to_excels(base_fd: FormattingData, results):
    """

    :param base_fd: FormattingData
    :param results: List of clustering results from multiple files
    :return:
    """
    wb = Workbook()
    ws = wb.create_sheet("Result", 0)
    col_cursor = base_fd.start_column
    for result in results:
        fd = FormattingData(col_cursor, base_fd.start_row, base_fd.padding)
        (cc, rc) = add_results_to_excel(fd, result, ws)
        col_cursor += cc # This just increases to column by 4 for each iteration
    wb.save("filename.xlsx")


def add_results_to_excel(fd: FormattingData,
                         cls: List[models.InputClustering],
                         ws: Worksheet):
    """
    Appends results to workbook with current time as suffix
    :param cls: list of models.InputClustering
    :param workbook:
    :return:
    """

    category_titles = set()

    row_cursor = fd.start_row
    col_cursor = 0
    for cl in cls:
        col_cursor = fd.start_column
        cluster_id = cl.id

        # get the category titles
        if len(category_titles) == 0:
            category_titles = extract_category_titles_from_cluster(cl)

        header_pass = True
        for cluster in cl.clusters:
            k = 0
            if header_pass:
                ws.cell(row=row_cursor, column=col_cursor, value=cluster_id)
                col_cursor += 1
                for cat_title in category_titles:
                    ws.cell(row=row_cursor, column=col_cursor + k, value=cat_title)
                    k += 1
                row_cursor += 1

            k = 0
            for cat in category_titles:
                cat_count = cluster.categories[cat]
                ws.cell(row=row_cursor, column=col_cursor + k, value=cat_count)
                k += 1

            row_cursor += 1
            header_pass = False
        row_cursor += fd.padding
    col_cursor += len(category_titles)
    return col_cursor, row_cursor
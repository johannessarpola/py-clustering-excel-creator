from typing import List

from openpyxl import Workbook
from openpyxl.worksheet import Worksheet

import os

from app.src import excel_formatting_utils as formatting
from app.src.excel_formatting_utils import Direction
from app.src import models


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


def multiple_results_to_excels(base_fd: FormattingData, results, filename=None):
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
        col_cursor = cc  # This just increases to column by 4 for each iteration

    par_dir = os.path.dirname(filename)
    if not os.path.exists(par_dir):
        os.makedirs(par_dir)
    if filename is not None:
        return wb.save(f"{filename}")
    return wb.save(f"results.xlsx")


def write_cluster_result_stats(fd: FormattingData, cl: models.InputClustering, ws: Worksheet, row_cursor):
    # Write stats
    # Reset column cursor
    col_cursor = fd.start_column
    row_cursor += 1
    first_cell = ws.cell(row=row_cursor, column=col_cursor, value="silhouette")
    formatting.add_border_to_row(ws, first_cell.row, Direction.TOP, formatting.borders.BORDER_DASHED)
    ws.cell(row=row_cursor, column=col_cursor + 1, value=round(cl.silhouette, 4))
    row_cursor += 1
    ws.cell(row=row_cursor, column=col_cursor, value="org. silhouette (sample)")
    ws.cell(row=row_cursor, column=col_cursor + 1, value=round(cl.original_silhouette, 4))
    row_cursor += 1
    ws.cell(row=row_cursor, column=col_cursor, value="purity score")
    ws.cell(row=row_cursor, column=col_cursor + 1, value=round(cl.purity_score, 3))
    row_cursor += 1
    ws.cell(row=row_cursor, column=col_cursor, value="running_time (ms)")
    ws.cell(row=row_cursor, column=col_cursor + 1, value=round(cl.running_time_ms, 2))

    return row_cursor + 1


def write_cluster_labels(cl: models.InputClustering, ws: Worksheet, row_start, target_col):
    row_cursor = row_start
    for clus in cl.clusters:
        cell = ws.cell(row=row_cursor, column=target_col, value=f"{clus.id}")
        formatting.right_align(cell)
        row_cursor += 1
    return row_cursor


def add_results_to_excel(fd: FormattingData,
                         cls: List[models.InputClustering],
                         ws: Worksheet):
    """
    Appends results to workbook with current time as suffix
    :param fd:
    :param cls: list of models.InputClustering
    :param ws:
    :return:
    """

    category_titles = set()

    row_cursor = fd.start_row
    col_cursor = 0
    title_column = None
    category_columns = []
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
                # Write cluster titlte
                title_cell = ws.cell(row=row_cursor, column=col_cursor, value=cluster_id)
                formatting.bold_cell(title_cell)
                if title_column is None:
                    title_column = title_cell.column

                col_cursor += 1
                # Write categories
                for cat_title in category_titles:
                    cat_cell = ws.cell(row=row_cursor, column=col_cursor + k, value=cat_title)
                    formatting.bold_cell(cat_cell)
                    if len(category_columns) <= len(category_titles):
                        category_columns.append(cat_cell.column)
                    k += 1
                formatting.add_thin_border_to_row(ws, row_cursor, Direction.BOTTOM)
                row_cursor += 1

                # Write cluster labels
                write_cluster_labels(cl, ws, row_cursor, fd.start_column)

            k = 0
            # Write results per category
            for cat in category_titles:
                cat_count = cluster.categories[cat]
                ws.cell(row=row_cursor, column=col_cursor + k, value=cat_count)
                k += 1

            row_cursor += 1
            header_pass = False

        # Write stats
        row_cursor = write_cluster_result_stats(fd, cl, ws, row_cursor)
        row_cursor += fd.padding
    col_cursor += len(category_titles)

    # Set some basic formatting
    formatting.set_column_width(ws, title_column, 20)
    formatting.add_thin_border_to_column(ws, title_column, Direction.RIGHT)
    for c in category_columns:
        formatting.set_column_width(ws, c, 15)
        if c == c[-1:]:
            formatting.add_thin_border_to_column(ws, title_column, Direction.RIGHT)
    return col_cursor, row_cursor

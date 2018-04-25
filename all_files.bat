#!/bin/bash
echo %1
set PYTHONPATH=%1
REM results_norm_9
start "1" /wait py runner/runner.py -if .data/results_norm_9/append-apps-clothing_jewelry-movies/ -o .data/results_norm_9/excels/append-apps-clothing_jewelry-movies.xlsx
start "2" /wait py runner/runner.py -if .data/results_norm_9/append-beauty-gourmet-pets/ -o .data/results_norm_9/excels/append-beauty-gourmet-pets.xlsx
start "3" /wait py runner/runner.py -if .data/results_norm_9/append-books-cell_accessories-sports_outdoors/ -o .data/results_norm_9/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "4" /wait py runner/runner.py -if .data/results_norm_9/replace-apps-clothing_jewelry-movies/ -o .data/results_norm_9/excels/replace-apps-clothing_jewelry-movies.xlsx
start "5" /wait py runner/runner.py -if .data/results_norm_9/replace-beauty-gourmet-pets/ -o .data/results_norm_9/excels/replace-beauty-gourmet-pets.xlsx
start "6" /wait py runner/runner.py -if .data/results_norm_9/replace-books-cell_accessories-sports_outdoors/ -o .data/results_norm_9/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM results_norm_3
start "7" /wait py runner/runner.py -if .data/results_norm_3/append-apps-clothing_jewelry-movies/ -o .data/results_norm_3/excels/append-apps-clothing_jewelry-movies.xlsx
start "8" /wait py runner/runner.py -if .data/results_norm_3/append-beauty-gourmet-pets/ -o .data/results_norm_3/excels/append-beauty-gourmet-pets.xlsx
start "9" /wait py runner/runner.py -if .data/results_norm_3/append-books-cell_accessories-sports_outdoors/ -o .data/results_norm_3/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "10" /wait py runner/runner.py -if .data/results_norm_3/replace-apps-clothing_jewelry-movies/ -o .data/results_norm_3/excels/replace-apps-clothing_jewelry-movies.xlsx
start "11" /wait py runner/runner.py -if .data/results_norm_3/replace-beauty-gourmet-pets/ -o .data/results_norm_3/excels/replace-beauty-gourmet-pets.xlsx
start "12" /wait py runner/runner.py -if .data/results_norm_3/replace-books-cell_accessories-sports_outdoors/ -o .data/results_norm_3/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM results_non_norm_lsa100_3
start "13" /wait py runner/runner.py -if .data/results_non_norm_lsa100_3/append-apps-clothing_jewelry-movies/ -o .data/results_non_norm_lsa100_3/excels/append-apps-clothing_jewelry-movies.xlsx
start "14" /wait py runner/runner.py -if .data/results_non_norm_lsa100_3/append-beauty-gourmet-pets/ -o .data/results_non_norm_lsa100_3/excels/append-beauty-gourmet-pets.xlsx
start "15" /wait py runner/runner.py -if .data/results_non_norm_lsa100_3/append-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_lsa100_3/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "16" /wait py runner/runner.py -if .data/results_non_norm_lsa100_3/replace-apps-clothing_jewelry-movies/ -o .data/results_non_norm_lsa100_3/excels/replace-apps-clothing_jewelry-movies.xlsx
start "17" /wait py runner/runner.py -if .data/results_non_norm_lsa100_3/replace-beauty-gourmet-pets/ -o .data/results_non_norm_lsa100_3/excels/replace-beauty-gourmet-pets.xlsx
start "18" /wait py runner/runner.py -if .data/results_non_norm_lsa100_3/replace-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_lsa100_3/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM results_non_norm_lsa100_9
start "19" /wait py runner/runner.py -if .data/results_non_norm_lsa100_9/append-apps-clothing_jewelry-movies/ -o .data/results_non_norm_lsa100_9/excels/append-apps-clothing_jewelry-movies.xlsx
start "20" /wait py runner/runner.py -if .data/results_non_norm_lsa100_9/append-beauty-gourmet-pets/ -o .data/results_non_norm_lsa100_9/excels/append-beauty-gourmet-pets.xlsx
start "21" /wait py runner/runner.py -if .data/results_non_norm_lsa100_9/append-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_lsa100_9/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "22" /wait py runner/runner.py -if .data/results_non_norm_lsa100_9/replace-apps-clothing_jewelry-movies/ -o .data/results_non_norm_lsa100_9/excels/replace-apps-clothing_jewelry-movies.xlsx
start "23" /wait py runner/runner.py -if .data/results_non_norm_lsa100_9/replace-beauty-gourmet-pets/ -o .data/results_non_norm_lsa100_9/excels/replace-beauty-gourmet-pets.xlsx
start "24" /wait py runner/runner.py -if .data/results_non_norm_lsa100_9/replace-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_lsa100_9/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM results_non_norm_9
start "25" /wait py runner/runner.py -if .data/results_non_norm_9/append-apps-clothing_jewelry-movies/ -o .data/results_non_norm_9/excels/append-apps-clothing_jewelry-movies.xlsx
start "26" /wait py runner/runner.py -if .data/results_non_norm_9/append-beauty-gourmet-pets/ -o .data/results_non_norm_9/excels/append-beauty-gourmet-pets.xlsx
start "27" /wait py runner/runner.py -if .data/results_non_norm_9/append-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_9/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "28" /wait py runner/runner.py -if .data/results_non_norm_9/replace-apps-clothing_jewelry-movies/ -o .data/results_non_norm_9/excels/replace-apps-clothing_jewelry-movies.xlsx
start "29" /wait py runner/runner.py -if .data/results_non_norm_9/replace-beauty-gourmet-pets/ -o .data/results_non_norm_9/excels/replace-beauty-gourmet-pets.xlsx
start "30" /wait py runner/runner.py -if .data/results_non_norm_9/replace-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_9/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM results_non_norm_3
start "31" /wait py runner/runner.py -if .data/results_non_norm_3/append-apps-clothing_jewelry-movies/ -o .data/results_non_norm_3/excels/append-apps-clothing_jewelry-movies.xlsx
start "32" /wait py runner/runner.py -if .data/results_non_norm_3/append-beauty-gourmet-pets/ -o .data/results_non_norm_3/excels/append-beauty-gourmet-pets.xlsx
start "33" /wait py runner/runner.py -if .data/results_non_norm_3/append-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_3/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "34" /wait py runner/runner.py -if .data/results_non_norm_3/replace-apps-clothing_jewelry-movies/ -o .data/results_non_norm_3/excels/replace-apps-clothing_jewelry-movies.xlsx
start "35" /wait py runner/runner.py -if .data/results_non_norm_3/replace-beauty-gourmet-pets/ -o .data/results_non_norm_3/excels/replace-beauty-gourmet-pets.xlsx
start "36" /wait py runner/runner.py -if .data/results_non_norm_3/replace-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_3/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM results_norm_lsa100_3
start "37" /wait py runner/runner.py -if .data/results_norm_lsa100_3/append-apps-clothing_jewelry-movies/ -o .data/results_norm_lsa100_3/excels/append-apps-clothing_jewelry-movies.xlsx
start "38" /wait py runner/runner.py -if .data/results_norm_lsa100_3/append-beauty-gourmet-pets/ -o .data/results_norm_lsa100_3/excels/append-beauty-gourmet-pets.xlsx
start "39" /wait py runner/runner.py -if .data/results_norm_lsa100_3/append-books-cell_accessories-sports_outdoors/ -o .data/results_norm_lsa100_3/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "40" /wait py runner/runner.py -if .data/results_norm_lsa100_3/replace-apps-clothing_jewelry-movies/ -o .data/results_norm_lsa100_3/excels/replace-apps-clothing_jewelry-movies.xlsx
start "41" /wait py runner/runner.py -if .data/results_norm_lsa100_3/replace-beauty-gourmet-pets/ -o .data/results_norm_lsa100_3/excels/replace-beauty-gourmet-pets.xlsx
start "42" /wait py runner/runner.py -if .data/results_norm_lsa100_3/replace-books-cell_accessories-sports_outdoors/ -o .data/results_norm_lsa100_3/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM results_norm_lsa100_9
start "43" /wait py runner/runner.py -if .data/results_norm_lsa100_9/append-apps-clothing_jewelry-movies/ -o .data/results_norm_lsa100_9/excels/append-apps-clothing_jewelry-movies.xlsx
start "44" /wait py runner/runner.py -if .data/results_norm_lsa100_9/append-beauty-gourmet-pets/ -o .data/results_norm_lsa100_9/excels/append-beauty-gourmet-pets.xlsx
start "45" /wait py runner/runner.py -if .data/results_norm_lsa100_9/append-books-cell_accessories-sports_outdoors/ -o .data/results_norm_lsa100_9/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "46" /wait py runner/runner.py -if .data/results_norm_lsa100_9/replace-apps-clothing_jewelry-movies/ -o .data/results_norm_lsa100_9/excels/replace-apps-clothing_jewelry-movies.xlsx
start "47" /wait py runner/runner.py -if .data/results_norm_lsa100_9/replace-beauty-gourmet-pets/ -o .data/results_norm_lsa100_9/excels/replace-beauty-gourmet-pets.xlsx
start "48" /wait py runner/runner.py -if .data/results_norm_lsa100_9/replace-books-cell_accessories-sports_outdoors/ -o .data/results_norm_lsa100_9/excels/replace-books-cell_accessories-sports_outdoors.xlsx




REM Shutdown computer when done
REM shutdown.exe /s /t 00
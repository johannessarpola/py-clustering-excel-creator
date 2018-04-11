#!/bin/bash
echo %1
set PYTHONPATH=%1
start "1" /wait py runner/runner.py -if .data/results_non_norm_9/append-apps-clothing_jewelry-movies/ -o .data/results_non_norm_9/excels/append-apps-clothing_jewelry-movies.xlsx
start "2" /wait py runner/runner.py -if .data/results_non_norm_9/append-beauty-gourmet-pets/ -o .data/results_non_norm_9/excels/append-beauty-gourmet-pets.xlsx
start "3" /wait py runner/runner.py -if .data/results_non_norm_9/append-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_9/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "4" /wait py runner/runner.py -if .data/results_non_norm_9/replace-apps-clothing_jewelry-movies/ -o .data/results_non_norm_9/excels/replace-apps-clothing_jewelry-movies.xlsx
start "5" /wait py runner/runner.py -if .data/results_non_norm_9/replace-beauty-gourmet-pets/ -o .data/results_non_norm_9/excels/replace-beauty-gourmet-pets.xlsx
start "6" /wait py runner/runner.py -if .data/results_non_norm_9/replace-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_9/excels/replace-books-cell_accessories-sports_outdoors.xlsx

start "7" /wait py runner/runner.py -if .data/results_non_norm_3/append-apps-clothing_jewelry-movies/ -o .data/results_non_norm_3/excels/append-apps-clothing_jewelry-movies.xlsx
start "8" /wait py runner/runner.py -if .data/results_non_norm_3/append-beauty-gourmet-pets/ -o .data/results_non_norm_3/excels/append-beauty-gourmet-pets.xlsx
start "9" /wait py runner/runner.py -if .data/results_non_norm_3/append-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_3/excels/append-books-cell_accessories-sports_outdoors.xlsx
start "10" /wait py runner/runner.py -if .data/results_non_norm_3/replace-apps-clothing_jewelry-movies/ -o .data/results_non_norm_3/excels/replace-apps-clothing_jewelry-movies.xlsx
start "11" /wait py runner/runner.py -if .data/results_non_norm_3/replace-beauty-gourmet-pets/ -o .data/results_non_norm_3/excels/replace-beauty-gourmet-pets.xlsx
start "12" /wait py runner/runner.py -if .data/results_non_norm_3/replace-books-cell_accessories-sports_outdoors/ -o .data/results_non_norm_3/excels/replace-books-cell_accessories-sports_outdoors.xlsx

REM Shutdown computer when done
REM shutdown.exe /s /t 00
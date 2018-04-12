import argparse

from app.src import app

parser = argparse.ArgumentParser()

parser.add_argument('-if', "--input_folder", help="where the documents are located", )
parser.add_argument('-o', "--output_file", help="output file excel", )

args = parser.parse_args()

if __name__ == '__main__':
    inp = args.input_folder
    out = args.output_file
    app.main(inp, out)
    print("done!")

from argparse import ArgumentParser, ArgumentError
from pathlib import Path
from os import path
from datetime import datetime
import constants as const

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

parser = ArgumentParser()
parser.add_argument("dir", help="create a file at this directory.")
parser.add_argument("file", help="file name to create with extension.")
parser.add_argument("-s",
                    "--symbol",
                    help="comment symbol for the file extension")
args = parser.parse_args()

file_name, file_extension = path.splitext(args.file)

if file_extension[1:] != const.LANG_EXT and args.symbol == None:
    parser.error(f"provide comment symbol for `{file_extension}` extension through [-s] flag")

symbol = None
if file_extension[1:] == const.LANG_EXT:
    symbol = const.LANG_COMMENT_SYMBOL
else:
    symbol = args.symbol
CONTENTS = [f"{symbol} PVT", " ", f"{now} IST {symbol}\n"]

dir_path = path.join(const.REPO_PATH, f"{args.dir}")
Path(dir_path).mkdir(parents=True, exist_ok=True)

file_path = dir_path + f"/{file_name}{file_extension}"
with open(file_path, 'w') as target:
    target.writelines(CONTENTS)
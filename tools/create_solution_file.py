from argparse import ArgumentParser
from pathlib import Path
from os import path
from datetime import datetime

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
CONTENTS = ["# PVT", " ", f"{now} IST #\n"]

parser = ArgumentParser()
parser.add_argument("dir", help="create a file at this directory.")
parser.add_argument("file", help="file name to create with extension.")
args = parser.parse_args()

dir_path = path.join(path.dirname(path.abspath(__file__)), f"../{args.dir}")
Path(dir_path).mkdir(parents=True, exist_ok=True)

file_path = dir_path + f"/{args.file}"
with open(file_path, 'w') as target:
    target.writelines(CONTENTS)
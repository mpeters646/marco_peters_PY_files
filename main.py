__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile
from pathlib import Path
import fileinput


def clean_cache():
    if not os.path.exists("./files/cache"):
        os.makedirs("./files/cache")
        # print("Created Directory : ", "./files/cache")
    else:
        shutil.rmtree("./files/cache")
        os.makedirs("./files/cache")
        # print("Directory already existed, : ", "./files/cache")


def cache_zip(zip_file_path, cache_dir_path):
    with ZipFile(zip_file_path) as zipObj:
        zipObj.extractall(cache_dir_path)


root_path = (
    "C:\\Users\\marco\\Google Drive\\WincAcademy\\Winc_Academy_BED\\files\\cache"
)


def cached_files():
    file_list = []
    for root, _, filenames in os.walk(root_path):
        for filename in filenames:
            file_list.append(os.path.join(root, filename))
    return file_list


def find_password(files_list):
    for file in files_list:
        with open(file, "r") as f:
            content = f.readlines()
            for line in content:
                if "password" in line:
                    line = line.split(" ")
                    return line[1].strip("\n")


# clean_cache()
# cache_zip("./files/data.zip", "./files/cache")
# print(cached_files())
# print(find_password(cached_files()))

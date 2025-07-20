#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2025 Hai Liang Wang<hailiang.hl.wang@gmail.com> All Rights Reserved
#
#
# File: /c/Users/Administrator/projects/2025_03_01_zhangphd_paper/experiments/data/src/gen_label2num.py
# Author: Hai Liang Wang
# Date: 2025-07-20:12:22:34
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2025 Hai Liang Wang<hailiang.hl.wang@gmail.com> All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2025-07-20:12:22:34"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str


import shutil
import math
import csv
import json

from pathlib import Path
from sklearn.utils import shuffle

ROOT_DIR = os.path.join(curdir, os.pardir)
NUM2LABEL_JSON = os.path.join(ROOT_DIR, "labels", "num2label.json")
LABEL2NUM_JSON = os.path.join(ROOT_DIR, "labels", "label2num.json")
LABEL_CLASS_CSV = os.path.join(ROOT_DIR, "labels", "labels.autogen.csv")

def get_dataset_cate(folder_path):
    '''
    get train or test
    '''
    return os.path.basename(os.path.dirname(folder_path))

def main():
    total_images_counter = 0
    class_labels = set()
    output_lines = []

    with open(LABEL_CLASS_CSV, "w") as fout:
        fout.writelines(["#filepath, label\n"])

    for x in ["train", "test"]:
        target_folder = os.path.join(ROOT_DIR, x)
        for root, dirs, images in os.walk(target_folder):
            for y in images:
                print("basename", os.path.basename(root))
                print("dirname", get_dataset_cate(root))
                label = os.path.basename(root).strip()
                class_labels.add(label)
                rel_path_from_root="/".join([get_dataset_cate(root), label, y])
                print("rel_path_from_root", rel_path_from_root)
                print("y", y)
                output_lines.append("%s, %s\n" % (rel_path_from_root, label))
                total_images_counter += 1

    with open(LABEL_CLASS_CSV, "a") as fout:
        fout.writelines(output_lines)

    print(f"Get all labels {class_labels}")
    print(f"Get images counter {total_images_counter}")


    with open(NUM2LABEL_JSON, 'w') as f:
        data = {}
        num = 0
        for x in list(class_labels):
            data[num] = x
            num += 1

        json.dump(data, f, ensure_ascii=False, indent=4)

    with open(LABEL2NUM_JSON, 'w') as f:
        data = {}
        num = 0
        for x in list(class_labels):
            data[x] = num
            num += 1

        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()

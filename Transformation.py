import os
import sys
import argparse
from plantcv import plantcv as pcv


def transformation(path: str):
    original_img, path, filename = pcv.readimage(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-src', type=str)
    parser.add_argument('-dst', type=str)
    parser.add_argument('-mask', action='store_true')
    args = parser.parse_args()

    src_dir = args.src
    dst_dir = args.dst
    mask = args.mask
    print(src_dir)
    print(dst_dir)
    print(mask)

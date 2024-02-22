import os
import sys
import argparse
from plantcv import plantcv as pcv
import matplotlib.pyplot as plt


def transformation(filename: str):
    print('what')
    try:
        img, path, filename = pcv.readimage(filename)
    except Exception as e:
        print(f"{e.__class__.__name}: {e}")
        exit(1)
    gaussian_blur_img = pcv.gaussian_blur(img, ksize=(11, 11))
    plt.imshow(gaussian_blur_img)
    plt.show()
    mask_img = pcv.apply_mask(img, mask= ,mask_color='green')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', default=None)
    parser.add_argument('-src', type=str, default=None)
    parser.add_argument('-dst', type=str, default=None)
    parser.add_argument('-mask', action='store_true')
    args = parser.parse_args()

    src_dir = args.src
    dst_dir = args.dst
    mask = args.mask
    if args.filename is not None:
        transformation(args.filename)


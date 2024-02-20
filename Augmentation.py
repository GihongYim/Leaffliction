import os
import sys
from plantcv import plantcv as pcv
import numpy as np


def augmentation(path: str):
    try:
        original_img, path, filename = pcv.readimage(path)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
    os.path.join("augmented_directory", path)
    print(filename)
    split_filename = path.split('.')
    path[0] = path[0] + "_Flip"
    flip_filename = '.'.join(split_filename)
    print(flip_filename)
    flip(original_img)


def flip(img: np.ndarray):
    flipped = pcv.flip(img=img, direction='horizontal')
    pcv.print_image(flipped, path)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, \
             "input -> python Augumentation.py $FILEPATH"

    except Exception as e:
        print(f"Error: {e}")
        exit(0)
    try:
        if os.path.exists(sys.argv[1]) is False:
            raise FileNotFoundError(sys.argv[1])
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    aug_dir = "augmented_directory"
    if not os.path.exists(aug_dir):
        os.mkdir(aug_dir)
    path = sys.argv[1]
    augmentation(path)

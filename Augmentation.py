import os
import sys
from plantcv import plantcv as pcv
import numpy as np


def augmentation(path: str):
    try:
        original_img, path, filename = pcv.readimage(path)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
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
    augmentation_path = "augmented_directory"
    if not os.path.exists(augmentation_path):
        os.mkdir(augmentation_path)
    path = sys.argv[1]
    augmentation(path)

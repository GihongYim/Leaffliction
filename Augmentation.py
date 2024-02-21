import os
import sys
import cv2
from plantcv import plantcv as pcv
import numpy as np


def augmentation(path: str):
    try:
        original_img, path, filename = pcv.readimage(path)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
    flip(original_img, path, filename, direction='vertical')
    rotate(original_img, path, filename, rotation_deg=45, crop=True)
    skew_factor = 0.5
    skew_matrix = np.array([[1, skew_factor, 0], [0, 1, 0]])
    skew(original_img, path, filename,
         skew_matrix=skew_matrix,
         skew_factor=skew_factor)


def flip(img: np.ndarray, path, filename, direction='vertical'):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Flip"
    flip_filename = '.'.join(split_filename)
    flipped = pcv.flip(img=img, direction=direction)
    pcv.print_image(flipped, filename=os.path.join(augmentation_dir,
                                                   flip_filename))


def rotate(img: np.ndarray, path, filename, rotation_deg, crop=True):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Rotate"
    flip_filename = '.'.join(split_filename)
    rotated = pcv.transform.rotate(img=img,
                                   rotation_deg=rotation_deg,
                                   crop=crop)
    pcv.print_image(rotated, filename=os.path.join(augmentation_dir,
                                                   flip_filename))


def rotate(img: np.ndarray, path, filename, rotation_deg, crop=True):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Rotate"
    flip_filename = '.'.join(split_filename)
    rotated = pcv.transform.rotate(img=img,
                                   rotation_deg=rotation_deg,
                                   crop=crop)
    pcv.print_image(rotated, filename=os.path.join(augmentation_dir,
                                                   flip_filename))


def skew(img: np.ndarray, path, filename, skew_matrix, skew_factor):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Skew"
    flip_filename = '.'.join(split_filename)

    rows, cols, _ = img.shape
    skewed_img_array = cv2.warpAffine(img, skew_matrix, (cols, rows))
    pcv.print_image(skewed_img_array, filename=os.path.join(augmentation_dir,
                                                            flip_filename))


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

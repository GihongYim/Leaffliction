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
    # flip
    flip(original_img, path, filename, direction='vertical')

    # rotate
    rotate(original_img, path, filename, rotation_deg=45, crop=True)

    # skew
    skew_factor = 0.5
    skew_matrix = np.array([[1, skew_factor, 0], [-skew_factor, 1, 0]])
    skew(original_img, path, filename,
         skew_matrix=skew_matrix)
    # shear
    shear_factor = 0.5
    shear_matrix = np.array([[1, shear_factor, 0], [0, 1, 0]])
    shear(original_img, path, filename,
          shear_matrix=shear_matrix)

    # crop
    crop(original_img, path, filename, x=80, y=80, h=80, w=80)

    # distortion
    distortion(original_img, path, filename)


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
    rotate_filename = '.'.join(split_filename)
    rotated = pcv.transform.rotate(img=img,
                                   rotation_deg=rotation_deg,
                                   crop=crop)
    pcv.print_image(rotated, filename=os.path.join(augmentation_dir,
                                                   rotate_filename))


def skew(img: np.ndarray, path, filename, skew_matrix):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Skew"
    skew_filename = '.'.join(split_filename)

    rows, cols, _ = img.shape
    skewed_img_array = cv2.warpAffine(img, skew_matrix, (cols, rows))
    pcv.print_image(skewed_img_array, filename=os.path.join(augmentation_dir,
                                                            skew_filename))


def shear(img: np.ndarray, path, filename, shear_matrix):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Shear"
    shear_filename = '.'.join(split_filename)

    rows, cols, _ = img.shape
    sheared_img_array = cv2.warpAffine(img, shear_matrix, (cols, rows))
    pcv.print_image(sheared_img_array, filename=os.path.join(augmentation_dir,
                                                             shear_filename))


def crop(img: np.ndarray, path, filename, x, y, h, w):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Crop"
    crop_filename = '.'.join(split_filename)

    rows, cols, _ = img.shape
    crop_img = pcv.crop(img=img, x=x, y=y, h=h, w=w)
    resize_crop_img = cv2.resize(crop_img, dsize=(rows, cols))
    print(resize_crop_img.shape)
    pcv.print_image(resize_crop_img, filename=os.path.join(augmentation_dir,
                                                           crop_filename))


def distortion(img: np.ndarray, path, filename):
    augmentation_dir = os.path.join("augmented_directory", path)
    if not os.path.exists(augmentation_dir):
        os.makedirs(augmentation_dir)
    split_filename = filename.split('.')
    split_filename[0] = split_filename[0] + "_Distortion"
    distortion_filename = '.'.join(split_filename)

    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 1] = hsv_image[:, :, 1] * 0.5

    distoted_img = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    pcv.print_image(distoted_img, filename=os.path.join(augmentation_dir,
                                                        distortion_filename))


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

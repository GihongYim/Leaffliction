import os
import sys
from PIL import Image, ImageOps


def augmentation(path: str):
    path_list = list(os.path.split(sys.argv[1]))
    folder_path = path_list[0]
    file_name = path_list[1]
    folder_list = list(os.path.split(folder_path))
    folder_list[0] = folder_list[0].replace('Apple', 'augmented_directory')
    folder_path = os.path.join(*folder_list)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    original_img = Image.open(path)
    # flip image
    flip_name = file_name.replace('.', '_Flip.')
    flip(original_img, os.path.join(folder_path, flip_name))
    # rotate image
    rotate_name = file_name.replace('.', '_Rotate.')
    rotate(original_img, os.path.join(folder_path, rotate_name))
    # Skew image
    skew_name = file_name.replace('.', '_Skew.')
    skew(original_img, os.path.join(folder_path, skew_name))


def flip(img: Image, path):
    flip_img = ImageOps.flip(img)
    flip_img.save(path)


def rotate(img: Image, path):
    rotate_img = img.rotate(90)
    rotate_img.save(path)


def skew(img: Image, path):
    rotate_img = img.rotate(90)
    rotate_img.save(path)


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
    if not os.path.exists("augmented_directory"):
        os.mkdir("augmented_directory")
    path = sys.argv[1]
    augmentation(path)

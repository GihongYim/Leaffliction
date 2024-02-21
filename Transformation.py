import os
import sys
from plantcv import plantcv as pcv


def transformation(path: str):
    original_img, path, filename = pcv.readimage(path)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, \
             "input -> python Transformation.py $FILEPATH"

    except Exception as e:
        print(f"Error: {e}")
        exit(0)
    try:
        if os.path.exists(sys.argv[1]) is False:
            raise FileNotFoundError(sys.argv[1])
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    path = sys.argv[1]
    try:
        transformation(path)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")

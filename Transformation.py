import os
import sys
import argparse
from plantcv import plantcv as pcv


def transformation(path: str):
    original_img, path, filename = pcv.readimage(path)


if __name__ == "__main__":
    

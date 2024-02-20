import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns


def get_category(image_root_path: str) -> dict():
    category = dict()
    image_root_dir = image_root_path
    for dir_name in os.listdir(image_root_dir):
        file_num = len(os.listdir(os.path.join(image_root_dir, dir_name)))
        category[dir_name] = file_num
    return category


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, \
            'input should be $PATH/Distribution.py target_dir'
    except Exception as e:
        print(f"{e.__class__.__name__} {e}")
        exit(0)
    category = get_category(sys.argv[1])
    print(category)
    apple_name = list(category.keys())
    apple_num = list(category.values())
    fig, ax = plt.subplots(ncols=2)
    colors = sns.color_palette('hls', len(apple_name))
    fig.suptitle('apple class distribution')

    ax[0].pie(apple_num,
              labels=apple_name,
              colors=colors,
              autopct='%.1f%%'
              )
    ax[1].bar(category.keys(), category.values(), color=colors)
    plt.show()

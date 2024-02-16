import os
import matplotlib.pyplot as plt


def get_category(image_root_path: str) -> dict():
    category = dict()
    image_root_dir = './Apple'
    for dir_name in os.listdir(image_root_dir):
        file_num = len(os.listdir(os.path.join(image_root_dir, dir_name)))
        category[dir_name] = file_num
    return category


if __name__ == "__main__":
    category = get_category('./Apple')
    print(category)
    apple_name = list(category.keys())
    apple_num = list(category.values())
    fig, ax = plt.subplots(ncols=2)

    ax[0].pie(apple_num,
              labels=apple_name,
              autopct='%.1f%%'
              )
    ax[1].bar(category.keys(), category.values())
    plt.show()

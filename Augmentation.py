import os
import sys


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
    path = os.path.split(sys.argv[1])
    
    folder_path = path[0]
    file_name = path[1]
    folder_list = list(os.path.split(folder_path))
    folder_list[0] = folder_list[0].replace('Apple', 'augmented_directory')
    folder_path = os.path.join(*folder_list)
    return_path = os.path.join(folder_path, file_name)
    print(return_path)

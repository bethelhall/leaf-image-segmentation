import os
import pathlib

from utils import *
from background_marker import *


def generate_background_markers(folder, intensity=5):
    # integrate directory name and create a new directory
    if folder.endswith(os.sep):
        folder = folder[:-1]
    if not os.path.isdir(folder):
        print(folder, ': is not a directory')
        return
    new_folder = folder + '_markers'
    os.makedirs(new_folder, exist_ok=True)

    for subdir, dirs, files in os.walk(folder):
        for file in files:
            try:
                original_image = read_image(os.path.join(folder, file))

                marker = np.full((original_image.shape[0], original_image.shape[1]), True)
                color_index_marker(index_diff(original_image), marker)

                image = np.zeros((original_image.shape))
                image[marker] = np.array([intensity, intensity, intensity])
                # image[~marker] = np.array([0, 0, 0])

            except ValueError as err:
                    print('Error: Not color image file: ', file)
                else:
                    pass
            else:
                print('Marker generated for image file: ', file)


if __name__ == '__main__':
    while True:
        folder = input('Enter absolute folder path: ')
        generate_background_markers(folder)
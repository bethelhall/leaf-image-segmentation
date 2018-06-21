import numpy as np
import cv2


# error message when image could not be read
IMAGE_NOT_READ = 'IMAGE_NOT_READ'

# error message when image is not colored while it should be
NOT_COLOR_IMAGE = 'NOT_COLOR_IMAGE'


def read_image(file_path, read_mode=cv2.IMREAD_COLOR):
    """
    Read image file with all preprocessing needed

    Args:
        file_path: absolute file_path of an image file
        read_mode: whether image reading mode is rgb, grayscale or somethin

    Returns:
        np.ndarray of the read image or None if couldn't read

    Raises:
        ValueError if image could not be read with message IMAGE_NOT_READ
    """
    # read image file in grayscale
    image = cv2.imread(file_path, read_mode)

    if image is None:
        raise ValueError(IMAGE_NOT_READ)
    else:
        return image


def ensure_color(image):
    """
    Ensure that an image is colored
    Args:
        image: image to be checked for

    Returns:
        nothing

    Raises:
        ValueError with message code if image is not colored
    """
    if len(image.shape) < 3:
        raise ValueError(NOT_COLOR_IMAGE)


def excess_green(image, scale = 2):
    """
    Compute excess green index for colored image

    Args:
        image: image to be converted
        scale: number to scale green channel of the image

    Returns:
        new image with excess green
    """

    ensure_color(image)

    new_image = image.copy()
    new_image[:, :, 1] = scale * image[:, :, 1]

    return new_image


def excess_red(image, scale=1.4):
    """
    Compute excess red index for colored image

    Args:
        image: image to be converted
        scale: number to scale red channel of the image

    Returns:
        new image with excess red
    """

    ensure_color(image)

    new_image = image.copy()
    new_image[:, :, 2] = scale * image[:, :, 2]

    return new_image


def debug(value, name=None):
    if isinstance(value, np.ndarray):
        name = 'ndarray' if name is None else name

        print("{}: {}".format(name, value))
        print("{} shape: {}".format(name, value.shape))
    else:
        name = 'value' if name is None else name

        print("{} type: {}".format(name, type(value)))
        print("{}: {}".format(name, value))


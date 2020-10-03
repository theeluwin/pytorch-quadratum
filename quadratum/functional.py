import os
import numpy as np

from typing import (
    Tuple,
    Union,
)

from cv2 import imencode
from skimage.io import imread
from skimage.color import gray2rgb
from skimage.transform import resize


__all__: Tuple[str, ...] = (
    'validate_image',
    'whiten',
    'invert',
    'dominofy',
    'contain',
)


def validate_image(path: str,
                   min_size: int = 2,
                   allow_gray: bool = False
                   ) -> bool:

    # check path
    if not os.path.isfile(path):
        return False

    # check image
    image: np.ndarray = imread(path)
    if image is None:
        return False

    # check jpg-convertable
    is_valid: bool
    istr: str
    is_valid, istr = imencode('.jpg', image)
    if not is_valid:
        return False
    if not (istr[0] == 0xff and istr[1] == 0xd8 and istr[len(istr) - 2] == 0xff and istr[len(istr) - 1] == 0xd9):
        return False

    # check shape
    try:
        h, w = image.shape
        c = 1
    except ValueError:
        try:
            h, w, c = image.shape
        except ValueError:
            return False

    # check gray
    if not allow_gray and c < 3:
        return False

    # check minimum size
    if h < min_size or w < min_size:
        return False

    # check variance
    if image.var() < 1:
        return False

    return True


def whiten(image: np.ndarray) -> np.ndarray:

    # if gray, change it to rgb
    h: int
    w: int
    c: int
    try:
        h, w, c = image.shape
    except ValueError:
        h, w = image.shape
        return gray2rgb(image)

    # if 3-channeled, just return
    if c == 3:
        return image

    # if alpha-channeled, fill with white (actually, it's more like dumping the image on a white canvas)
    elif c == 4:
        content: np.ndarray = image[:, :, :3]
        alpha: np.ndarray = image[:, :, 3].astype(np.float32)[:, :, np.newaxis] / 255
        canvas: np.ndarray = np.ones((h, w, 3), dtype=np.float32) * 255
        composed: np.ndarray = alpha * content + (1 - alpha) * canvas
        return composed.astype(np.uint8)

    # no other cases are allowed
    raise ValueError(f"Invalid image channel size. It should be either 3 or 4, but got {c}.")


def invert(image: np.ndarray) -> np.ndarray:
    return 255 - image


def dominofy(image: np.ndarray,
             threshold: float = 3.0
             ) -> np.ndarray:

    # get image shape
    h: int
    w: int
    h, w, _ = image.shape

    # if acceptable, just return
    if h / w < threshold and w / h < threshold:
        return image

    # if vertically long
    if h > w:
        cy: float = h / 2
        ysize: float = w * threshold / 2
        return image[int(cy - ysize): int(cy + ysize), :, :]

    # if horizontally long
    else:
        cx: float = w / 2
        xsize: float = h * threshold / 2
        return image[:, int(cx - xsize): int(cx + xsize), :]


def contain(image: np.ndarray,
            size: Union[int, Tuple[int, int]],
            fill: Union[str, Tuple[int, int, int]] = 'white'
            ) -> np.ndarray:

    # deal with size parameter
    canvas_height: int
    canvas_width: int
    if isinstance(size, int):
        canvas_height = size
        canvas_width = size
    elif isinstance(size, tuple) and len(size) == 2:
        canvas_height = size[0]
        canvas_width = size[1]
    else:
        raise TypeError(f"Invalid parameter type: `size` should be either `int` or `tuple` of (`int`, `int`), but got {size} with type `{type(size)}``.")
    canvas: np.ndarray = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8)

    # deal with fill parameter
    if isinstance(fill, str):
        if fill == 'white':
            canvas = canvas * 255
        elif fill == 'black':
            canvas = canvas * 0
        else:
            raise TypeError(f"Invalid parameter value: `fill` should be either of 'white', 'black', or `tuple` of (`int`, `int`, `int`), but got {fill} with type `{type(fill)}`.")
    elif isinstance(fill, tuple) and len(fill) == 3:
        canvas = canvas * fill
    else:
        raise TypeError(f"Invalid parameter type: `fill` should be either of 'white', 'black', or `tuple` of (`int`, `int`, `int`), but got {fill} with type `{type(fill)}`.")

    # get the original image shape
    original_height: int
    original_width: int
    original_height, original_width, _ = image.shape

    # get ratios
    original_ratio: float = original_height / original_width
    canvas_ratio: float = canvas_height / canvas_width

    # resize the original image so it can fit into the canvas
    resize_height: int
    resize_width: int

    # if vertically long
    if original_ratio > canvas_ratio:
        resized_height = canvas_height
        resized_width = int(canvas_height / original_ratio)

    # if horizontally long
    else:
        resized_height = int(canvas_width * original_ratio)
        resized_width = canvas_width

    # resize it
    resized_image: np.ndarray = resize(image, (resized_height, resized_width), mode='reflect', preserve_range=True)

    # fill it
    canvas[
        int((canvas_height - resized_height) / 2): int((canvas_height + resized_height) / 2),
        int((canvas_width - resized_width) / 2): int((canvas_width + resized_width) / 2),
        :
    ] = resized_image

    return canvas

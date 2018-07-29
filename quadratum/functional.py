# -*- coding: utf-8 -*-

from __future__ import division

import os
import numpy as np

from skimage.io import imread
from skimage.color import gray2rgb
from skimage.transform import resize


def validate(path, min_size=1):
    if not os.path.isfile(path):
        return False
    try:
        image = imread(path)
    except:
        return False
    try:
        h, w = image.shape
    except:
        try:
            h, w, c = image.shape
        except:
            return False
    if h < min_size or w < min_size:
        return False
    if not image.var():
        return False
    return True


def whiten(image):
    try:
        h, w, c = image.shape
    except:
        h, w = image.shape
        return gray2rgb(image)
    if c == 3:
        return image
    elif c == 4:
        alpha = image[:, :, 3].astype(np.float32)[:, :, np.newaxis] / 255
        image = image[:, :, :3]
        canvas = np.ones((h, w, 3), dtype=np.float32) * 255
        composed = alpha * image + (1 - alpha) * canvas
        return composed.astype(np.uint8)
    else:
        raise ValueError("Invalid image channel size.")


def invert(image):
    return image.max() - image


def dominofy(image, threshold=2):
    h, w, _ = image.shape
    if h / w < threshold and w / h < threshold:
        return image
    if h > w:
        cy = int(h / 2)
        size = w * threshold / 2
        return image[int(cy - size): int(cy + size), :, :]
    else:
        cx = int(w / 2)
        size = h * threshold / 2
        return image[:, int(cx - size): int(cx + size), :]


def contain(image, size, fill='white'):
    if type(size) == int:
        size = (size, size)
    bh = size[0]
    bw = size[1]
    if fill == 'white':
        canvas = np.ones((bh, bw, 3), dtype=np.uint8) * 255
    elif fill == 'black':
        canvas = np.zeros((bh, bw, 3), dtype=np.uint8)
    else:
        raise ValueError("Invalid fill option.")
    ih, iw, _ = image.shape
    ir = ih / iw
    br = bh / bw
    if ir > br:
        image = resize(image, (bh, int(bh / ir)), mode='reflect', preserve_range=True)
    else:
        image = resize(image, (int(bw * ir), bw), mode='reflect', preserve_range=True)
    h, w, _ = image.shape
    canvas[int(bh / 2 - h / 2): int(bh / 2 + h / 2), int(bw / 2 - w / 2): int(bw / 2 + w / 2), :] = image
    return canvas

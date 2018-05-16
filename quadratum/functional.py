# -*- coding: utf-8 -*-

from __future__ import division

import numpy as np

from skimage.color import gray2rgb
from skimage.transform import resize


def whiten(image, threshold=255):
    try:
        h, w, d = image.shape
    except:
        h, w = image.shape
        return gray2rgb(image)
    if d == 3:
        return image
    canvas = np.ones((h, w, 3), dtype=np.uint8) * 255
    for y in range(h):
        for x in range(w):
            if image[y, x][3] >= threshold:
                canvas[y, x] = image[y, x][:3]
    return canvas


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


def contain(image, size):
    if type(size) == int:
        size = (size, size)
    bh = size[0]
    bw = size[1]
    canvas = np.ones((bh, bw, 3), dtype=np.uint8) * 255
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

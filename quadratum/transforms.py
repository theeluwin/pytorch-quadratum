# -*- coding: utf-8 -*-

from . import functional as F

__all__ = ["Whiten", "Dominofy", "Contain"]


class Whiten(object):
    """Make all transparent pixels white (if there is an alpha channel)."""

    def __init__(self, threshold=255):
        self.threshold = threshold

    def __call__(self, image):
        return F.whiten(image, self.threshold)


class Dominofy(object):
    """Limits the ratio of an image."""

    def __init__(self, threshold=2):
        self.threshold = threshold

    def __call__(self, image):
        return F.dominofy(image, self.threshold)


class Contain(object):
    """Contains an image into given canvas, like good-old `background-size: contain;` from CSS."""

    def __init__(self, size):
        self.size = size

    def __call__(self, image):
        return F.contain(image, self.size)

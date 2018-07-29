# -*- coding: utf-8 -*-

from . import functional as F

__all__ = ["Whiten", "Invert", "Dominofy", "Contain"]


class Whiten(object):
    """Make all transparent pixels white (if there is an alpha channel)."""

    def __init__(self):
        pass

    def __call__(self, image):
        return F.whiten(image)


class Invert(object):
    """Invert RGB values."""

    def __init__(self):
        pass

    def __call__(self, image):
        return F.invert(image)


class Dominofy(object):
    """Limits the ratio of an image."""

    def __init__(self, threshold=2):
        self.threshold = threshold

    def __call__(self, image):
        return F.dominofy(image, self.threshold)


class Contain(object):
    """Contains an image into given canvas, like good-old `background-size: contain;` from CSS."""

    def __init__(self, size, fill='white'):
        self.size = size
        if fill in ['white', 'black']:  # todo: customizable filling color
            self.fill = fill
        else:
            raise ValueError("Invalid fill option.")

    def __call__(self, image):
        return F.contain(image, self.size, fill=self.fill)

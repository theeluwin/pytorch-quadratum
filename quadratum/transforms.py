import numpy as np

from typing import Any

from . import functional as F


__all__ = (
    'Whiten',
    'Invert',
    'Dominofy',
    'Contain',
)


class Whiten(object):
    """Make all transparent pixels white (if there is an alpha channel)."""

    def __init__(self) -> None:
        pass

    def __call__(self, image: np.ndarray) -> np.ndarray:
        return F.whiten(image)


class Invert(object):
    """Invert RGB values."""

    def __init__(self) -> None:
        pass

    def __call__(self, image: np.ndarray) -> np.ndarray:
        return F.invert(image)


class Dominofy(object):
    """Limits the ratio of an image."""

    def __init__(self, threshold: float = 3.0) -> None:
        self.threshold: float = threshold

    def __call__(self, image: np.ndarray) -> np.ndarray:
        return F.dominofy(image, self.threshold)


class Contain(object):
    """Contains an image into given canvas, like good-old `background-size: contain;` from CSS."""

    def __init__(self, size: Any, fill: Any = 'white') -> None:
        self.size: Any = size
        self.fill: Any = fill

    def __call__(self, image: np.ndarray) -> np.ndarray:
        return F.contain(image, size=self.size, fill=self.fill)

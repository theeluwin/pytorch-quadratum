import torch
import numpy as np

from typing import Tuple

from torchvision import transforms as vtrfm

from . import transforms as qtrfm


__all__: Tuple[str, ...] = (
    'Transformer',
)


class Transformer(object):
    """Useful pre-defined transforms just for me."""

    def __init__(self, name: str) -> None:
        self.transform: vtrfm.Compose
        if name == 'resnet':
            self.transform = vtrfm.Compose([
                qtrfm.Whiten(),
                qtrfm.Dominofy(),
                qtrfm.Contain(256),
                vtrfm.ToPILImage(),
                vtrfm.CenterCrop(224),
                vtrfm.ToTensor(),
                vtrfm.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            ])
        elif name == 'inception':
            self.transform = vtrfm.Compose([
                qtrfm.Whiten(),
                qtrfm.Dominofy(),
                qtrfm.Contain(320),
                vtrfm.ToPILImage(),
                vtrfm.CenterCrop(299),
                vtrfm.ToTensor(),
                vtrfm.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
            ])
        else:
            raise NotImplementedError

    def __call__(self, image: np.ndarray) -> torch.Tensor:
        return self.transform(image)

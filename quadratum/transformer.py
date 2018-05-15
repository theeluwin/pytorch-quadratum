# -*- coding: utf-8 -*-

from . import transforms as qtrfm
from torchvision import transforms as vtrfm


class Transformer(object):
    """Useful pre-defined transforms just for me."""

    def __init__(self, name):
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

    def __call__(self, image):
        return self.transform(image)

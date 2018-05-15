Quadratum
==========

Additional torchvision image transforms for practical usage.

Just for me. I needed it.

Note that all functors implemented here assumes an input image to be (H, W, C)-size np.uint8, ranged from 0 to 255.

`Whiten`: make all transparent pixels white.

`Dominofy`: limits the ratio of an image, like dominos.

`Contain`: contains an image into given canvas (or box, whatever), just like, you know, the `background-size: contain;` thingi from CSS?


Installation
-----

```sh
python setup.py install
```

Usage
-----

Similar to all the other transform functors:

```python
from quadratum import transforms as qtrfm
from torchvision import transforms as vtrfm
transform = vtrfm.Compose([
    qtrfm.Whiten(),
    qtrfm.Dominofy(),
    qtrfm.Contain(256),
    vtrfm.ToPILImage(),
    vtrfm.CenterCrop(224),
    vtrfm.ToTensor(),
    vtrfm.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
```

or, you can use some pretrained transformers:

```python
from quadratum.transformer import Transformer
transform = Transformer('resnet')
```

---

"Quadratum" means "square" in Latin. I wanted to make any noisy user-input images into fine-nice-good-well-godlike-heaven-deep-learning-applicable-preprocessed-square-images.

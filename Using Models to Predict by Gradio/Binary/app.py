import platform
import pathlib
plt = platform.system()
pathlib.WindowsPath = pathlib.PosixPath


import requests


# AUTOGENERATED! DO NOT EDIT! File to edit: app.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'interface', 'classify_image']

# %% app.ipynb 1
from fastai.vision.all import *
import PIL.Image
PIL.Image.MAX_IMAGE_PIXELS = None
from PIL import Image

import gradio as gr

# %% app.ipynb 2
learn = load_learner('Binarymodel.pkl')

# %% app.ipynb 3
categories=('Brain','Chest','Random')

def classify_image(img):
    pred,indx,probs=learn.predict(img)
    return dict(zip(categories,map(float,probs)))


# %% app.ipynb 4
image=gr.inputs.Image(shape=(512,512))
label=gr.outputs.Label()
examples=['1.jpg','10.jpg','2.jpeg','9.jpg','3.jpg','4.jpg','5.jpg','6.png','7.jpg',
'8.jpeg','9.jpg','b.jpg','d.jpg','f.jpg','e.jpg']


interface=gr.Interface(fn=classify_image, inputs=image ,outputs=label,examples=examples)
interface.launch(inline=False)
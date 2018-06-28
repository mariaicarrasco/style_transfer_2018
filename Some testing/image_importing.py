# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 20:00:30 2018

@author: yam13
"""

import tensorflow as tf
from PIL import Image

image_size= 512
image = Image.open("content/023.jpg").resize((image_size, image_size))

#vgg = tf.keras.applications.VGG16
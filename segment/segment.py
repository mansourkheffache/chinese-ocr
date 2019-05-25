import numpy as np
import pandas as pd

from keras.preprocessing.image import load_img
from PIL import ImageOps

def gen_binarray(filename, proj_axis = 0, quantile = 0.8, invert = False):
    """Return binary array of projection axis"""

    img = load_img(filename)

    if invert:
        img = PIL.ImageOps.invert(img)
        quantile = 1 - quantile

    y = np.mean(image.img_to_array(img)/255, axis=2)
    y = np.mean(y, axis=proj_axis)

    print(f"Image size: {img.size}")
    width = img.size[0]

    m = pd.DataFrame(y).rolling(center = True, window=width//8).mean().fillna(method='ffill').fillna(method='bfill')
    M = pd.DataFrame(y).rolling(center = True, window=width).mean().fillna(method='ffill').fillna(method='bfill')

    y = m / M

    s = y > y.quantile(quantile)

    return s

def get_width(filename):
    """Returns estimate of character width"""

    s = gen_binarray(filename, proj_axis = 0, invert = True)

    widths = []
    count = 0
    flag = 0

    for val in s[0]:
        if val == 0:
            if flag == 1:
                widths.append(count)
                flag = 0
            count = 0
        elif val == 1:
            count += 1
            flag = 1

    if count > 0:
        widths.append(count)

    return np.max(widths)

from PIL import Image
import sys

inn = './in/'
out = './out/'

# Max size
ms = 96

def scale(filename):
    try:
        im = Image.open(inn + filename)
        w, h = im.size
        rr = min(ms/w, ms/h)

        w *= rr
        h *= rr
        s = (int(w), int(h))
        img = im.resize(s)

        img.save(out + filename)
    except Exception as e:
        print(e)
        print("sad life :/")

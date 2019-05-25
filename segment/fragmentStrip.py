#from PIL import Image
import PIL
from segment import *
from IPython.display import display, Image

def fragmentStrip(ImageJpg, savePath, quantile = 0.9):
    white = True;
    black = False;

    widthArray = gen_binarray(ImageJpg, proj_axis=0, quantile=quantile)
    heightArray = gen_binarray(ImageJpg, proj_axis=1, quantile=quantile)

    im = PIL.Image.open(ImageJpg)

    width, height = im.size
    divisor = 7
    #numberArray = [y%2 for y in range(divisor) for x in range(height//divisor)]
    numberArray = heightArray[0]
    #print(numberArray)
    i = 0

    widthStart = 5
    widthEnd = width - 5


    k = 0
    #while True:
    #    if(widthArray[k] == black):
    #        widthStart = k - 1
    #        break
    #    k += 1
    #    
    #while True:
    #    if(widthArray[k] == white):
    #        widthEnd = k
    #        break
    #    k += 1
    
    while True:
        if(i == len(numberArray)):
            break
        inc = True
        if(numberArray[i] == black):
            for j in range(i, len(numberArray)):
                if(numberArray[j] == white or j == len(numberArray) - 1):
                    crop(widthStart, i, widthEnd, j, savePath, ImageJpg)
                    i = j
                    break
        i += 1


def crop(startValueWidth, startValueHeight, endValueWidth, \
         endValueHeight, savePath, ImageJpg):
    if(startValueHeight == endValueHeight):
        return
    else:
        im = PIL.Image.open(ImageJpg)
        box = (startValueWidth, startValueHeight, endValueWidth, endValueHeight)
        try:
            a = im.crop(box)
            #a.save(savePath + ImageJpg[13:-4] + "_" +str(startValueHeight) \
            #+ "_" + str(endValueHeight) + ".jpg")
            display(a)
        except Exception as e:
            return


#fragmentStrip("./Task1/train/004708932_00055_l0.jpg", "./Result", 0, [])
        
    

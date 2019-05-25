from PIL import Image
import math

ImageArray = []
heightArray = []

def fragmentStrip(ImageJpg, savePath, widthArray, heightArray):
    white = 1;
    black = 0;
    
    im = Image.open(ImageJpg)

    width, height = im.size
    divisor = 7
    numberArray = [y%2 for y in range(divisor) for x in range(height//divisor)]
    print(numberArray)
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
    widthSize = widthEnd - widthStart
    print(widthSize, "widthSize")
    merge(widthSize, everyWord = True)


def crop(startValueWidth, startValueHeight, endValueWidth, \
         endValueHeight, savePath, ImageJpg):
    if(startValueHeight == endValueHeight):
        return
    else:
        im = Image.open(ImageJpg)
        box = (startValueWidth, startValueHeight, endValueWidth, endValueHeight)
        try:
            a = im.crop(box)
            #ImageArrayMetod(a)
            ImageArray.append(a)
            height_temp =  endValueHeight - startValueHeight
            heightArray.append(height_temp)
            #a.save(savePath + ImageJpg[13:-4] + "_" +str(startValueHeight) \
            #+ "_" + str(endValueHeight) + ".jpg")
            #a.show()
        except e:
            return

        

def merge(width, everyWord = False):
    if(everyWord == True):
        print("YAY")
        i = 0
        widthLow = width * 0.9
        widthHigh = width * 1.1
        print(widthLow, widthHigh, "low and high")
        while True:
            if(len(ImageArray) == i):
                return
            else:
                
                if(heightArray[i] > widthLow and heightArray[i] < widthHigh):
                    scale(ImageArray[i])
                else:
                    if(i == len(ImageArray) - 1):
                        scale(ImageArray[i])
                        print(True)
                    elif(heightArray[i] + heightArray[i+1] > widthLow and heightArray[i] + heightArray[i+1] < widthHigh):
                        scale(ImageArray[i])
                    else:
                        print(False)
                i += 1


fragmentStrip("./Task1/train/004708932_00055_l0.jpg", "./Result", 0, [])
        
    

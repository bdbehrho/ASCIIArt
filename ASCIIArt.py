__author__ = 'Brian'
from PIL import Image

img = Image.open("lena.jpg")
char_height = 8
char_width = 4
(width, height) = img.size
#letters = [' ',' ',' ',' ',' ', '`', '.', '-', 'i', 'l', ';', 'c', 'e', '&', 'N', '@', 'O', 'W']
letters = ['\'','-', '!','0', '%', '&']
brightnessFactor = 1
brightnesses = []
rotate = False

if rotate:
    temp = char_width
    char_width = char_height
    char_height = temp

def getBrightness(pixel):
    brightness = brightnessFactor * (.7*pixel[0] + .2*pixel[1] + .1*pixel[2])
    if brightness > 255:
        return 254
    else:
        return brightness

def getGrayScale(pos):
    sum = 0
    num_pixels = 0
    for i in range(pos[0]*char_width, pos[0]*char_width + char_width):
        for j in range(pos[1]*char_height, pos[1]*char_height + char_height):
            sum += getBrightness(img.getpixel((i,j)))
            num_pixels += 1

    return sum/num_pixels



for j in range(height/char_height):
    row = []
    for i in range(width/char_width):
        row.append(getGrayScale((i,j)))
    brightnesses.append(row)

if not rotate:
    for row in brightnesses:
        str = ""
        #print row
        for value in row:
            str += letters[len(letters) - 1 - int(value/255*len(letters))]
        print str
else:
    for i in range(len(brightnesses[0])):
        str = ""
        for j in range(len(brightnesses)):
             str += letters[len(letters) - 1 - int(brightnesses[j][i]/255*len(letters))]
        print str
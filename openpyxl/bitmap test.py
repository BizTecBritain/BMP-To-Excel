from bitmap2 import Image
 
with open('test.bmp','rb') as file:
    a = Image(file.read())
 
print('Width: ', a.getBitmapWidth())
print('Height: ', a.getBitmapHeight())

#print('Pixel RGB value at value X, Y:', [ord(c) for c in a.getPixels()[0][4]]) # Return the RGB value as a list (note that the first pixel starts on 0 and not 1)
print((a.getPixels()[0][4][0]))
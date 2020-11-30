"""
File: reflection_picture.py
This function will return an output 
image that is twice the height of the 
original. The top half will be identical 
to the original, and the bottom half 
should look like a reflection of the 
top half.
"""

# Pillow package have to be installed
from simpleimage import SimpleImage

DEFAULT_IMAGE = 'mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(DEFAULT_IMAGE)
    width = image.width
    height = image.height
    # new image mirrored
    mirror = SimpleImage.blank(width,height * 2)
    for x in range(width):
        for y in range(height):
            pixel = image.get_pixel(x,y)
            mirror.set_pixel(x,y,pixel)
            mirror.set_pixel(x,height*2 - (y+1),pixel)
    return mirror

def get_file():
    filename = input("Enter image name or press enter to continue with default: ")
    if filename == '':
        filename = DEFAULT_IMAGE
    return filename

def main():
    """
    This program tests your function by displaying
    the original image and the resulting image.
    """
    original = SimpleImage('mt-rainier.jpg')
    original.show()
    reflected = make_reflected('mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()

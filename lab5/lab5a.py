
import cv2 
import cvlib
import math
import numpy


def cvimg_to_list(img):
    """returns a list with the bgr values from the image"""
    
    return [tuple(int(value) for value in rgb) for hight in img for rgb in hight]


def the_math(x,y):
    """seperate function for the math part of unshrp_mask returns the result"""

    if x == 0 and y == 0:
        return 1.5
    
    return ((-1) / (2 * math.pi * (4.5 ** 2))) * math.e ** ((-1)*((x**2 + y**2)/(2*(4.5**2))))


def unsharp_mask(n):
    """creates a list with a matrix of the values from its index that is centered around (0,0)"""
    
    if n <= 0: 
        return None

    num = n//2
    if n % 2 == 0:
        seq = [[the_math(x,y) for x in range(-1 * num,num)] for y in range(-1 * num,num)]
    
    elif n % 2 == 1:
        seq = [[the_math(x,y) for x in range(-1 * num,num+1)] for y in range(-1 * num,num+1)]
        
    return numpy.array(seq)


def test5a1():
    """a simple function to store the example to run 5a1"""

    filename = 'flowers.png'
    img  = cv2.imread(filename)
    list_img = cvimg_to_list(img)

    # print(list_img[:10])

    converted_img = cvlib.rgblist_to_cvimg(list_img, img.shape[0],img.shape[1])

    cv2.imshow('Never gonna give you up', converted_img)
    cv2.waitKey(10000)


def test5a2():
    """a simple function to store the example to run 5a2"""

    print(unsharp_mask(3))
    #print(unsharp_mask())
    #print(unsharp_mask())

"""test5a1()
test5a2()"""

import cv2
import cvlib
import random
import lab5a
from inspect import isfunction

def pixel_constraint(hlow,hhigh,slow,shigh,vlow,vhigh):  # h = hue, s = saturation, v = value
    """will create a function identifing a limitation in the hsv color spectrum"""

    if hlow < 0: hlow = 0
    if hlow > 255: hlow = 255
    if hhigh < 0: hhigh = 0
    if hhigh > 255: hhigh = 255
    if slow < 0: slow = 0
    if slow > 255: slow = 255
    if shigh < 0: shigh = 0
    if shigh > 255: shigh = 255
    if vlow < 0: vlow = 0
    if vlow > 255: vlow = 255
    if vhigh < 0: vhigh = 0
    if vhigh > 255: vhigh = 255

    def func(values):
        """sends in a pixel in hsv format to check if it is part of the limitation. returns 0 or 1 to give white or black in later picture"""
        
        if type(values) != tuple:
            raise TypeError('pixel_constraint')

        elif len(values) != 3 or values[0] < 0 or values[1] < 0 or values[2] < 0:
            raise ValueError('pixel_constraint')

        else:
            for each in values:
                h = values[0]
                s = values[1]
                v = values[2]

                if h >= hlow and h <= hhigh and s >= slow and s <= shigh and v >= vlow and v <= vhigh:
                    return 1
                return 0

    return func


def gradient_condition(values):
    """returns a value between 0 and 1 instead of giving 0 or 1 to be able to create a gradiant"""

    if type(values) != tuple:
        raise TypeError('gradient_condition') 

    elif len(values) != 3 or values[0] < 0 or values[1] < 0 or values[2] < 0:
        raise ValueError('gradient_condition') # how it is supposed to be like.

    else:
        for each in values:

            if each == values[2]:
                return each / 255


def generator_from_image(orig_list):
    """uses the list of a picture to create a function that returns a pixel of that picture"""

    def generate(index):
        """checks for the index that is sent in and gives back the pixel of a picture that is in the same index"""

        if type(index) != int:
            raise TypeError('generator_from_image')
        
        elif index >= len(orig_list) or index < 0:
            raise IndexError('generator_from_image')
        
        else: 
            return orig_list[index]

    return generate


def combine_images(hsv_list , condition, generator1, generator2):
    """merges togheter 2 images that are sent in based on the hsv and condtion"""

    complete_img = []

    try:

        if type(hsv_list) != list:
            raise TypeError('hsv_list, combine_images')
        
        if not isfunction(condition):
            raise TypeError('condition, combine_images')
        
        if not isfunction(generator1):
            raise TypeError('generator1, combine_images')
            
        if not isfunction(generator2):
            raise TypeError('generator2, combine_images')

    
        for i, each in enumerate(hsv_list):

            mult = float(condition(each))

            pixel1 = generator1(i)
            pixel2 = generator2(i)

            values = tuple(int(pixel1[j] * mult + pixel2[j] * (1 - mult)) for j in range(3))

            complete_img.append(values)

    except ValueError as e: 
        print("Value Error: ", e) 
        return None
    except IndexError as e:
        print("Index Error: ", e) 
        return None
    except TypeError as e:
        print("Type Error: ", e)
        return None

    return complete_img


def test5b1():
    """a simple function to store the example to run 5b1"""

    hsv_plane = cv2.cvtColor(cv2.imread("plane.png"), cv2.COLOR_BGR2HSV)
    plane_list = lab5a.cvimg_to_list(hsv_plane)

    is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
    sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

    cv2.imshow('sky', cvlib.greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
    cv2.waitKey(10000)


def test5b2():
    """a simple function to store the example to run 5b2"""

    orig_img = cv2.imread("plane.png")
    orig_list = lab5a.cvimg_to_list(orig_img)

    generator = generator_from_image(orig_list)

    new_list = [generator(i) for i in range(len(orig_list))]

    cv2.imshow('original', orig_img)
    cv2.imshow('new', cvlib.rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
    cv2.waitKey(10000)


def test5b3():
    """a simple function to store the example to run 5b3"""

    filename = "plane.png"
    img = cv2.imread("plane.png")
    img_list = lab5a.cvimg_to_list(img)

    hsv_img = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2HSV)
    hsv_list = lab5a.cvimg_to_list(hsv_img)

    condition = pixel_constraint(100, 150, 50, 200, 100, 255)

    night_sky = [(255,255,255) if random.random() > 0.99 else (0,0,0) for i in range(hsv_img.size)]
    generator1 = generator_from_image(night_sky)

    generator2 = generator_from_image(img_list)

    complete = combine_images(hsv_list, condition, generator1, generator2)
    # complete_img = cvlib.rgblist_to_cvimg(complete, hsv_img.shape[0], hsv_img.shape[1])

    cv2.imshow('Completed', cvlib.rgblist_to_cvimg(complete, hsv_img.shape[0], hsv_img.shape[1]))
    cv2.waitKey(10000)


def test5b4():
    """a simple function to store the example to run 5b4"""

    file1 = "plane.png"
    file2 = "flowers.png"

    img1 = cv2.imread(file1)
    img2 = cv2.imread(file2)

    img1_list = lab5a.cvimg_to_list(img1)
    img2_list = lab5a.cvimg_to_list(img2)

    gradient = cv2.imread("gradient.png")
    gradient_list = lab5a.cvimg_to_list(gradient)

    generator1 = generator_from_image(img1_list)
    generator2 = generator_from_image(img2_list)

    complete = combine_images(gradient_list, gradient_condition, generator1, generator2)
    print(len(complete))

    cv2.imshow('Completed', cvlib.rgblist_to_cvimg(complete, img1.shape[0], img1.shape[1]))
    cv2.waitKey(10000)


"""test5b1()
test5b2()
test5b3()
test5b4()"""
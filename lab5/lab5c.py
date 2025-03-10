import lab5a
import lab5b
import cv2
import cvlib
import os



def test_cvimg_to_list():
    """tests the cvimg_to_list function for multiple images"""

    if os.name == 'nt': # in case of windows
        assert len(lab5a.cvimg_to_list(cv2.imread("Testing Files\penguin.png"))) == 2120,'cvimg_to_list error in case 1'
    else:                # in case of Linux
        assert len(lab5a.cvimg_to_list(cv2.imread("Testing Files/penguin.png"))) == 2120, 'cvimg_to_list error in case 1'
    
    test_img = [[(0,0,255),(0,255,0)],[(255,0,0),(255,0,255)]]

    assert len(lab5a.cvimg_to_list(test_img)) == 4, 'cvimg_to_list error in case 2'
    assert lab5a.cvimg_to_list(test_img)[2] == (255,0,0), 'cvimg_to_list error in case 3'
    assert lab5a.cvimg_to_list(test_img)[-1] == (255,0,255), 'cvimg_to_list error in case 4'

    print('')
    print('cvimg_to_list completed')
    print('')
    print('-----------------------------')


def test_unsharp_mask():
    """tests the unsharp_mask function for multiple values"""

    assert lab5a.unsharp_mask(1)[0][0] == 1.5, 'unsharp_mask error in case 1'
    assert lab5a.unsharp_mask(3)[0][0] == -0.007480807217716918, 'unsharp_mask error in case 2'
    assert lab5a.unsharp_mask(0) == None, 'unsharp_mask error in case 3'
    assert lab5a.unsharp_mask(-2) == None, 'unsharp_mask error in case 4'

    print('')
    print('unsharp_mask completed')
    print('')
    print('-----------------------------')


def test_pixel_constraint():
    """tests the pixel_constraint function with a simple 5x5 picture"""

    #test_img = [[(0,0,255),(255,0,0)],[(255,0,0),(0,0,255)]]

    if os.name == 'nt':
        test_img = cv2.imread("Testing Files\small guy.png")
    else:
        test_img = cv2.imread("Testing Files/small guy.png")

    test_list = lab5a.cvimg_to_list(test_img)
    #cv2.imwrite('lab5/Testing files/test_img.jpg', test_img)
    #print(test_list)

    hsv_test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2HSV)
    hsv_test_list = lab5a.cvimg_to_list(hsv_test_img)
    # print(hsv_test_list)

    blue = lab5b.pixel_constraint(90,100,240,256,230,256)
    blue_list = [blue(value) for value in hsv_test_list]

    red = lab5b.pixel_constraint(170,180,200,255,230,255)
    red_list = [red(value) for value in hsv_test_list]

    # -------------------------------------------------

    edge = lab5b.pixel_constraint(0,255,0,255,0,255)
    edge_list = []
    edge_list.append((0,0,0))
    edge_list.append((255,255,255))
    edge_list.append((-1,-1,-1))
    edge_list.append((1,1))
    edge_list.append([1,1,1])
    edge_list.append((256,256,256))

    pixel_constraint_typeerror = []
    pixel_constraint_valueerror = []
    
    for i in range(len(edge_list)):
        
        try:
            if i == 0: edge_img = [edge(edge_list[0])]
            if i == 1: edge_img = [edge(edge_list[1])]
            if i == 2: 
                edge_img = [edge(edge_list[2])]
                print('There should be an error here 1 but there is not')
            if i == 3: 
                edge_img = [edge(edge_list[3])]
                print('There should be an error here 2 but there is not')
            if i == 4: 
                edge_img = [edge(edge_list[4])]
                print('there should be an error here 3 but there is not')
            if i == 5: 
                edge_img = [edge(edge_list[4])]
                print('there should be an error here 4 but there is not')

        except TypeError:
            pixel_constraint_typeerror.append(f'True [{i}]')
            pass
        except ValueError:
            pixel_constraint_valueerror.append(f'True [{i}]')
            pass

    # -------------------------------------------------

    assert blue_list == [1 if i == 7 or i == 8 else 0 for i in range(len(blue_list))], 'pixel_constraint error in case 1'
    assert red_list == [0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,0], 'pixel_constraint error in case 2'
    assert red_list != [0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1], 'pixel_constraint error in case 3' # should not return this list

    # print('')                        for visualizing the lists
    # print('blue list')
    # for i in range (5):
    #     print(blue_list[i*5: i*5+5])

    # print('red list')
    # for i in range (5):
    #     print(red_list[i*5: i*5+5])

    print('type: ',pixel_constraint_typeerror)
    print('value: ',pixel_constraint_valueerror)

    print('')
    print('pixel_constraint completed')
    print('')
    print('-----------------------------')


def test_generator_from_image():
    """tests the pixel_constraint function with a simple 5x5 picture"""

    if os.name == 'nt':
        test_img = cv2.imread("Testing Files\small guy.png")
    else:
        test_img = cv2.imread("Testing Files/small guy.png")

    test_list = lab5a.cvimg_to_list(test_img)

    generator = lab5b.generator_from_image(test_list)

    assert generator(1) == (36,28,237), 'generator_from_image error in case 1'
    assert generator(7) == (232,162,0), 'generator_from_image error in case 2'
    assert generator(24) == (255,255,255), 'generator_from_image error in case 3'

    # ---------------------------------------------

    generator_from_image_typeerror = []
    generator_from_image_indexerror = []

    try:
        if generator(25) != None: print('generator_from_image error in case 4')
        """except TypeError:
        generator_from_image_typeerror.append(True)
        pass"""
    except IndexError:
        generator_from_image_indexerror.append(True)
        pass

    try:
        if generator((20,20)) != None: print('generator_from_image error in case 5')
    except TypeError:
        generator_from_image_typeerror.append(True)
        pass
        """except IndexError:
        generator_from_image_indexerror.append(True)
        pass"""

    # ---------------------------------------------

    print('type: ',generator_from_image_typeerror)
    print('index: ',generator_from_image_indexerror)

    print('')
    print('generator_from_image completed')
    print('')
    print('-----------------------------')
    

def test_combine_image():
    """tests the combine_image function with two simple 5x5 picture and gradient, white and black, condition based on one picture"""
    
    if os.name == 'nt':
        test_img1 = cv2.imread("Testing Files\guy.png")
        test_img2 = cv2.imread("Testing Files\guy blue.png")
        hsv_img1 = cv2.imread("Testing Files\some block.png")
        hsv_img2 = cv2.imread("Testing Files\gradient blocky.png")

    else:
        test_img1 = cv2.imread("Testing Files/guy.png")
        test_img2 = cv2.imread("Testing Files/guy blue.png")
        hsv_img1 = cv2.imread("Testing Files/some block.png")
        hsv_img2 = cv2.imread("Testing Files/gradient blocky.png")


    hsv_img1 = cv2.cvtColor(hsv_img1, cv2.COLOR_BGR2HSV)
    hsv_img2 = cv2.cvtColor(hsv_img2, cv2.COLOR_BGR2HSV)
    hsv_img3 = cv2.cvtColor(test_img1, cv2.COLOR_BGR2HSV)

    test_list1 = lab5a.cvimg_to_list(test_img1)
    test_list2 = lab5a.cvimg_to_list(test_img2)

    hsv_list1 = lab5a.cvimg_to_list(hsv_img1)
    hsv_list2 = lab5a.cvimg_to_list(hsv_img2)
    hsv_list3 = lab5a.cvimg_to_list(hsv_img3)

    generator1 = lab5b.generator_from_image(test_list1)
    generator2 = lab5b.generator_from_image(test_list2)
    green_generator = lab5b.generator_from_image([(0,255,0) for i in range(125*125)])
    
    red_const = lab5b.pixel_constraint(170,180,200,255,230,255)
    white_const = lab5b.pixel_constraint(0,180,0,0,255,255)
    graidient = lab5b.gradient_condition

    combined1 = lab5b.combine_images(hsv_list1, white_const,generator1,generator2)
    combined2 = lab5b.combine_images(hsv_list2, graidient, generator2, generator1)
    combined3 = lab5b.combine_images(hsv_list3, red_const, green_generator, generator1)


    # should give a bunch of errors ---------------------

    hsv_error1 = [(0,0,-255),[100,200,255],(-10,30,-40)] 
    hsv_error2 = [[0,0,255],[100,200,255],(-10,30,-40)] 
    test_list_error1 = [[20,30,180],(20,90),(0,0,0)] 
    test_list_error2 = [(20,30,180),(-20,200,90),(0,0,0)] 
    test_edge = lab5b.pixel_constraint(-2,255,0,400,350,255)
    test_generator1 = lab5b.generator_from_image(test_list_error1)
    test_generator2 = lab5b.generator_from_image(test_list_error2)

    combined_error1 = lab5b.combine_images(hsv_error1, test_edge, generator1, generator2) # trigger hsv_list Value error
    combined_error2 = lab5b.combine_images(hsv_error2, test_edge, test_generator1, generator2) # trigger generator Type error
    combined_error3 = lab5b.combine_images(hsv_list1, test_edge, generator1, test_generator2) # trigger generator Index error

    # ---------------------------------------------------

    assert combined1[50] == (156,55,48), 'combine_images error case 1'
    assert combined1[8175] == (36,28,237), 'combine_images error case 2'
    assert len(combined2) == len(test_list2), 'combine_images error case 3'
    # testa att innre funktioner kastar rätt
    
    
    cv2.imshow('combinerad', cvlib.rgblist_to_cvimg(combined1, test_img1.shape[0], test_img1.shape[1])) 
    cv2.waitKey(0)
    cv2.imshow('combinerad', cvlib.rgblist_to_cvimg(combined2, test_img1.shape[0], test_img1.shape[1]))
    cv2.waitKey(0)
    cv2.imshow('combinerad', cvlib.rgblist_to_cvimg(combined3, test_img1.shape[0], test_img1.shape[1]))
    cv2.waitKey(0)
    # cv2.imshow('combinerad', cvlib.rgblist_to_cvimg(combined_error, test_img1.shape[0], test_img1.shape[1]))
    # cv2.waitKey(0)

    print('')
    print('combine_image completed')
    print('')
    print('-----------------------------')


"""test_cvimg_to_list()
test_unsharp_mask()
test_pixel_constraint()
test_generator_from_image()
test_combine_image()"""
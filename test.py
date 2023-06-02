# import camera
# sizes = camera.image_sizes()
# appuifw.app.orientation = 'landscape'
# canvas = appuifw.Canvas()
#
# def cam_finder(im):
#     canvas.blit(im)
# camera.start_finder(cam_finder, size=(320,240))
# canvas.bind(key_codes.EKeySelect, take_picture)
# pic.save(filename, quality=75)
#
# import math
# x0 = ...
# y0 = ...
# r = ...
# xx = x0 + r + r
# yy = y0
# dt = 0.5 / r
# t = 0.0
# while t < 2.0 * math.pi:
#     x = x0 + int(r * math.cos(t))
#     y = y0 + int(r * math.sin(t))
#     if (xx != x) and (yy != y):
#         xx = x
#         yy = y
#     t += dt
#
#
# gray = 0.114 * b + 0.587 * g + 0.299 * r
# gray = gray.astype(np.uint8)
# cv2.imshow("gray", gray)
#
# cvtColor(median * 0.6, gray, COLOR_BGR2GRAY)
#
# Canny(gray, canny, 100, 400)
# cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
#
# import numpy as np
# import cv2 as cv
# img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)
# assert img is not None, "file could not be read, check with os.path.exists()"
# # create a CLAHE object (Arguments are optional).
# clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cl1 = clahe.apply(img)
# cv.imwrite('image2.jpg',cl1)
#
# img = cv.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
#
# from PIL import Image
# img = Image.open('image1.jpg')
# img_crop_outside = img.crop((100, 175, 300, 250))
# img_crop_outside.save('image2.jpg', quality=95)
#
#
# import torch
# from haar_pytorch import HaarForward, HaarInverse
#
# haar = HaarForward()
# ihaar = HaarInverse()
#
# img = torch.randn(5, 4, 64, 64)
# wavelets = haar(img)
# img_reconstructed = ihaar(wavelets)
#
# from scipy.ndimage import zoom
# from PIL import Image
# import numpy as np
#
# srcImage = Image.open("image_in_binary_color.jpg")
# grayImage = srcImage.convert('L')
# array = np.array(grayImage)
# array = zoom(array, 310/174)
#
# np.savetxt("binarized.txt", array<128, fmt="%d")
# print("\n\n Output Stored to binarized.txt.......#").
#
# from scipy.spatial.distance import hamming
#
# array1 = (1011101101010, 10111011110)
# array2 = (1010110110100, 10111011110)
# x = list(str(array1[1]))
# y = list(str(array2[1]))
# print(x)
# print(y)
# print(1 - hamming(x, y))

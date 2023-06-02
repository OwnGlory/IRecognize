import cv2
# import numpy as np


url = "10.16.204.68:8080/video"
cp = cv2.VideoCapture(url)

while (True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
        cv2.imwrite("img1.png", camera[1])
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()

# cam = cv2.VideoCapture(0)
# image = cam.read()
# cv2.imshow("img1", image[1])
# cv2.imwrite("img1.png", image[1])
# cv2.waitKey(0)
# 
# 
# sizes = camera.image_sizes()
# appuifw.app.orientation = 'landscape'
# canvas = appuifw.Canvas()
# 
# 
# def cam_finder(im):
#     canvas.blit(im)
# 
# 
# camera.start_finder(cam_finder, size=(320,240))
# canvas.bind(key_codes.EKeySelect, take_picture)
# pic.save(filename, quality=75)

# import cv2
# img = cv2.imread("iris.jpg", cv2.IMREAD_GRAYSCALE)
#
# print("Высота:"+str(img.shape[0]))
# print("Ширина:" + str(img.shape[1]))
# res_img_area = cv2.resize(img, (int(img.shape[1] / 1.4),
# int(img.shape[0] / 1.4)), cv2.INTER_AREA)
# print("Высота:"+str(res_img_area.shape[0]))
# print("Ширина:" + str(res_img_area.shape[1]))
#
# img_b_5 = cv2.blur(res_img_area, (5, 5))
# img_b_7 = cv2.blur(res_img_area, (7, 7))
# img_b_11 = cv2.blur(res_img_area, (11, 11))
#
# img_g_7 = cv2.GaussianBlur(res_img_area, (7, 7), 0)
# img_g_11 = cv2.GaussianBlur(res_img_area, (11, 11), 0)
# img_g_15 = cv2.GaussianBlur(res_img_area, (15, 15), 0)
#
# img_m_5 = cv2.medianBlur(res_img_area, 5)
# img_m_7 = cv2.medianBlur(res_img_area, 7)
# img_m_11 = cv2.medianBlur(res_img_area, 11)
# img_m_15 = cv2.medianBlur(res_img_area, 15)
# img_m_25 = cv2.medianBlur(res_img_area, 25)
# img_m_29 = cv2.medianBlur(res_img_area, 29)
#
#
#
#
# imgC = cv2.Canny(img_m_29,10,10)
# #img2 = cv2.threshold(imgC, 10, 255, cv2.THRESH_BINARY)
# cv2.imshow('Image1',res_img_area)
# cv2.imshow("Image2",img_m_29)
# cv2.waitKey(0)

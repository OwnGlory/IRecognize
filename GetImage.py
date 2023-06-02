import cv2
cam = cv2.VideoCapture(0)
image = cam.read()
cv2.imshow("img1", image[1])
cv2.imwrite("img1.png", image[1])
cv2.waitKey(0)

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

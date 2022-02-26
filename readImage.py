import cv2
image = cv2.imread('Assests/road.jpg')
h, w = image.shape[:2]
print("height = {}, width = {}".format(h,w))
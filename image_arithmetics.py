import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#=======================doesnot work=============================
# filename1 = 'Assests/water.jpg'
# filename2 = 'Assests/horse.jpeg'

# image1 = cv2.imread(filename1, 1)
# image2 = cv2.imread(filename2, 1)

# weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

# cv2.imshow('Weighted Image - Addition', weightedSum)
# cv2.waitKey(0)
# if (cv2.waitKey(0) & 0xff == 27):
#     cv2.destroyAllWindows()




img_water = mpimg.imread('Assests/water.jpeg')
resized = cv2.resize(img_water, (300,300))
plt.imshow(resized)
plt.title('water image')
plt.show()
print("part 1 ")

img_horse = mpimg.imread('Assests/horse.jpeg')
resized2 = cv2.resize(img_horse, (300,300))
plt.imshow(resized2)
plt.title('horse image')
plt.show()
print("part 2")

blend1 = cv2.addWeighted(resized, 0.5, resized2, 0.8, 0)
plt.imshow(blend1)
plt.title('blended image - addition')
plt.show()


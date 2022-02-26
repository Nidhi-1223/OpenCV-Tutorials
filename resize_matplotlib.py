import cv2
import numpy as np
import matplotlib.pyplot as plt

filename = 'Assests/road.jpg'
image = cv2.imread(filename, 1)
half = cv2.resize(image, (0,0), fx= 0.1, fy= 0.1)
bigger = cv2.resize(image, (1050, 1610))
stretch_near = cv2.resize(image, (780, 540), interpolation= cv2.INTER_NEAREST)

Titles = ["Original", "half", "bigger", "Interpolation nearest"]
images_list =  [image, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2,2,i+1)
    plt.title(Titles[i])
    plt.imshow(images_list[i])

plt.show()
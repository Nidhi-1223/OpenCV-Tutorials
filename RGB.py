import cv2
image = cv2.imread('Assests/road.jpg')
(B, G, R) = image[200,200]
print("R = {}, G = {}, B = {} \n".format(R,G,B))

# #we can also pass the channel to extract the value for a specific channel
# B = image[100,100,0]
# print("B = {}".format(B))




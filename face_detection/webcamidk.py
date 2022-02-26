import cv2
from skimage import io
url = 'http://192.168.43.91/capture'

while(True):
    img = io.imread(url)
    cv2.imshow("Webcam", img)
    key = cv2.waitKey(20)
    print(key)
    if(key == ord('q')):
        break
    

cv2.destroyAllWindows()
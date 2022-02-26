import cv2
camera = cv2.VideoCapture(0)
while(True):
    ret, img = camera.read()
    if(ret == True):
        cv2.imshow("Webcam", img)
        key = cv2.waitKey(20)
        print(key)
        if(key == ord('q')):
            break
    else:
        break
camera.release()
cv2.destroyAllWindows()

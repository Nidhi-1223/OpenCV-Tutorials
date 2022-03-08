import cv2
capture = cv2.VideoCapture(0)
while(True):
    ret, img = capture.read()
    if(ret == True):
        cv2.imshow("video_steam", img)
        key = cv2.waitKey(100)
        print(key)
        
        if(key == ord('q')):     #if (key == 113)       its gonna quit when we press "q"
            break
        
    else:
        break

capture.release()
cv2.destroyAllWindows()
import cv2
filename = 'Assests/sample_video.mp4'
video_stream = cv2.VideoCapture(filename)

while(True):
    ret, img = video_stream.read()
    if(ret == True):
        cv2.imshow("video_steam", img)
        key = cv2.waitKey(100)
        print(key)
        
        if(key == ord('q')):     #if (key == 113)       its gonna quit when we press "q"
            break
        
    else:
        break


cv2.destroyAllWindows()

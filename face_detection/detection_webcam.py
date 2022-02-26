import cv2
import sys

xml_path = 'face_detection/face_train.xml'
faceCascade = cv2.CascadeClassifier(xml_path)
video_capture = cv2.VideoCapture(0)

while(True):
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
    scaleFactor= 1.1,
    minNeighbors=5,
    minSize= (30,30)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(255, 0, 0),2 )
    cv2.imshow('Video', frame)
    key = cv2.waitKey(20)
    if (key == ord('q')):
        break

video_capture.release()
cv2.destroyAllWindows()
    
        
    
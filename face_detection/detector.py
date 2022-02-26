import cv2
img_path = 'face_detection/Leclerc.png'
xml_path = 'face_detection/face_train.xml'

img = cv2.imread(img_path, 0)

face_detector = cv2.CascadeClassifier(xml_path)

faces = face_detector.detectMultiScale(img, scaleFactor=2)

for face in faces:
    top_left_x = face[0]
    top_left_y = face[1]
    width = face[2]
    height = face[3]

    bottom_right_x = top_left_x + width
    bottom_right_y = top_left_y + height

    cv2.rectangle(img,                                      #image or the object
                    (top_left_x, top_left_y),               #top corner co-ordinates
                    (bottom_right_x, bottom_right_y),       #bottom corner co-ordinates
                    (255, 0, 0),                            #rgb value of rectgangle
                    2)                                      #width of the rectangle
cv2.imshow("Faces", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
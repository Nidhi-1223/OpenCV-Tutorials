import cv2
from skimage import io
img_path = 'face_detection/Leclerc.png'
xml_path = 'face_detection/face_train.xml'
eyes_xml_path = 'face_detection/eye_train.xml'
face_detector = cv2.CascadeClassifier(xml_path)
eyes_detector = cv2.CascadeClassifier(eyes_xml_path)

url = 'http://192.168.43.91/capture'        #change everytime you connect to hotspot and run that arduino file

while(True):
    img = io.imread(url)
    faces = face_detector.detectMultiScale(img, scaleFactor=2)
    eyes = eyes_detector.detectMultiScale(img, scaleFactor=1.2)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
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


    for eye in eyes:
        top_left_x = eye[0]
        top_left_y = eye[1]
        width = eye[2]
        height = eye[3]

        bottom_right_x = top_left_x + width
        bottom_right_y = top_left_y + height

        cv2.rectangle(img,                                      #image or the object
                        (top_left_x, top_left_y),               #top corner co-ordinates
                        (bottom_right_x, bottom_right_y),       #bottom corner co-ordinates
                        (0, 0, 225),                            #rgb value of rectgangle
                        2)                                      #width of the rectangle
    cv2.imshow("Faces and eyes", img)
    key = cv2.waitKey(20)
    if (key == ord('q')):
        break

cv2.destroyAllWindows()
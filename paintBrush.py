import cv2
mouse_events = [j for j in dir(cv2) if 'EVENT' in j]
print(mouse_events )
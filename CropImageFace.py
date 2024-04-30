import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('C:/Users/flori/Desktop/DataSetVideo/Fake/id34_id31_0002_frameV2250.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 8)
os.makedirs('visages_recadres', exist_ok=True)

for i, (x, y, w, h) in enumerate(faces):
    roi_color = img[y:y+h, x:x+w]
    cv2.imwrite(f'ImagesVideo/visage_{i}.jpg', roi_color)

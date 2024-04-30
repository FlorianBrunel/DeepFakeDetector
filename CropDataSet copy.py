import os
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def crop_face(img_path, output_folder):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Increase scaleFactor and minNeighbors
    if len(faces) == 1:  # If exactly one face is detected
        (x, y, w, h) = faces[0]  # Only take the first face
        face = img[y:y + h, x:x + w]
        cv2.imwrite(f"{output_folder}/{os.path.basename(img_path)}", face)
        os.remove(img_path)  # Only remove the image if it has been cropped successfully

dataset_folder = "C:/Users/flori/Desktop/DataSet"
new_dataset_folder = "C:/Users/flori/Desktop/NewDataSet"

for folder in ['Test', 'Train', 'Validation']:
    for subfolder in ['Fake', 'Real']:
        image_folder = os.path.join(dataset_folder, folder, subfolder)
        face_folder = os.path.join(new_dataset_folder, folder, subfolder)
        os.makedirs(face_folder, exist_ok=True)
        for filename in os.listdir(image_folder):
            crop_face(os.path.join(image_folder, filename), face_folder)
            print(filename)
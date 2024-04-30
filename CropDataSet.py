import os
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def crop_face(img_path, output_folder):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Increase scaleFactor and minNeighbors
    if len(faces) > 0:  # If at least one face is detected
        (x, y, w, h) = faces[0]  # Only take the first face
        face = img[y:y + h, x:x + w]
        cv2.imwrite(f"{output_folder}/{os.path.basename(img_path)}", face)
    os.remove(img_path)

def extract_frames(video_path, output_folder, frame_interval):
    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == False:
            break
        if count % frame_interval == 0:
            cv2.imwrite(f"{output_folder}/{os.path.basename(video_path)}_frame{count}.jpg", frame)
        count += 1
    cap.release()

video_folder = "C:/Users/flori/Desktop/Celeb-synthesis"
frame_folder = "C:/Users/flori/Desktop/FrameFake"
face_folder = "C:/Users/flori/Desktop/FaceFake"

os.makedirs(frame_folder, exist_ok=True)
os.makedirs(face_folder, exist_ok=True)

for filename in os.listdir(video_folder):
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        extract_frames(os.path.join(video_folder, filename), frame_folder, 10)
print("Fin frames")
for filename in os.listdir(frame_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        crop_face(os.path.join(frame_folder, filename), face_folder)
print("Fin CROP ---------------------------------------------------------------------------------")
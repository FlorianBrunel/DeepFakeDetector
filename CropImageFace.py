import cv2
import os

<<<<<<< HEAD
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('C:/Users/flori/Desktop/DataSetVideo/Fake/id34_id31_0002_frameV2250.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 8)
os.makedirs('visages_recadres', exist_ok=True)

for i, (x, y, w, h) in enumerate(faces):
    roi_color = img[y:y+h, x:x+w]
    cv2.imwrite(f'ImagesVideo/visage_{i}.jpg', roi_color)
=======
# Charger le modèle de détection de visage
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Charger l'image
img = cv2.imread('C:/Users/flori/Desktop/DataSetVideo/Fake/id34_id31_0002_frameV2250.jpg')

# Convertir en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Détecter les visages
faces = face_cascade.detectMultiScale(gray, 1.1, 8)

# Créer un dossier pour stocker les images recadrées
os.makedirs('visages_recadres', exist_ok=True)

# Boucle sur les visages détectés
for i, (x, y, w, h) in enumerate(faces):
    # Recadrer l'image sur le visage
    roi_color = img[y:y+h, x:x+w]
    # Enregistrer l'image recadrée
    cv2.imwrite(f'visages_recadres/visage_{i}.jpg', roi_color)

print("Les images recadrées ont été enregistrées dans le dossier 'visages_recadres'.")
>>>>>>> 13f9f409407b7bc05fb2093d4f20b542604c5c7c

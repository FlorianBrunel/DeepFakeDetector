import os
import cv2
import tkinter as tk
from tkinter import filedialog

def lister_chemins_dossier(dossier):
    print("Test")
    for chemin, dossiers, fichiers in os.walk(dossier):
        for fichier in fichiers:
            yield os.path.join(chemin, fichier)

def decomposer_video_en_images(chemin_video, dossier_sortie):
    video = cv2.VideoCapture(chemin_video)
    succes, image = video.read()
    compteur = 0
    while succes:
        cv2.imwrite(os.path.join(dossier_sortie, "frame%d.jpg" % compteur), image)
        succes, image = video.read()
        compteur += 1

print("Test")
root = tk.Tk()
root.withdraw()

dossier = filedialog.askdirectory()  # Demande à l'utilisateur de sélectionner un dossier

for chemin_fichier in lister_chemins_dossier(dossier):
    if chemin_fichier.endswith(('.mp4', '.avi', '.mov')):  # Ajoutez d'autres extensions de vidéo si nécessaire
        dossier_sortie = os.path.join(os.path.dirname(chemin_fichier), os.path.basename(chemin_fichier) + "_frames")
        os.makedirs(dossier_sortie, exist_ok=True)
        decomposer_video_en_images(chemin_fichier, dossier_sortie)
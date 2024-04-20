import os
import cv2
import tkinter as tk
from tkinter import filedialog

def lister_chemins_dossier(dossier):
    for chemin, dossiers, fichiers in os.walk(dossier):
        for fichier in fichiers:
            yield os.path.join(chemin, fichier)

def decomposer_video_en_images(chemin_video, dossier_sortie):
    video = cv2.VideoCapture(chemin_video)
    succes, image = video.read()
    compteur = 0
    nom_video = os.path.basename(chemin_video).split('.')[0]  # Ajouté
    while succes:
        cv2.imwrite(os.path.join(dossier_sortie, f"{nom_video}_frameV2{compteur}.jpg"), image)  # Modifié
        succes, image = video.read()
        compteur += 1

root = tk.Tk()
root.withdraw()

dossier = filedialog.askdirectory()  # Demande à l'utilisateur de sélectionner un dossier

for chemin_fichier in lister_chemins_dossier(dossier):
    if chemin_fichier.endswith(('.mp4', '.avi', '.mov')):  # Ajoutez d'autres extensions de vidéo si nécessaire
        dossier_sortie = "DataSetVideo/Fake"
        os.makedirs(dossier_sortie, exist_ok=True)
        decomposer_video_en_images(chemin_fichier, dossier_sortie)
        print("En cours")

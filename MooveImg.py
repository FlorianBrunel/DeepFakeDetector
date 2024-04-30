import os
import shutil

def deplacer_images(dossier_source, dossier_destination, nombre_images):
    fichiers = os.listdir(dossier_source)
    fichiers.sort()
    fichiers = fichiers[:nombre_images]

    for fichier in fichiers:
        if fichier.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            chemin_complet = os.path.join(dossier_source, fichier)
            shutil.move(chemin_complet, dossier_destination)

deplacer_images('C:/Users/flori/Desktop/FaceFake', 'C:/Users/flori/Desktop/Test/Fake', 5205)

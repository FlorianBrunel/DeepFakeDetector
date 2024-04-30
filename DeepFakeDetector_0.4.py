from keras.layers import TFSMLayer
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import tensorflow as tf
import os
import cv2
# https://www.youtube.com/watch?v=S3qftloOO4U

model = TFSMLayer('Model\ModelNewDataSet20E200B2C', call_endpoint='serving_default')

FilePathTest = ""
ImageToAnalys = ""

# Définition des fonctions --------------------------------------------------------------------------------------------------------------------------------------------

def OpenFilePathTest():
     
    global FilePathTest 
    FilePathTest = filedialog.askopenfilename()
    extension = check_extension(FilePathTest)
    if (extension == ".jpg" or extension == ".png" or extension == ".jpeg"):
        UpdateImage(FilePathTest)
    


def RouterModel(FilePathTest):
    
    extension = check_extension(FilePathTest)
    if (FilePathTest == ""):
        WarningUser()

    elif (extension == ".jpg" or extension == ".png" or extension == ".jpeg"):
        ImageAnalyse(FilePathTest)
    elif (extension == ".mp4"):
        VideoAnalyse(FilePathTest)


def check_extension(FilePathTest):
    _, extension = os.path.splitext(FilePathTest)
    return extension


def ImageAnalyse(FilePathTest):
    UpdateImage(FilePathTest)
    LunchAnalyze(FilePathTest)


def VideoAnalyse(FilePathTest):
    cap = cv2.VideoCapture(FilePathTest)
    count = 0
    Sum_RateBool = [0, 0]

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == False:
            break
        image_path = 'ImagesVideo/VideoFrame'+str(count)+'.jpg'
        cv2.imwrite(image_path, frame)

        if (count == 0) :
            UpdateImage(image_path)

        Sum_RateBool += LunchAnalyze(image_path)
        count += 1
    cap.release()
    DestroyContent(count)

    ReturnAnalyseVideo(Sum_RateBool, count)
    return count




def LunchAnalyze(FilePathTest):
    
    global ImgToAnalys 
    ImgToAnalys = Image.open(FilePathTest)
    
    ImgToAnalys = ImgToAnalys.resize((200, 200))
    ImgToAnalysArray = np.array(ImgToAnalys)
    ImgToAnalysArray = np.expand_dims(ImgToAnalysArray, axis=0)
    predictions = model(ImgToAnalysArray)
    Rates = predictions['output_0'].numpy()[0]

    RateFake = Rates[0]
    RateReal = Rates[1]

    print(RateFake)
    print(RateReal)
    
    return RateFake, RateReal


def ResultAnalyseImage(RateFake, RateReal):
    if RateFake < RateReal :
        TrueRate = round(100*RateReal)
        LabelReturn.config(text = "IMAGE REELLE A " + str(TrueRate) + " %." , fg = "Green" )

        
    else :
        TrueRate = round(100*RateFake)
        LabelReturn.config(text = "IMAGE FAUSSE A " + str(TrueRate) + " %.", fg = "Red" )


def UpdateImage(FilePathTest):
    global tk_ImgToAnalys
    ImgToAnalys = Image.open(FilePathTest)
    ImgToAnalys = ImgToAnalys.resize((700, 700)) 
    tk_ImgToAnalys = ImageTk.PhotoImage(ImgToAnalys)
    LabelImageFrame.config(image=tk_ImgToAnalys)
    LabelImageFrame.image = tk_ImgToAnalys


def DestroyContent(count):
    for i in range(count):
        image_path = 'ImagesVideo/VideoFrame'+str(i)+'.jpg'
        os.remove(image_path)
    return count

def ReturnAnalyseVideo(Sum_RateBool, count):
    print(Sum_RateBool)
    print(count)
    average_RateBool = Sum_RateBool / count
    if (Sum_RateBool < count/2) :
        LabelReturn.config(text = "VIDEO FAUSSE A " + str(100 - 100 * Sum_RateBool) + " %." , fg = "Green" )
    else :
        LabelReturn.config(text = "IMAGE REELLE A " + str(100 * Sum_RateBool) + " %." , fg = "Green" )




def WarningUser():
    LabelReturn.config(text = "Sélectionnez un fichier valide.", fg = "Red" )
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Création de l'IHM -------------------------------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title("DeepFakeDetector Version 0.2")
root.iconbitmap('ImageRessource\Ico.ico')
root.geometry("1440x920")
root.resizable(False, False)


background = tk.Frame(root, width=1440, height=920, bg="lightgrey")
background.grid(row=0, column=0)

Bg = Image.open("ImageRessource\Background.jpg")
Bg = Bg.resize((1440, 920)) 
Bg = ImageTk.PhotoImage(Bg)


LabelImageFrame = tk.Label(background, image=Bg)
LabelImageFrame.place(x=0, y=0)


menu = tk.Frame(background, width=1320, height=800, bg='white')
menu.grid(row=0, column=0)
menu.place(x=60, y=60)


# Partie Detection Interface -------------------------------------------------------------------------------------------------------------------------------------------

TestLabelTitle = tk.Label(menu, text="Bienvenue sur DeepFakeDetector !", font=("Arial", 20), bg="white")
TestLabelTitle.place(x = 50, y = 50)

Notice = tk.Label(menu, text="Mode d'emploi : ", font=("Arial", 15), bg="white")
Notice.place(x = 50, y = 150)

Instruction1 = tk.Label(menu, text="1. Selectionnez une image avec le bouton < CHARGER VOTRE IMAGE >.", font=("Arial", 11), bg="white", fg="grey")
Instruction1.place(x = 50, y = 200)

Instruction2 = tk.Label(menu, text="2. Lancez l'analyse avec le bouton < LANCER L'ANALYSE >.", font=("Arial", 11), bg="white", fg="grey")
Instruction2.place(x = 50, y = 230)

Instruction3 = tk.Label(menu, text="3. Le système va vous indiquer l'interprétation de l'image.", font=("Arial", 11), bg="white", fg="grey")
Instruction3.place(x = 50, y = 260)


ButtonPathTest = tk.Button(menu, text = "CHARGER VOTRE IMAGE", width=70, command = OpenFilePathTest, bg="#1E90FF", fg="white")
ButtonPathTest.place(x = 50, y = 680)

ButtonLunchTest = tk.Button(menu, text="LANCER L'ANALYSE", width = 70, command = lambda : RouterModel(FilePathTest), bg="#1E90FF", fg="white")
ButtonLunchTest.place(x = 50, y = 726)

LabelReturn=tk.Label(menu,text ="",font=("Arial",31), bg="white")
LabelReturn.place(x = 50,y = 600)



ImageFrame = Image.open("ImageRessource\ImageCadre.jpg")
ImageFrame = ImageFrame.resize((700, 700)) 
tk_ImageFrame = ImageTk.PhotoImage(ImageFrame)
LabelImageFrame = tk.Label(menu, image=tk_ImageFrame)

LabelImageFrame.place(x=570, y= 50)



# Démarrage de l'application ------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()


from keras.models import load_model
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

model = load_model('Model\Model10Epochs30batch.h5')

FilePathTest = ""
ImageToAnalys = ""



# Définition des fonctions --------------------------------------------------------------------------------------------------------------------------------------------

def OpenFilePathTest():
     
    global FilePathTest 
    FilePathTest = filedialog.askopenfilename()
    print(FilePathTest)
    if FilePathTest != "":
        UpdateImage(FilePathTest)
    
def LunchAnalyze(FilePathTest):
    
    if FilePathTest == "":
        
        LabelReturn.config(text = "VEUILLEZ SELECTIONNER UNE IMAGE POUR ANALYSE.", fg = "Red" )
        
    else:
            
        print(FilePathTest)
        global ImgToAnalys 
        ImgToAnalys = Image.open(FilePathTest)
    
        ImgToAnalys = ImgToAnalys.resize((200, 200))
        ImgToAnalysArray = np.array(ImgToAnalys)
        ImgToAnalysArray = np.expand_dims(ImgToAnalysArray, axis=0)
        predictions = model.predict(ImgToAnalysArray)
        Rates = predictions[0]
    
        RateFake = Rates[0]
        RateReal = Rates[1]
    
        print(RateFake)
        print(RateReal)
    
        ResultAnalys(RateFake, RateReal)


def ResultAnalys(RateFake, RateReal):
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
    LabelImageFrame.image = tk_ImgToAnalys  # Garde une référence de l'image


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

TestLabelTitle = tk.Label(menu, text="Bienvenue sur DeepfakeDetector !", font=("Arial", 20), bg="white")
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

ButtonLunchTest = tk.Button(menu, text="LANCER L'ANALYSE", width = 70, command = lambda : LunchAnalyze(FilePathTest), bg="#1E90FF", fg="white")
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
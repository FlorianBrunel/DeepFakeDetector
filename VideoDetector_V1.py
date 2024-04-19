from keras.layers import TFSMLayer
import numpy as np
from tkinter import filedialog
import tensorflow as tf
import cv2
from PIL import Image
import os

model = TFSMLayer('Model\Model10Epochs60batch', call_endpoint='serving_default')

FilePathTest = ""
ImageToAnalys = ""

# Définition des fonctions --------------------------------------------------------------------------------------------------------------------------------------------

def OpenFilePathTest():
     
    global FilePathTest 
    FilePathTest = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
    print(FilePathTest)
    TransformVideoToImage(FilePathTest)
    

def TransformVideoToImage(FilePathTest):
    cap = cv2.VideoCapture(FilePathTest)
    count = 0
    Sum_RateBool = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == False:
            break
        image_path = 'ImagesVideo/VideoFrame'+str(count)+'.jpg'
        cv2.imwrite(image_path, frame)
        Sum_RateBool += LunchAnalyze(image_path)
        count += 1
    cap.release()
    DestroyContent(count)

    ReturnResult(Sum_RateBool, count)

    return count


def DestroyContent(count):
    for i in range(count):
        image_path = 'ImagesVideo/VideoFrame'+str(i)+'.jpg'
        os.remove(image_path)
    return count

def LunchAnalyze(FilePathTest):
    if FilePathTest == "":
        print("Pas de vidéo")
    else:
        global ImgToAnalys 
        ImgToAnalys = Image.open(FilePathTest)
        
        ImgToAnalys = ImgToAnalys.resize((200, 200))
        ImgToAnalysArray = np.array(ImgToAnalys)
        ImgToAnalysArray = np.expand_dims(ImgToAnalysArray, axis=0)
        predictions = model(ImgToAnalysArray)
        
        Rates = tf.nn.softmax(predictions['output_0'][0]).numpy()

        RateFake = Rates[0]
        RateReal = Rates[1]
        
        ResultAnalys(RateFake, RateReal)

        RateBool = 0
        if RateFake < RateReal :
            RateBool = 1
        
        return RateBool
            
            
def ResultAnalys(RateFake, RateReal):
    if RateFake < RateReal :
        TrueRate = round(100*RateReal)
        print("Vrai à " + str(TrueRate))
    else :
        TrueRate = round(100*RateFake)
        print("Faux à " + str(TrueRate))
    return TrueRate



def ReturnResult(Sum_RateBool, count):
    print(Sum_RateBool)
    print(count)
    average_RateBool = Sum_RateBool / count
    if (Sum_RateBool < count/2) :
        print('En moyenne :' + str(round(100 - 100*average_RateBool)) + ' % des images de la vidéo sont considérées comme des fakes.')
    else :
        print('En moyenne :' + str(round(100*average_RateBool)) + ' % des images de la vidéo sont considérées comme réelles.')



OpenFilePathTest()


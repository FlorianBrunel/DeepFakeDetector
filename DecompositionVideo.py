from tkinter import filedialog
import cv2
import os

FilePathTest = ""
ImageToAnalys = ""


def OpenFilePathTest():
    global FilePathTest 
    directory_path = filedialog.askdirectory()
    video_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith(('.mp4', '.avi'))]
    for video_file in video_files:
        print(video_file)
        TransformVideoToImage(video_file)

def TransformVideoToImage(FilePathTest):
    cap = cv2.VideoCapture(FilePathTest)
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == False:
            break
        image_path = 'ImagesVideo/VideoFrame'+str(count)+'.jpg'
        cv2.imwrite(image_path, frame)
        count += 1
    cap.release()


    return count



OpenFilePathTest()
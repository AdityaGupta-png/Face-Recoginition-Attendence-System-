# Importing the all library of python 
# Importing the tkinter 
from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox   # importing the message box 
import mysql.connector   # import mysql data base 
import cv2       # Importing the opencv 
import numpy as np
import os


# Making the class Face_Recogintion attendence system
class Face_Recognition: 
    
    # Making the constructor of the class 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recoginition Attendence System")
        
        # Making the title of the page  Face Recognition 
        title_label = Label(self.root,text="Face Recognition",
                            font=("times new roman",35,"bold"),
                            fg="blue",
                            bg="white",
                            anchor="center")
        title_label.place(x=0,y=0,width=1280,height=60)
        
        # Adding the 1st images 
        img1 = Image.open(r"Project_Images\Face_Detector_4.jpg")
        img1 = img1.resize((550,530),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img1)
        
        f_label_1 = Label(self.root,image=self.photoimg_1)
        f_label_1.place(x=0,y=60,width=550,height=530)
        
        # Adding the 2 nd image
        img2 = Image.open(r"Project_Images\faec_detect.pg.jpg")
        img2 = img2.resize((730,530),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img2)
        
        f_label_1 = Label(self.root,image=self.photoimg_2)
        f_label_1.place(x=550,y=60,width=730,height=530)
        
        # Making the bottom title 
        title_bottom = Label(self.root,
                             text="Frontal Face Detector",
                             font=("times new roman",25,"bold"),
                             bg="white",fg="blue",anchor="center")
        title_bottom.place(x=0,y=590,width=1280,height=50)
        
    
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
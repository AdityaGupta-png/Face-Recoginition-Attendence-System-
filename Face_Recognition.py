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
        
        # Adding the images 
        
        
    
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
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
class Train_Face: 
    
    # Making the constructor of the class 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recoginition Attendence System")
        
        title_label = Label(self.root,text="TRAIN DATA SET",
                            font=("times new roman",35,"bold"),
                            fg="red",
                            bg="white",
                            anchor="center")
        title_label.place(x=0,y=0,width=1350,height=45)
        
        # Add the image
        img1 = Image.open(r"Project_Images\train_imp_img.jpg")
        img1 = img1.resize((1280,250),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img1)
        
        f_label_1 = Label(self.root,image=self.photoimg_1)
        f_label_1.place(x=0,y=45,width=1280,height=250)
        
        # making the button 
        b1_1 = Button(self.root,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",35,"bold"),width=50,bg="blue",fg="white")
        b1_1.place(x=0,y=295,width=1280,height=50)
        
        # Add the botttom images 
        img_bottom = Image.open(r"Project_Images\Photo.jpg")
        img_bottom = img_bottom.resize((1280,300),Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_label_1 = Label(self.root,image=self.photoimg_bottom)
        f_label_1.place(x=0,y=345,width=1280,height=300)
        
    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces = []
        ids = []
        
        for image in path :
            img = Image.open(image).convert('L')  #Gray scal convert 
            imageNp = np.array(img,'uint8')
            
            id = int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Training Face",imageNp)
            cv2.waitKey(1) == 13
            
        ids = np.array(ids)
        
        # ====================== TRAIN THE CLASSIFIER AND SAVE ===================
        # Create LBPH recognizer
        clf = cv2.face.LBPHFaceRecognizer_create()

        # Train with faces and IDs
        clf.train(faces, np.array(ids))

        # Save the trained model
        clf.write("Classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed!!!",parent=self.root) 
        

# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Train_Face(root)
    root.mainloop()
# Importing the tkinter 
from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk

# Making the class Face_Recogintion attendence system
class Face_Recoginition_System: 
    
    # Making the constructor of the class 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recoginition Attendence System")
        
        # Attated images on the Root window 
        # Added image no 1
        img1 = Image.open(r"Project_Images\image_3.jpg")
        img1 = img1.resize((425,150),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img1)
        
        f_label_1 = Label(self.root,image=self.photoimg_1)
        f_label_1.place(x=0,y=0,width=425,height=150)
        
        # Added image number 2 
        img2 = Image.open(r"Project_Images\image_1.jpg")
        img2 = img2.resize((425,150),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img2)
        
        f_label_2 = Label(self.root,image=self.photoimg_2)
        f_label_2.place(x= 425,y=0,width=425,height=150)
        
        # Added 3 rd image 
        img3 = Image.open(r"Project_Images\Image_2.jpg")
        img3 = img3.resize((425,150),Image.Resampling.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img3)
        
        f_label_3 = Label(self.root,image=self.photoimg_3)
        f_label_3.place(x= 850,y=0,width=425,height=150)
        
        # Added the background 
        img4 = Image.open(r"Project_Images\bg_image1.jpg")
        img4 = img4.resize((1300,500),Image.Resampling.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img4)
        
        f_label_4 = Label(self.root,image=self.photoimg_4)
        f_label_4.place(x = 0,y = 150,width=1300,height=500)
        
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition_System(root)
    root.mainloop()
    


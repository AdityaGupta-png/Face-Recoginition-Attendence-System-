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
        img1 = img1.resize((425,130),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img1)
        
        f_label_1 = Label(self.root,image=self.photoimg_1)
        f_label_1.place(x=0,y=0,width=425,height=130)
        
        # Added image number 2 
        img2 = Image.open(r"Project_Images\image_1.jpg")
        img2 = img2.resize((425,130),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img2)
        
        f_label_2 = Label(self.root,image=self.photoimg_2)
        f_label_2.place(x= 425,y=0,width=425,height=130)
        
        # Added 3 rd image 
        img3 = Image.open(r"Project_Images\Image_2.jpg")
        img3 = img3.resize((425,130),Image.Resampling.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img3)
        
        f_label_3 = Label(self.root,image=self.photoimg_3)
        f_label_3.place(x= 850,y=0,width=425,height=130)
        
        # Added the background 
        img4 = Image.open(r"Project_Images\bg_image1.jpg")
        img4 = img4.resize((1300,550),Image.Resampling.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img4)
        
        bg_img = Label(self.root,image=self.photoimg_4)
        bg_img.place(x = 0,y = 130,width=1300,height=550)
        
        # Added the title label 
        title_label = Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",
                            font=("times new roman",30,"bold"),
                            bg = "white",fg="red")
        title_label.place(x=0,y=0,width=1350,height=45)
        
        # Adding buttons to the Background label
        
        # STUDENT DETAILS button 
        img5 = Image.open(r"Project_Images\Student_Details2.jpg")
        img5 = img5.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img,image=self.photoimg_5,cursor="hand2")
        b1.place(x= 95,y= 50,width=200,height=180)
        
        b1_1 = Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x= 95,y= 230,width=200,height=35)
        
        # Detect face button 
        img6 = Image.open(r"Project_Images\Face_Detector_2.jpg")
        img6 = img6.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_6 = ImageTk.PhotoImage(img6)
        
        b2 = Button(bg_img,image=self.photoimg_6,cursor="hand2")
        b2.place(x= 375,y= 50,width=200,height=180)
        
        b1_2 = Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_2.place(x= 375,y= 230,width=200,height=35)
        
        # Attendence face button  
        img7 = Image.open(r"Project_Images\Attendence.jpg")
        img7 = img7.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_7 = ImageTk.PhotoImage(img7)
        
        b2 = Button(bg_img,image=self.photoimg_7,cursor="hand2")
        b2.place(x= 655,y= 50,width=200,height=180)
        
        b1_2 = Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_2.place(x= 655,y= 230,width=200,height=35)
        
        # Help desk button  
        img8 = Image.open(r"Project_Images\help desk.jpg")
        img8 = img8.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_8 = ImageTk.PhotoImage(img8)
        
        b2 = Button(bg_img,image=self.photoimg_8,cursor="hand2")
        b2.place(x= 960,y= 50,width=200,height=180)
        
        b1_2 = Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_2.place(x= 960,y= 230,width=200,height=35)
        
        # Train face 
        img9 = Image.open(r"Project_Images\Train_Face.jpg")
        img9 = img9.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img,image=self.photoimg_9,cursor="hand2")
        b1.place(x= 95,y= 295,width=200,height=180)
        
        b1_1 = Button(bg_img,text="Train Face",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_1.place(x= 95,y= 475,width=200,height=35)
        
        # Add Photos 
        img10 = Image.open(r"Project_Images\Photo.jpg")
        img10 = img10.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_10 = ImageTk.PhotoImage(img10)
        
        b2 = Button(bg_img,image=self.photoimg_10,cursor="hand2")
        b2.place(x= 375,y= 295,width=200,height=180)
        
        b1_2 = Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_2.place(x= 375,y= 475,width=200,height=35)
        
        # Developer button  
        img11 = Image.open(r"Project_Images\Developer_2.jpg")
        img11 = img11.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_11 = ImageTk.PhotoImage(img11)
        
        b2 = Button(bg_img,image=self.photoimg_11,cursor="hand2")
        b2.place(x= 655,y= 295,width=200,height=180)
        
        b1_2 = Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_2.place(x= 655,y= 475,width=200,height=35)
        
        # Exit button 
        img12 = Image.open(r"Project_Images\Exit_2.jpg")
        img12 = img12.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg_12 = ImageTk.PhotoImage(img12)
        
        b2 = Button(bg_img,image=self.photoimg_12,cursor="hand2")
        b2.place(x= 960,y= 295,width=200,height=180)
        
        b1_2 = Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",20,"bold"),bg = "darkblue",fg="white")
        b1_2.place(x= 960,y= 475,width=200,height=35)
        

        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition_System(root)
    root.mainloop()
    


# Importing the tkinter 
from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk

# Making the class Face_Recogintion attendence system
class StudentDetails: 
    
    # Making the constructor of the class 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recoginition Attendence System")
        
    # Adding the different images of the same size so we cpoy the code 
        # Added image no 1
        img1 = Image.open(r"Project_Images\student_details_3.jpg")
        img1 = img1.resize((425,130),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img1)
        
        f_label_1 = Label(self.root,image=self.photoimg_1)
        f_label_1.place(x=0,y=0,width=425,height=130)
        
        # Added image number 2 
        img2 = Image.open(r"Project_Images\student_details_4.jpg")
        img2 = img2.resize((425,130),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img2)
        
        f_label_2 = Label(self.root,image=self.photoimg_2)
        f_label_2.place(x= 425,y=0,width=425,height=130)
        
        # Added 3 rd image 
        img3 = Image.open(r"Project_Images\Student_Details.jpg")
        img3 = img3.resize((425,130),Image.Resampling.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(img3)
        
        f_label_3 = Label(self.root,image=self.photoimg_3)
        f_label_3.place(x= 850,y=0,width=425,height=130)
        
        # Added the background images 
        img4 = Image.open(r"Project_Images\bg_image1.jpg")
        img4 = img4.resize((1300,550),Image.Resampling.LANCZOS)
        self.photoimg_4 = ImageTk.PhotoImage(img4)
        
        bg_img = Label(self.root,image=self.photoimg_4)
        bg_img.place(x = 0,y = 130,width=1300,height=550)
        
        # Added the title label 
        title_label = Label(bg_img,text="STUDENT MANAGEMENT SYETEM",
                            font=("times new roman",30,"bold"),
                            bg = "white",fg="red")
        title_label.place(x=0, y=0, width=1350, height=45)
        
        # Making the main frame 
        main_frame = Frame(bg_img,border=2,bg="white")
        main_frame.place(x=0,y=45,width=1350,height=500)
        
        # DIVIDE mainLabelFrame --> 2 types 
        # 1 --> LeftSideLabelFrame                2 --> RightSideLabelFrame 
        
        # Left Side Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details"
                                ,font=("times new roman",12,"bold"))
        left_frame.place(x=0,y=0,width=700,height=465)
        
        # Right side Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details"
                                ,font=("times new roman",12,"bold"))
        right_frame.place(x=705,y=0,width=565,height=465)
        
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = StudentDetails(root)
    root.mainloop()
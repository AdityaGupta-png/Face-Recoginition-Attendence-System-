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
        title_label = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",
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
        left_frame.place(x=0,y=0,width=700,height=460)
        
        # Adding images to the left frames 
        img_left_1 = Image.open(r"Project_Images\student_details_3.jpg")
        img_left_1 = img_left_1.resize((695,120),Image.Resampling.LANCZOS)
        self.photoimg_left_1 = ImageTk.PhotoImage(img_left_1)
        
        f_label_1 = Label(left_frame,image=self.photoimg_left_1)
        f_label_1.place(x=0,y=0,width=695,height=120)
        
        # Cousre information 
        cousre_info = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Infomation"
                                ,font=("times new roman",12,"bold"))
        cousre_info.place(x=0,y=125,width=695,height=90)
        
        # Making the comboBox inside the Course Information 
        # 1---> For the Department 
        dep_label = Label(cousre_info,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,pady=5)
        
        dep_combo = ttk.Combobox(cousre_info,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"] = ("Select Department",
                               "Computer Science",
                               "Information Technology",
                               "AIML",
                               "Data Science",
                               "Mechanical",
                               "Civil")
        dep_combo.current(0)   # make 0 index as the default values 
        dep_combo.grid(row=0,column=1,padx=20,pady=5)
        
        # 2--->  for the college year
        currentcollegeYear_label = Label(cousre_info,text="Current College Year",font=("times new roman",12,"bold"),bg="white")
        currentcollegeYear_label.grid(row=0,column=2,padx=10,pady=5)
        
        currentcollegeYear_combo = ttk.Combobox(cousre_info,font=("times new roman",12,"bold"),width=17,state="readonly")
        currentcollegeYear_combo["values"] = ("Select Year",
                                              "FE",
                                              "SE",
                                              "TE",
                                              "BE")
        currentcollegeYear_combo.current(0)  # Make 0 index as the default 
        currentcollegeYear_combo.grid(row=0,column=3,padx=10,pady=5)
        
        #3 --->  for the year 
        year_label = Label(cousre_info,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,pady=5)
        
        year_combo = ttk.Combobox(cousre_info,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"] = ("Select Year",
                                "2025-26",
                                "2026-27",
                                "2027-28",
                                "2028-29")
        year_combo.current(0)  # Making the 0 index as the default values 
        year_combo.grid(row=1,column=1,padx=20,pady=5)
        
        #4 -->  For the semester 
        semester_label = Label(cousre_info,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,pady=5)
        
        semester_combo = ttk.Combobox(cousre_info,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"] = ("Select Semester",
                                    "Semester-1",
                                    "Semester-2",
                                    "Semester-3",
                                    "Semester-4",
                                    "Semester-5",
                                    "Semester-6",
                                    "Semester-7",
                                    "Semester-8"
                                )
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=20,pady=5)
        
        
        
        
        
        # Right side Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details"
                                ,font=("times new roman",12,"bold"))
        right_frame.place(x=705,y=0,width=560,height=460)
        
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = StudentDetails(root)
    root.mainloop()
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
from time import strftime   # import the date and time 
from datetime import datetime

# Making the class Face_Recogintion attendence system
class Attendence: 
    
    # Making the constructor of the class 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.title("Manange Attendence System")
        
        # Adding the different images of the same size so we cpoy the code 
        # Added image no 1
        left_frame_img_1 = Image.open(r"Project_Images\Attendence_1.jpg")
        left_frame_img_1 = left_frame_img_1.resize((635,150),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(left_frame_img_1)
        
        f_label_1 = Label(self.root,image=self.photoimg_1)
        f_label_1.place(x=0,y=0,width=635,height=150)
        
        # Added image number 2 
        left_frame_img = Image.open(r"Project_Images\Attendence_3.jpg")
        left_frame_img = left_frame_img.resize((640,150),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(left_frame_img)
        
        f_label_2 = Label(self.root,image=self.photoimg_2)
        f_label_2.place(x= 635,y=0,width=640,height=150)
        
        # Making the title name as the Student management attendence system 
        title_label = Label(self.root,
                            text="STUDENT ATTENDENCE MANAGEMENT SYSTEM",
                            font=("times new roman",30,"bold"),
                            fg="red",
                            bg="white",
                            anchor="center")
        title_label.place(x=0,y=150,width=1275,height=50)
        
        # Maaking the main frame 
        main_frame = Frame(self.root,border=2,bg="white")
        main_frame.place(x=0,y=200,width=1280,height=500)
        
        # Making the left side label frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information"
                                ,font=("times new roman",12,"bold"))
        left_frame.place(x=0,y=0,width=630,height=435)
        
        # Adding the image in the left frame 
        left_frame_img_1 = Image.open(r"Project_Images\Attendence_2.jpg")
        left_frame_img_1 = left_frame_img_1.resize((630,150),Image.Resampling.LANCZOS)
        self.photoimg_3 = ImageTk.PhotoImage(left_frame_img_1)
        
        f_label_1 = Label(left_frame,image=self.photoimg_3)
        f_label_1.place(x=0,y=0,width=630,height=150)
        
        # Making the another frame 
        frame_1 = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
        frame_1.place(x=0,y=150,width=625,height=210)
        
        # Making the entry fills 
        
        # 1 --> Student Id 
        studentId_label = Label(frame_1,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=4)
        
        studentId_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=4)
        
        # 2 --> Student Name 
        studentName_label = Label(frame_1,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=4)
        
        StudentName_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=4)
        
        # 3 --> current cousre 
        current_course_label = Label(frame_1,text="Current Course:",font=("times new roman",12,"bold"),bg="white")
        current_course_label.grid(row=1,column=0,padx=10,pady=4)
        
        current_course_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        current_course_entry.grid(row=1,column=1,padx=10,pady=4)
        
        # 4 --> Department 
        department_label = Label(frame_1,text="Department:",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=4)
        
        department_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=4)
        
        # 5 --> Division 
        division_label = Label(frame_1,text="Division:",font=("times new roman",12,"bold"),bg="white")
        division_label.grid(row=2,column=0,padx=10,pady=4)
        
        division_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        division_entry.grid(row=2,column=1,padx=10,pady=4)
        
        #  6 --> Roll No,. 
        roll_label = Label(frame_1,text="Roll No.:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=2,column=2,padx=10,pady=4)
        
        roll_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        roll_entry.grid(row=2,column=3,padx=10,pady=4)
        
        # 7 --> Semester 
        Semester_label = Label(frame_1,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        Semester_label.grid(row=3,column=0,padx=10,pady=4)
        
        Semester_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        Semester_entry.grid(row=3,column=1,padx=10,pady=4)
        
        #  8 --> Date of birth
        dob_label = Label(frame_1,text="D.O.B.:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=3,column=2,padx=10,pady=4)
        
        dob_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        dob_entry.grid(row=3,column=3,padx=10,pady=4)
        
        #  9 --> timing 
        timming_label = Label(frame_1,text="Timming:",font=("times new roman",12,"bold"),bg="white")
        timming_label.grid(row=4,column=0,padx=10,pady=4)
        
        timming_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        timming_entry.grid(row=4,column=1,padx=10,pady=4)
        
        # Date
        year_label = Label(frame_1,text="Date:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=4,column=2,padx=10,pady=4)
        
        year_entry = ttk.Entry(frame_1,width=19,font=("times new roman",12,"bold"))
        year_entry.grid(row=4,column=3,padx=10,pady=4)
        
        # making the attendence label 
        attendence_label = Label(frame_1,text="Attendence Label:",font=("times new roman",12,"bold"),bg="white")
        attendence_label.grid(row=5,column=0,padx=10,pady=4)
        
        attendence_label_combo = ttk.Combobox(frame_1,font=("times new roman",12,"bold"),width=14,state="readonly")
        attendence_label_combo["values"] = ("Status",
                                  "Present",
                                  "Absent")
        attendence_label_combo.current(0)
        attendence_label_combo.grid(row=5,column=1,padx=10,pady=4)
        
        
        # Making the another frame 
        frame_2 = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
        frame_2.place(x=0,y=360,width=625,height=50)
        
        # # Making the buttons in frame 2 
        # Import csv
        importcsv_btn = Button(frame_2,text="Import csv",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        importcsv_btn.grid(row=0,column=0,padx=12,pady=6)
        
        # Export csv 
        exportcsv_btn = Button(frame_2,text="Export csv",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        exportcsv_btn.grid(row=0,column=1,padx=12,pady=6)
        
        #Update button
        update_btn = Button(frame_2,text="Update",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2,padx=12,pady=6)
        
        # Reset button 
        reset_btn = Button(frame_2,text="Reset",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=12,pady=6)
        
        # Making the right frane 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details"
                                ,font=("times new roman",12,"bold"))
        right_frame.place(x=635,y=0,width=630,height=435)
        
        
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
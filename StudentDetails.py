# Importing the tkinter 
from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox   # importing the message box 
import mysql.connector




# Making the class Face_Recogintion attendence system
class StudentDetails: 
    
    # Making the constructor of the class 
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recoginition Attendence System")
        
        # Making the variables 
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year_1 = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        
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
        left_frame.place(x=0,y=0,width=670,height=460)
        
        # Cousre information 
        cousre_info = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Infomation"
                                ,font=("times new roman",12,"bold"))
        cousre_info.place(x=0,y=10,width=665,height=120)
        
        # Making the comboBox inside the Course Information 
        # 1---> For the Department 
        dep_label = Label(cousre_info,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,pady=10)
        
        dep_combo = ttk.Combobox(cousre_info,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"] = ("Select Department",
                               "Computer Science",
                               "Information Technology",
                               "AIML",
                               "Data Science",
                               "Mechanical",
                               "Civil")
        dep_combo.current(0)   # make 0 index as the default values 
        dep_combo.grid(row=0,column=1,padx=20,pady=10)
        
        # 2--->  for the college year
        currentcollegeYear_label = Label(cousre_info,text="Current College Year",font=("times new roman",12,"bold"),bg="white")
        currentcollegeYear_label.grid(row=0,column=2,padx=10,pady=10)
        
        currentcollegeYear_combo = ttk.Combobox(cousre_info,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        currentcollegeYear_combo["values"] = ("Select Year",
                                              "FE",
                                              "SE",
                                              "TE",
                                              "BE")
        currentcollegeYear_combo.current(0)  # Make 0 index as the default 
        currentcollegeYear_combo.grid(row=0,column=3,padx=10,pady=10)
        
        #3 --->  for the year 
        year_label = Label(cousre_info,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,pady=10)
        
        year_combo = ttk.Combobox(cousre_info,textvariable=self.var_year_1,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"] = ("Select Year",
                                "2025-26",
                                "2026-27",
                                "2027-28",
                                "2028-29")
        year_combo.current(0)  # Making the 0 index as the default values 
        year_combo.grid(row=1,column=1,padx=20,pady=10)
        
        #4 -->  For the semester 
        semester_label = Label(cousre_info,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,pady=10)
        
        semester_combo = ttk.Combobox(cousre_info,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
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
        semester_combo.grid(row=1,column=3,padx=20,pady=10)
        
        # Making another label name as the class student information taken 
        Class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information"
                                ,font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=0,y=140,width=665,height=200)
        
        # 1 --> Entry fill name as Student Name 
        studentName_label = Label(Class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=10)
        
        StudentName_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=10)
        
        # 2 --> Entry fill for the studentId 
        studentId_label = Label(Class_Student_frame,text="StudentId:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=20,pady=10)
        
        studentId_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=10)
        
        # 3 --> For the roll no 
        rollNo_label = Label(Class_Student_frame,text="RollNo.:",font=("times new roman",12,"bold"),bg="white")
        rollNo_label.grid(row=1,column=0,padx=5,pady=10)
        
        rollNo_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=1,column=1,padx=10,pady=10)
        
        # 4 --> FOR the Date of birth
        DOB_label = Label(Class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=1,column=2,padx=20,pady=10)
        
        DOB_entry = ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        DOB_entry.grid(row=1,column=3,padx=10,pady=10)
        
        # 5 --> Entry fill for the division 
        division_label = Label(Class_Student_frame,text="Division:",font=("times new roman",12,"bold"),bg="white")
        division_label.grid(row=2,column=0,padx=5,pady=10)
        
        division_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="readonly")
        division_combo["values"] = ("Select Divion",
                                    "A",
                                    "B",
                                    "C",
                                    "D",
                                    "E")
        division_combo.current(0)
        division_combo.grid(row=2,column=1,padx=10,pady=10)
        
        # 6 --> Entry fill for the gender 
        gender_label = Label(Class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=2,padx=10,pady=10)
        
        gender_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"] = ("Select Gender",
                                  "Male",
                                  "Female",
                                  "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=10,pady=10)
        
        # Making the radio buttons 
        # Radio Buttons 1
        self.var_radio = StringVar()
        radiobutton_1 = ttk.Radiobutton(Class_Student_frame,text="Take Photo Sample",variable=self.var_radio,value="Yes")
        radiobutton_1.grid(row=3,column=0,padx=10,pady=10)
        
        # Radio Buttons 2 
        radiobutton_2 = ttk.Radiobutton(Class_Student_frame,text="No Photo Sample",variable=self.var_radio,value="No")
        radiobutton_2.grid(row=3,column=1,padx=10,pady=10)
    
        # Making the another frame for the buttons 
        
        button_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
        button_frame.place(x=0,y=340,width=665,height=45)
        
        # 1 --> Save button
        save_btn = Button(button_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=12,pady=5)
        
        # 2 --> Update button
        update_btn = Button(button_frame,text="Update",command=self.update_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=12,pady=5)
        
        # 3 --> delete button 
        delete_btn = Button(button_frame,text="Delete",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=12,pady=5)
        
        # 4 --> reset button
        reset_btn = Button(button_frame,text="Reset",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=12,pady=5)
        
        # Making the second button frame 
        button_frame_2 = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE)
        button_frame_2.place(x=0,y=385,width=665,height=50)
        
        # 1 --> Take phtot sample 
        takePhotoSample_btn = Button(button_frame_2,text="Take Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takePhotoSample_btn.grid(row=0,column=0,padx=10,pady=5)
        
        # 2 --> Update photo sample 
        updatePhotoSample_btn = Button(button_frame_2,text="Update Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatePhotoSample_btn.grid(row=0,column=1,padx=10,pady=5)
        
        # Right side Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details"
                                ,font=("times new roman",12,"bold"))
        right_frame.place(x=675,y=0,width=590,height=460)
        
        # Adding image in the right frame 
        right_frame_img = Image.open(r"Project_Images\right_frame_img.jpg")
        right_frame_img = right_frame_img.resize((589,120),Image.Resampling.LANCZOS)
        self.photoimg_right_frame = ImageTk.PhotoImage(right_frame_img)
        
        f_label_1 = Label(right_frame,image=self.photoimg_right_frame)
        f_label_1.place(x=1,y=0,width=585,height=120)
        
        # # Making the search system Label which is used to find the student details ny using their id 
        # #################### SEARCH SYSTEM ###################
        Search_system_frame = LabelFrame(right_frame,
                                        bd=2,bg="white",relief=RIDGE,
                                        text="Search System",
                                        font=("times new roman",12,"bold"))
        Search_system_frame.place(x=0,y=120,width=585,height=70)
        
        # Making the search lebel 
        search_label = Label(Search_system_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5)
        
        # Making the search Bar comboBox 
        search_combo = ttk.Combobox(Search_system_frame,font=("times new roman",13,"bold"),state="readonly",width=11)
        search_combo["values"] = ("Select Values",
                                  "StudentId",
                                  "Roll_No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5)
        
        # Making the Entry fill to fill the information then the search 
        search_entry = ttk.Entry(Search_system_frame,width=10,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5)
        
        # Making the buttons name as the search and show all 
        search_btn = Button(Search_system_frame,width=8,text= "Search",font=("times new roman",13,"bold"),fg="white",bg="blue")
        search_btn.grid(row=0,column=3,padx=10,pady=5)
        
        showAll_btn = Button(Search_system_frame,width=8,text="Show All",font=("times new roman",13,"bold"),fg="white",bg="blue")
        showAll_btn.grid(row=0,column=4,padx=10,pady=5)
        
        # Making the another table frame to display the data 
        table_frame = LabelFrame(right_frame,
                                bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=220,width=585,height=215)
        
        # Making the scroll bar in the X 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        
        # Making the scroll bar in the y
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,columns=("dep",
                                                               "course",
                                                               "year_1",
                                                               "sem",
                                                               "id",
                                                               "name",
                                                               "roll",
                                                               "dob",
                                                               "div",
                                                               "gender",
                                                               "photo"),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
    
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Current College Year")
        self.student_table.heading("year_1",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("dob",text="Date Of Birth")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"] = "headings"
        
        # Set the width of the every columns 
        self.student_table.column("dep",width=120)
        self.student_table.column("course",width=120)
        self.student_table.column("year_1",width=120)
        self.student_table.column("sem",width=120)
        self.student_table.column("id",width=120)
        self.student_table.column("name",width=120)
        self.student_table.column("roll",width=120)
        self.student_table.column("dob",width=120)
        self.student_table.column("div",width=120)
        self.student_table.column("gender",width=120)
        self.student_table.column("photo",width=120)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # ================================ Function declaration ==================================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Year" or self.var_year_1.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_roll.get() == "" or self.var_dob.get() =="" or self.var_gender.get() == "Select Division" or self.var_gender.get() == "Select Gender":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost",
                                            username = "root",
                                            password = "Aditya@1234",
                                            database = "face_recognize")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year_1.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_id.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_radio.get()
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Has Been Added Successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("error",f"Due To : {str(es)}",parent=self.root)

    # ============================= FETCH DATA ===========================================
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost",
                                       username = "root",
                                       password = "Aditya@1234",
                                       database = "face_recognize")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("",END,values=i)
            conn.commit
        conn.close()
        
    # =================================  get cursor ===========================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year_1.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_dob.set(data[7])
        self.var_div.set(data[8])
        self.var_gender.set(data[9])
        self.var_radio.set(data[10])
        
    #  =============================== UPDATE FUNCTION =================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Year" or self.var_year_1.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_roll.get() == "" or self.var_dob.get() =="" or self.var_gender.get() == "Select Division" or self.var_gender.get() == "Select Gender":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
      
        else:
            try:
                update = messagebox.askyesno("Update","Do You Want To Update Data ",parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host = "localhost",
                                       username = "root",
                                       password = "Aditya@1234",
                                       database = "face_recognize")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,year_1=%s,Semester=%s,Name=%s,Roll=%s,Dob=%s,Division=%s,Gender=%s,PhotoSample=%s WHERE Id=%s",(
                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                    self.var_year_1.get(),
                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                    self.var_dob.get(),  
                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_radio.get(),
                                                                                                                                                                    self.var_id.get()
                                                                                                                                                                                                                                      
                    ))                                                                                                                                                                                                                                                                 
                else:
                    if not update:
                        return
                
                messagebox.showinfo('Sucess',"Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
        
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
       
        
        
        
        
        
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = StudentDetails(root)
    root.mainloop()
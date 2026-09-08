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
        img1 = img1.resize((550,600),Image.Resampling.LANCZOS)
        self.photoimg_1 = ImageTk.PhotoImage(img1)
        
        f_label_1 = Label(self.root,image=self.photoimg_1)
        f_label_1.place(x=0,y=60,width=550,height=600)
        
        # Adding the 2 nd image
        img2 = Image.open(r"Project_Images\faec_detect.pg.jpg")
        img2 = img2.resize((730,600),Image.Resampling.LANCZOS)
        self.photoimg_2 = ImageTk.PhotoImage(img2)
        
        f_label_2 = Label(self.root,image=self.photoimg_2)
        f_label_2.place(x=550,y=60,width=730,height=600)
        
        # Making the button inside the image 2 
        b1_image_2 = Button(f_label_2,text="Face Recognition",cursor="hand2",
                            command=self.face_recog,
                            font=("times new roman",18,"bold"),
                            fg="white",bg="blue")
        b1_image_2.place(x=260,y=530,width=200,height=35)
        
    #  ============================   MARK ATTENDENCE =================================
    def mark_attendence(self,i, n, cc, d, di, r, s, dob):
        with open("Attendence.csv","r+",newline="\n") as f :
            
            # Store the file data 
            myDataList = f.readlines()
            
            # Creating empty list 
            name_List = []
            
            for line in myDataList:
                
                # Store values in form of the spilling value 
                entry = line.split((","))
                
                if len(entry) > 0:
                    name_List.append(entry[0])
                
        
            # making the condition if id not in name list then mark attendence 
            # if present then do not mark attendence same have present 
            if str(i) not in name_List:
                
                now = datetime.now()
                
                # for the year 
                d1 = now.strftime("%d/%m/%Y")
                
                # Making the date string 
                dtString = now.strftime("%H:%M:%S")
                
                # Writing all the data in csv files 
                f.writelines(f"\n{i},{n},{cc},{d},{di},{r},{s},{dob},{dtString},{d1},Present \n")
                
                # In above we store 
                """
                1. Student Id 
                2. Student Name 
                3. Current cousre 
                4. department 
                5. Division
                6. Roll No.
                7. Semester 
                8. Date of birth 
                9. timing and day month and year 
                """
            
        
    # ============================== FACE RECOGNITION =====================================
    # Adding the face_recognize methods 
    def face_recog(self):

    # =========================================================
    # DRAW BOUNDARY + RECOGNIZE FACE
    # =========================================================
        def draw_boundary(img, classifier, scaleFactor, minNeighbors,
                      color, text, clf, my_cursor):

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = classifier.detectMultiScale(
            gray_image,
            scaleFactor,
            minNeighbors
            )

            coord = []

            for (x, y, w, h) in faces:

            # -------------------------------------------------
            # Predict face using LBPH
            # -------------------------------------------------
                face_roi = gray_image[y:y + h, x:x + w]

                id, distance = clf.predict(face_roi)

                print("================================")
                print("Predicted ID :", id)
                print("LBPH Distance:", distance)

            # -------------------------------------------------
            # Convert distance approximately to confidence
            # -------------------------------------------------
                confidence = int(100 * (1 - distance / 100))

                if confidence < 0:
                    confidence = 0

                print("Confidence    :", confidence)

            # -------------------------------------------------
            # Get student from database
            # -------------------------------------------------
                my_cursor.execute("""
                SELECT Id, Name, Course, Dep, Division, Roll, Semester, Dob
                FROM student
                WHERE Id = %s
                """, (int(id),))

                students = my_cursor.fetchone()

                print("Database Student:", students)

            # =================================================
            # FACE RECOGNIZED
            # =================================================
                if students is not None and distance < 70:

                    i, n, cc, d, di, r, s, dob = students

                # Green rectangle
                    cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    3
                    )

                # -------------------------------------------------
                # Student ID
                # -------------------------------------------------
                    cv2.putText(
                    img,
                    f"Student Id: {i}",
                    (x, y - 250),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # Student Name
                    cv2.putText(
                    img,
                    f"Student Name: {n}",
                    (x, y - 225),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # Course
                    cv2.putText(
                    img,
                    f"Course: {cc}",
                    (x, y - 200),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # Department
                    cv2.putText(
                    img,
                    f"Department: {d}",
                    (x, y - 175),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # Division
                    cv2.putText(
                    img,
                    f"Division: {di}",
                    (x, y - 150),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # Roll
                    cv2.putText(
                    img,
                    f"Roll No.: {r}",
                    (x, y - 125),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # Semester
                    cv2.putText(
                    img,
                    f"Semester: {s}",
                    (x, y - 100),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # DOB
                    cv2.putText(
                    img,
                    f"Date Of Birth: {dob}",
                    (x, y - 75),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                    )

                # Distance
                    cv2.putText(
                    img,
                    f"Distance: {distance:.2f}",
                    (x, y -50),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                    )

                # Confidence
                    cv2.putText(
                    img,
                    f"Confidence: {confidence}%",
                    (x, y -25),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                    )
                    
                    # Mark attendence
                    self.mark_attendence(i,n,cc,d,di,r,s,dob)

            # =================================================
            # UNKNOWN FACE
            # =================================================
                else:

                    cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (0, 0, 255),
                    3
                    )

                    cv2.putText(
                    img,
                    "Unknown Face",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.8,
                    (0, 0, 255),
                    2
                    )

                coord.append([x, y, w, h])

            return coord


    # =========================================================
    # RECOGNIZE FUNCTION
    # =========================================================
        def recognize(img, clf, faceCascade, my_cursor):

            draw_boundary(
            img,
            faceCascade,
            1.1,
            10,
            (255, 255, 255),
            "Face",
            clf,
            my_cursor
            )

            return img


    # =========================================================
    # HAAR CASCADE
    # =========================================================
        faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
        )

        if faceCascade.empty():
            print("ERROR: Haar Cascade not loaded")
            return


    # =========================================================
    # LBPH CLASSIFIER
    # =========================================================
        clf = cv2.face.LBPHFaceRecognizer_create()

        try:
            clf.read("Classifier.xml")
            print("Classifier.xml loaded successfully")

        except Exception as e:
            print("ERROR loading Classifier.xml:", e)
            return


    # =========================================================
    # MYSQL CONNECTION
    # =========================================================
        try:

            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Aditya@1234",
                database="face_recognize"
            )

            my_cursor = conn.cursor()

            print("MySQL connected successfully")

        except mysql.connector.Error as e:

            print("Database connection error:", e)
            return


    # =========================================================
    # OPEN CAMERA
    # =========================================================
        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():

            print("ERROR: Camera could not be opened")

            my_cursor.close()
            conn.close()

            return


    # =========================================================
    # MAIN LOOP
    # =========================================================
        while True:

            ret, img = video_cap.read()

            if not ret:

                print("ERROR: Could not read camera frame")
                break

        # Face recognition
            img = recognize(
                img,
                clf,
                faceCascade,
                my_cursor
            )

        # Show camera
            cv2.imshow(
            "Welcome To Face Recognition",
            img
            )

        # Press ENTER to exit
            if cv2.waitKey(1) == 13:
                break


    # =========================================================
    # RELEASE RESOURCES
    # =========================================================
        video_cap.release()

        cv2.destroyAllWindows()

        my_cursor.close()
        conn.close()



                    
                    
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
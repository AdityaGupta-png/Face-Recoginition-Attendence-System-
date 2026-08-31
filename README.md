
######################################################  DAY ONE  ############################################
1 --> main file 
import tkinter --> for making the powerful Gui--> Graphical user interface 
ttk --> iske andar stylish toolkit hote hai 
pillow library --> for images dalne ke liye 

self.root.geometry("widthxheight+x+y)
self.root.title("name ")

add the Porject image --> that add all image related to project 

after adding all the images to the Images folders 

creating the FACE RECOGNITION ATTENDENCE SYSTEM root window 
1 --> Adding the background image
# Adding the Buttons above the background image 
            a --> Student details buttons 
            b --> Detect face 
            c --> Attendence face button 
            d --> Help desk button 
            e --> Train face 
            f --> Photos 
            g --> Developer option 
            h ---> Exit button --> redirect to the login page 

############# HERE FACE RECOGINTION ATTEDENCE SYSTEM PAGE AND 8 BUTTTON ARE ADDED" ###############

2 --> Making the student details page 
        Here We Make the Main frame and divide into 2 frames 
            a --> left side frame 
            b --> Right side frame 

        1. Left side Frame --> Divide into more 3 frame 
            a --> Student Deatails 
            b --> Current course information 
                        1. Department ComboBox
                        2. College Year ComboBox
                        3. Year ComboBox
                        4. Semester ComboBox
            c --> Class student information 
                        1. StudentId entry fill 
                        2. Student Name entry fill
                        3. Roll No entry fill 
                        4. DOB entry fill 
                        5. Division combo box 
                        6. Gender combo box 
            d --> Radio Buttons 
                        1. Take photo sample Yes or no 
                        2. No photo sample 
            e --> Buttons 
                        1. Save the data 
                        2. Update the data 
                        3. Delete the data
                        4. Reset the data 
                        5. Take the phot0 sample --> take you 100 photos in sceond 
                        6. Update photo sample 
            
        2. Right side Frame --> Divide into  main frame 
            a. Add the image 
            b. Search system 
                --> We can search student based on their rollNo. and studentId
            c. Table frame 
                --> Show all the data related registe student
            
        3 . Establish the connection with the MYSQL data base 
            a. Working on the save button 
                --> After click its save the information in the mysql workbench 
            b. fetch the data from the MYSQL to student frame 
                


        



 

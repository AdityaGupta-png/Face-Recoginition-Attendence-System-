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
        
# Making object 
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition_System(root)
    root.mainloop()
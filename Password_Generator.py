from tkinter import*
from random import randint
from tkinter import font
import tkinter



root = Tk()
root.title("Strong Password Generator")
root.iconbitmap(r'C:\Users\Amay\Downloads\fingerprint.ico')
root.geometry("500x300")




# Generate Random Strong  Password
def new_rand():

    # Clear the Outputbox
    pw_entry.delete(0,END)
    
    
    # Get PW length and convert into interger
    
    pw_length = int(my_entry.get())
    
    
    
    # Create a variable to hold the password
    my_password = ''
    
    
    # loop through password length 
    
    for x in range (pw_length):
        my_password +=chr(randint(32,126))
        
        
        
    # output password to the screen
    
    
    pw_entry.insert(0, my_password)
    
    
    
    
# Copy to the clipboard

def clipper():
    
    
    # clearing the clipboard
    root.clipboard_clear()
    
    # copy to the clipboard
    
    root.clipboard_append(pw_entry.get())
    
    
# label Frame

lf = LabelFrame(root, text = "How manny characters do you want ?")
lf.pack(pady=20)


# create Entry Box to Designate Number of Characters

my_entry = Entry(lf, font=("Helventica", 24))
my_entry.pack(pady=20, padx =20)



# Create a box for Our Returned Password


pw_entry = Entry(root, text= '', font =('Helventica', 24), bd = 0, bg ="systembuttonface")
pw_entry.pack(pady=20)


# create a frame for buttons

my_frame = Frame(root)
my_frame.pack(pady=20)



# Creating the Buttons

my_button = Button(my_frame, text = "Generate Strong Password", command=new_rand)
my_button.grid(row = 0, column=0,padx=10)


clipbutton = Button(my_frame, text="Copy to Clipboard",command=clipper)
clipbutton.grid(row = 0,column=1, padx=10)

root.mainloop()


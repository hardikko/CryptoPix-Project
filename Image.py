from tkinter import *
from tkinter import filedialog
from ImageLibrary import *
print("Welcome to CryptoPix's Image Enc/Dec System!!")
print("1.Encrypt")
print("2.Decrypt")
print("3.Exit")
choice=int(input("Enter your Choice: "))
if choice==2:
    root=Tk()
    root.title("CryptoPix")
    root.filename=filedialog.askopenfilename(initialdir=r"C:/",title="Select a File",filetypes=(("PNG Files ","*.png"),("JPG/JPEG Files ","*.jpg")))
    root.destroy()
    if "_Encrypt" not in root.filename:
        print("Not an Encrypted File !!")
        exit()
    imageDecrypt(root.filename)
    
    
elif choice==1:
    root=Tk()
    root.title("CryptoPix")
    root.filename=filedialog.askopenfilename(initialdir=r"C:/",title="Select a File",filetypes=(("PNG Files ","*.png"),("JPG/JPEG Files ","*.jpg")))
    root.destroy()
    imageEncrypt(root.filename)
elif choice==3:
    exit()
else:
    print("Invalid Choice!!")
    
    
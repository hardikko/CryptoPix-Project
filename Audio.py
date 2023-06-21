from pydub import AudioSegment
from tkinter import *
from tkinter import filedialog
from AudioLibrary import *
print("Welcome to CryptoPix's Audio Enc/Dec System!!")
print("1.Encrypt")
print("2.Decrypt")
print("3.Exit")
choice=int(input("Enter your Choice: "))
if choice==2:
    root=Tk()
    root.title("CryptoPix")
    root.filename=filedialog.askopenfilename(initialdir=r"C:/",title="Select a File",filetypes=("WAV Files ","*.wav"))
    root.destroy()
    if "_Encrypt" not in root.filename:
        print("Not an Encrypted File !!")
        exit()
    audioDecrypt(root.filename)
    
    
elif choice==1:
    root=Tk()
    root.title("CryptoPix")
    root.filename=filedialog.askopenfilename(initialdir=r"C:/",title="Select a File",filetypes=(("MP3 Files ","*.mp3"),("WAV Files ","*.wav")))
    root.destroy()
    if ".mp3" in root.filename:
        x=root.filename
        f=x.replace("mp3","wav")
        s=AudioSegment.from_mp3(x)
        s.export(f,format="wav")
        audioEncrypt(f)
    else:
        audioEncrypt(root.filename)
elif choice==3:
    exit()
else:
    print("Invalid Choice!!")
    
    
import os
from PIL import ImageTk,Image
from numpy import asarray,zeros,shape,full_like

def imageEncrypt(f):
    print("Initiating Image Encryption")
    img = Image.open(f)
    img=img.resize((800,800))
    ndata = asarray(img)
    z=0
    x=ndata.copy()
    y=ndata.copy()
    for r in range(1,800,10):
        for c in range(1,800,10):
            for i in range(r+2,r+9):
                for j in range(c+2,c+9):
                    x[i][j][0]=ndata[j][i][0]
                    x[i][j][1]=ndata[j][i][1]
                    x[i][j][2]=ndata[j][i][2]            
    for i in range(800):
        z=z+150
        for j in range(800):
            x[i][j][0]-=z
            x[i][j][1]-=z
            x[i][j][2]-=z
    data=Image.fromarray(x)
    if "jpg" in f:
        f=f.replace(".jpg","_Encrypt.png")
    else:
        f=f.replace(".png","_Encrypt.png")
    data.save(f)
    print("Encryption Successfull!!")
    
    
def imageDecrypt(f):
    print("Initiating Image Decryption")
    i=0
    j=0
    img = Image.open(f)
    ndata = asarray(img)
    z=0
    x=ndata.copy()
    f=f.replace("_Encrypt.png",".jpg")
    if not os.path.isfile(f):
        f=f.replace(".jpg",".png")  
    img = Image.open(f)
    img=img.resize((800,800))
    ndata = asarray(img)
    y=ndata.copy()
    for i in range(800):
        z=z+150
        for j in range(800):
            x[i][j][0]+=z
            x[i][j][1]+=z
            x[i][j][2]+=z  

    for r in range(1,800,10):
        for c in range(1,800,10):
            for i in range(r+2,r+9):
                for j in range(c+2,c+9):
                    y[j][i][0]=x[i][j][0]
                    y[j][i][1]=x[i][j][1]
                    y[j][i][2]=x[i][j][2]

    #print(ndata.shape)
    data=Image.fromarray(y)
    if "jpg" in f:
        f=f.replace(".jpg","_Decrypt.png")
    else:
        f=f.replace(".png","_Decrypt.png")
    data.save(f)
    print("Decryption Successfull !!")

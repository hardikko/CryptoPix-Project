import numpy as np
import librosa
from scipy.io.wavfile import read,write

def audioEncrypt(f):
    print("Initiating Audio Encryption")
    x,sr=librosa.load(f)
    sc = np.int16(x/np.max(np.abs(x))*32767)
    z=0
    for i in range(sc.shape[0]):
        if i%2:
            z=((z)**6)%32200
            sc[i]=sc[i]-z
            z+=4
        else:
            z=((z)**3)%32767
            sc[i]=sc[i]+z
            z+=4
    f=f.replace(".wav","_Encrypt.wav")
    write(f,sr,sc)
    print("Encryption Successfull!!")
    
    
def audioDecrypt(f):
    print("Initiating Audio Decryption")
    x,sr=librosa.load(f)
    dc = np.int16(x/np.max(np.abs(x))*32767)
    z=0
    for i in range(dc.shape[0]):
        if i%2:
            z=((z)**6)%32200
            dc[i]=dc[i]+z
            z+=4
        else:
            z=((z)**3)%32767
            dc[i]=dc[i]-z
            z+=4
    f=f.replace("Encrypt.wav","Decrypt.wav")
    write(f,sr,dc)
    print("Decryption Successfull !!")
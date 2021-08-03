from cryptography.fernet import Fernet
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# asymmertci decryption
msg=""
def symmetricdecryption(msg,h):
    msg=bytes(msg,'utf-8')
    print(msg)
    f=open(f'{h}','rb')
    g=Fernet(msg)
    encrypteddata=f.read()
    f.close()
    f=open(f'{h}','wb')
    f.write(g.decrypt(encrypteddata))
    f.close()
    Mbox('message', 'Done!'+'\n'+'NOTE: In case the result is wrong try using some higher value for the size.Ex-100,200 etc.', 1)
def asymmetricdecryption(n,d,cipher,h):
    global msg
    cipher=cipher.split()
    msg = ""
    parts = cipher
    n=int(n)
    d=int(d)
    for part in parts:
        if part:
            c = int(part)
            msg+=chr(pow(c,d,n)) 
    symmetricdecryption(msg,h)        
#symmetric decryption



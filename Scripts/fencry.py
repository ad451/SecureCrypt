from cryptography.fernet import Fernet
import key_generator
import codecs
import shutil
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#symmetric encryption
key=0
def asymmetricencryption(key,size):
    print(key)
    key=key.decode('utf-8')
    size=key_generator.key(size)
    f = open("keys.txt", "w")
    count=0
    for i in size[1]:
        if count==0:
          f.write("N :"+str(i))
        else:
          f.write("private key : "+str(i))
        count+=1  
        f.write('\n')
    
    e=size[0][1]
    f.write("public key : "+str(e))
    f.close()
    n=size[0][0]
    msg=key
    cipher = ""
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, n)) + " "
    g=open('cipher.txt','w')
    g.write(cipher)
    g.close()
    Mbox('message', 'Done! check the keys.txt file for using the keys and cipher.txt for the cipher message', 1)
def symmetricencryption(m,size):
    global key
    key=Fernet.generate_key()
    o=""
    for i in m[::-1]:
        if i=='.':
           break
        else:
            o+=i
    shutil.copy(f'{m}','backup'+'.'+o[::-1])        
    with codecs.open(f'{m}', 'r', encoding='utf-8',
                 errors='ignore') as f:
                 k=f.read()
    f.close()
    backup=open('backup.txt','w')
    backup.write(k)
    backup.close()
    f=open(f'{m}','rb')
    k=f.read()
    g=Fernet(key)
    f.close()
    encryteddata=g.encrypt(k)
    f=open(f'{m}','wb')
    f.write(encryteddata)
    f.close()
    asymmetricencryption(key,size)
#key asymmetric encryption


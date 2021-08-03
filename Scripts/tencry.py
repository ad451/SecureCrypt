import key_generator
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
def tencryption(size,text):
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
    msg=text
    cipher = ""
    for c in msg:
        m = ord(c)
        if str(pow(m,e,n))=='0':
          Mbox('error','Please provide a larger size for encryption.Ex-100,200 etc',1)
          break
        cipher += str(pow(m, e, n)) + " "
    g=open('cipher.txt','w')
    g.write(cipher)
    g.close()
    Mbox('message', 'Done! check the keys.txt file for using the keys and cipher.txt for the cipher message', 1)
    

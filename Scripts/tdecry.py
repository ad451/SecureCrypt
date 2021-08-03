import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
def tdecryption(n,cipher,d):
    msg = ""
    parts = cipher
    n=int(n)
    d=int(d)
    print(n)
    print(d)
    parts=parts.split()
    for part in parts:
        if part:
            c = int(part)
            msg+=chr(pow(c,d,n))
    l=open("decrypt_message.txt","w")
    l.write(msg)  
    l.close()
    Mbox('message', 'Done! check the decrypt_message.txt file for your message and in case you dont get your desired message try encrypting with a higher size. EX-100,200 etc ', 1)


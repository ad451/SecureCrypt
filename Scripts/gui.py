from tkinter import font, ttk
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilename
import tencry
import tdecry
import fencry
import fdecry
import ctypes
import os
import sys
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#root
root = Tk()
# all functions
root.geometry("400x670")
root.maxsize(400,670)
root.minsize(400,670)
filepath=""
def open_file():
    global filepath
    file=askopenfilename()
    if file is not None:
        filepath=file
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)        
def add_tab(event):
    alltabs=tabControl.tabs()
    if tabControl.select()==alltabs[-1]:
        Mbox('Help', 'Welcome to T&F Encryptor!'+'\n'+'\n'+
        'Below points can help you to get started with the application'+'\n'+'\n'+
        '1) The application provides encryption and decryption functionalities for text and files.'+'\n'+'\n'+
        '2) The Text tab helps you to encrypt and decrypt text based on rsa encryption.'+'\n'+'\n'+
        '3) The File tab helps you to  encrypt and decrypt files based on a combination of symmetric and asymmetric encryption methods.'+'\n'+'\n'+
        '4) All other steps are self-explanatory and as you go through the respective encryption process,you will '+
         'be explained what to do next once you are done with encryption or decryption.' +'\n'+'\n'+
         '5) NOTE-In case you dont get the correct result try using higher values for the size'+'\n'+'\n'+
         'Enjoy!!!', 1)        
def encrypt_file():
    if len(filepath)!=0:
        if sizef.get()<4:
            Mbox('error','enter a number greater than 3',1) 
        else:    
            fencry.symmetricencryption(filepath,sizef.get())     
def decrypt_file():
    if len(filepath)!=0:
       fdecry.asymmetricdecryption(nf.get(),keyf.get(),cipherf.get(),filepath)     
def Encrypt():
    if size.get()<4:
       Mbox('error','enter a number greater than 3',1) 
    else:   
       tencry.tencryption(size.get(),text.get())
def Decrypt():
    tdecry.tdecryption(n.get(),cipher.get(),key.get())
#creating tabs
root.title("T&F ENCRYPTOR")
# photo = PhotoImage(file = resource_path("key.png"))
# root.iconphoto(False, photo)
tabControl = ttk.Notebook(root)
  
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tabControl.add(tab1, text ='Text   ')
tabControl.add(tab2, text ='File   ')
tabControl.add(Frame(tabControl), text ='Help   ')

tabControl.pack(expand = 4, fill ="both")
tabControl.bind('<ButtonRelease-1>', add_tab)
#tab text 
#endcryption

Label(tab1, text ="ENCRYPTION",font="comicsansms 11 bold").grid(column = 0, row = 0,padx = 10,pady = 20) 
Label(tab1, text ="ENTER THE SIZE:",font="comicsansms 9 bold").grid(column = 0, row = 1,padx = 10,pady = 20)  
size = IntVar()
sizeE = Entry(tab1, textvariable = size)
sizeE.grid(row=1, column=1)
sizeE.delete(0, END)
Label(tab1, text ="ENTER THE TEXT:",font="comicsansms 9 bold").grid(column = 0, row = 2,padx = 10,pady = 20)  
text = StringVar()
textE = Entry(tab1, textvariable = text)
textE.grid(row=2, column=1)
Button(tab1,text="Encrypt",command=Encrypt).grid(column=0,row=3,padx=10,pady=20)
#decryption
Label(tab1, text ="DECRYPTION",font="comicsansms 11 bold").grid(column = 0, row = 4,padx = 10,pady = 20) 
Label(tab1, text ="ENTER THE CIPHER:",font="comicsansms 9 bold").grid(column = 0, row = 5,padx = 10,pady = 20)  
cipher = StringVar()
cipherD = Entry(tab1, textvariable = cipher)
cipherD.grid(row=5, column=1)
Label(tab1, text ="ENTER THE KEY:",font="comicsansms 9 bold").grid(column = 0, row = 6,padx = 10,pady = 20)  
key = StringVar()
keyD = Entry(tab1, textvariable = key)
keyD.grid(row=6, column=1)
Label(tab1, text ="ENTER THE VALUE of N:",font="comicsansms 9 bold").grid(column = 0, row = 7,padx = 10,pady = 20)  
n = StringVar()
nD = Entry(tab1, textvariable = n)
nD.grid(row=7, column=1)
Button(tab1,text="Decrypt",command=Decrypt).grid(column=0,row=8,padx=10,pady=20)
#tab file
#encryption
Label(tab2, text ="ENCRYPTION",font="comicsansms 11 bold").grid(column = 0,row = 0, padx = 10,pady = 20)
Label(tab2, text ="ENTER THE SIZE:",font="comicsansms 9 bold").grid(column = 0, row = 1,padx = 10,pady = 20)  
sizef = IntVar()
sizeE = Entry(tab2, textvariable = sizef)
sizeE.delete(0, END)
sizeE.grid(row=1, column=1)
Button(tab2, text ='Select File', command = lambda:open_file()).grid(column=0,row=2,padx=10,pady=20)
Button(tab2,text="Encrypt",command=encrypt_file).grid(column=0,row=3,padx=10,pady=20)
#decryption

Label(tab2, text ="DECRYPTION",font="comicsansms 11 bold").grid(column = 0,row = 4, padx = 10,pady = 20)

Label(tab2, text ="ENTER THE CIPHER:",font="comicsansms 9 bold").grid(column = 0, row = 5,padx = 10,pady = 20)  
cipherf = StringVar()
cipherD = Entry(tab2, textvariable = cipherf)
cipherD.grid(row=5, column=1)

Label(tab2, text ="ENTER THE KEY:",font="comicsansms 9 bold").grid(column = 0, row = 6,padx = 10,pady = 20)  
keyf = StringVar()
keyD = Entry(tab2, textvariable = keyf)
keyD.grid(row=6, column=1)

Label(tab2, text ="ENTER THE VALUE of N:",font="comicsansms 9 bold").grid(column = 0, row = 7,padx = 10,pady = 20)  
nf= StringVar()
nD = Entry(tab2, textvariable = nf)
nD.grid(row=7, column=1)

Button(tab2, text ='Select File', command = lambda:open_file()).grid(column=0,row=8,padx=10,pady=20)
Button(tab2,text="Decrypt",command=decrypt_file).grid(column=0,row=9,padx=10,pady=20)

root.mainloop()
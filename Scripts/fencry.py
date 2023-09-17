from cryptography.fernet import Fernet
import key_generator
import codecs
import shutil
import ctypes

def show_message(title, text, style):
    """Show a message box."""
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# Asymmetric encryption
def asymmetric_encryption(text, size):
    try:
        key=text.decode('utf-8')
        size = key_generator.generate_rsa_key(size)
        f = open("keys.txt", "w")
        count=0
        for i in size[1]:
            if count==0:
               f.write("N :"+str(i))
            else:
               f.write("private key : "+str(i))
            count+=1  
            f.write('\n')
    
        
        e = size[0][1]
        n = size[0][0]
        f.write("public key : "+str(e))
        f.close()
        cipher = " ".join(str(pow(ord(c), e, n)) for c in key)
        
        with open('cipher.txt', 'w') as cipher_file:
            cipher_file.write(cipher)
        
        show_message('Message', 'Done! Check the keys.txt file for keys and cipher.txt for the cipher message', 1)
    
    except Exception as e:
        show_message('Error', f'An error occurred: {str(e)}', 0)

# Symmetric encryption
def symmetric_encryption(file_path, size):
    try:
        global key
        key=Fernet.generate_key()
        o=""
        for i in file_path[::-1]:
            if i=='.':
                break
            else:
                o+=i
        shutil.copy(f'{file_path}','backup'+'.'+o[::-1])        
        with codecs.open(f'{file_path}', 'r', encoding='utf-8',
                    errors='ignore') as f:
                    k=f.read()
        f.close()
        
        #creating the backup file
        backup=open('backup.txt','w')
        backup.write(k)
        backup.close()
        
        f=open(f'{file_path}','rb')
        k=f.read()
        g=Fernet(key)
        f.close()
        encryteddata=g.encrypt(k)
        
        f=open(f'{file_path}','wb')
        f.write(encryteddata)
        f.close()
        
        asymmetric_encryption(key, size)
    
    except Exception as e:
        show_message('Error', f'An error occurred: {str(e)}', 0)

# Example usage:
# symmetric_encryption(file_path, size)

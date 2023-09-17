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
        key = text.encode('utf-8')
        size = key_generator.key(size)
        
        with open("keys.txt", "w") as key_file:
            key_file.write(f"N: {size[0][0]}\n")
            key_file.write(f"Public Key: {size[0][1]}\n")
            key_file.write(f"Private Keys: {', '.join(map(str, size[1]))}\n")
        
        e = size[0][1]
        n = size[0][0]
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
        key = Fernet.generate_key()
        file_name = file_path.split(".")[0]
        backup_file_name = f'backup.{file_name[::-1]}'
        
        shutil.copy(file_path, backup_file_name)
        
        with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            data = file.read()
        
        with open(file_path, 'rb') as file:
            original_data = file.read()
            cipher = Fernet(key).encrypt(original_data)
        
        with open(file_path, 'wb') as file:
            file.write(cipher)
        
        asymmetric_encryption(key, size)
    
    except Exception as e:
        show_message('Error', f'An error occurred: {str(e)}', 0)

# Example usage:
# symmetric_encryption(file_path, size)

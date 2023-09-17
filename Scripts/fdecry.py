from cryptography.fernet import Fernet
import ctypes

def show_message(title, text, style):
    """Show a message box."""
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def symmetric_decryption(msg, file_path):
    """Decrypt data using symmetric encryption and write to a file."""
    try:
        msg_bytes = bytes(msg, 'utf-8')
        print(msg_bytes)

        with open(file_path, 'rb') as file:
            key = Fernet(msg_bytes)
            encrypted_data = file.read()

        with open(file_path, 'wb') as file:
            file.write(key.decrypt(encrypted_data))

        show_message('Message', 'Done!\nNOTE: In case the result is wrong, try using a higher value for the size. Ex: 100, 200, etc.', 1)

    except Exception as e:
        show_message('Error', f'An error occurred: {str(e)}', 0)

def asymmetric_decryption(n, d, cipher, file_path):
    """Decrypt data using asymmetric encryption and then call symmetric decryption."""
    try:
        cipher_parts = cipher.split()
        msg = ""
        n = int(n)
        d = int(d)

        for part in cipher_parts:
            if part:
                c = int(part)
                msg += chr(pow(c, d, n))

        symmetric_decryption(msg, file_path)

    except Exception as e:
        show_message('Error', f'An error occurred: {str(e)}', 0)

# Example usage:
# asymmetric_decryption(n_value, d_value, cipher_text, file_path)

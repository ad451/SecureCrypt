import ctypes  # An included library with Python install.

def show_message(title, text, style):
    """
    Show a message box with the given title and text.

    Args:
        title (str): The title of the message box.
        text (str): The message text to display.
        style (int): The style of the message box.

    Returns:
        int: The result of the message box operation.
    """
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def text_decryption(modulus, cipher_text, private_key):
    """
    Decrypt a cipher text using RSA decryption.

    Args:
        modulus (str): The modulus (n) used in RSA encryption.
        cipher_text (str): The cipher text to decrypt.
        private_key (str): The private key (d) used in RSA decryption.

    Writes:
        A text file named "decrypt_message.txt" containing the decrypted message.
    """
    decrypted_message = ""
    cipher_parts = cipher_text.split()
    modulus = int(modulus)
    private_key = int(private_key)

    for part in cipher_parts:
        if part:
            c = int(part)
            decrypted_message += chr(pow(c, private_key, modulus))

    with open("decrypt_message.txt", "w") as file:
        file.write(decrypted_message)

    show_message('Message', 'Done! Check the "decrypt_message.txt" file for your message. In case you don\'t get your desired message, try encrypting with a higher size (e.g., 100, 200, etc.).', 1)

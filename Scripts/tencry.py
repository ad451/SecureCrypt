import key_generator
import ctypes

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

def text_encryption(key_size, text):
    """
    Encrypt text using RSA encryption.

    Args:
        key_size (int): The desired key size for encryption.
        text (str): The text to encrypt.

    Writes:
        - A text file named "keys.txt" containing keys (public and private).
        - A text file named "cipher.txt" containing the cipher text.

    Displays:
        - A message box with a success message.
        - A message box with an error message if encryption fails.

    Notes:
        If the result of pow(m, e, n) is zero, an error message is displayed.
    """
    size = key_generator.generate_rsa_key(key_size)

    with open("keys.txt", "w") as key_file:
        count = 0
        for i in size[1]:
            if count == 0:
                key_file.write("N: " + str(i))
            else:
                key_file.write("Private Key: " + str(i))
            count += 1
            key_file.write('\n')

        e = size[0][1]
        key_file.write("Public Key: " + str(e))

    n = size[0][0]
    msg = text
    cipher = ""

    for c in msg:
        m = ord(c)
        encrypted = pow(m, e, n)

        if encrypted == 0:
            show_message('Error', 'Please provide a larger size for encryption. Ex: 100, 200, etc.', 1)
            return

        cipher += str(encrypted) + " "

    with open('cipher.txt', 'w') as cipher_file:
        cipher_file.write(cipher)

    show_message('Message', 'Done! Check the "keys.txt" file for keys and "cipher.txt" for the cipher message.', 1)

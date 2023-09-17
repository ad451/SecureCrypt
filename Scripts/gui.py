import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tencry
import tdecry
import fencry
import fdecry
from ttkthemes import ThemedTk

def open_file(select_file_button):
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if filepath:
        select_file_button.config(text="File Selected")

def encrypt_text():
    size_value = size_var.get()
    text_value = text_var.get()
    if size_value < 4:
        messagebox.showerror("Error", "Enter a number greater than 3")
    else:
        encrypted_text = tencry.tencryption(size_value, text_value)
        cipher_text.delete(0, tk.END)
        cipher_text.insert(0, encrypted_text)

def decrypt_text():
    cipher_value = cipher_var.get()
    key_value = key_var.get()
    n_value = n_var.get()
    decrypted_text = tdecry.tdecryption(n_value, cipher_value, key_value)
    text_var.set(decrypted_text)

def encrypt_file():
    size_value = file_size_var.get()
    if not filepath:
        messagebox.showerror("Error", "Please select a file to encrypt")
    elif size_value < 4:
        messagebox.showerror("Error", "Enter a number greater than 3")
    else:
        fencry.symmetricencryption(filepath, size_value)

def decrypt_file():
    cipher_value = file_cipher_var.get()
    key_value = file_key_var.get()
    n_value = file_n_var.get()
    fdecry.asymmetricdecryption(n_value, key_value, cipher_value, filepath)

# Create the main window with a modern theme
root = ThemedTk(theme="arc")
root.title("T&F Encryptor")
root.geometry("400x670")
root.minsize(400, 670)

# Create a notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# Text tab
text_tab = ttk.Frame(notebook)
notebook.add(text_tab, text="Text")

# Encryption section
text_encrypt_frame = ttk.LabelFrame(text_tab, text="Encryption")
text_encrypt_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

size_var = tk.IntVar()
text_var = tk.StringVar()
size_var.set('') 
size_label = ttk.Label(text_encrypt_frame, text="Enter the Size:", font=("Helvetica", 12, "bold"))
text_label = ttk.Label(text_encrypt_frame, text="Enter the Text:", font=("Helvetica", 12, "bold"))
size_entry = ttk.Entry(text_encrypt_frame, textvariable=size_var, font=("Helvetica", 12))
text_entry = ttk.Entry(text_encrypt_frame, textvariable=text_var, font=("Helvetica", 12))
encrypt_button = ttk.Button(text_encrypt_frame, text="Encrypt", command=encrypt_text, style="Bold.TButton")

size_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
size_entry.grid(row=0, column=1, padx=5, pady=5)
text_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
text_entry.grid(row=1, column=1, padx=5, pady=5)
encrypt_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Decryption section
text_decrypt_frame = ttk.LabelFrame(text_tab, text="Decryption")
text_decrypt_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

cipher_var = tk.StringVar()
key_var = tk.StringVar()
n_var = tk.StringVar()
cipher_label = ttk.Label(text_decrypt_frame, text="Enter the Cipher:", font=("Helvetica", 12, "bold"))
cipher_entry = ttk.Entry(text_decrypt_frame, textvariable=cipher_var, font=("Helvetica", 12))
key_label = ttk.Label(text_decrypt_frame, text="Enter the Key:", font=("Helvetica", 12, "bold"))
key_entry = ttk.Entry(text_decrypt_frame, textvariable=key_var, font=("Helvetica", 12))
n_label = ttk.Label(text_decrypt_frame, text="Enter the Value of N:", font=("Helvetica", 12, "bold"))
n_entry = ttk.Entry(text_decrypt_frame, textvariable=n_var, font=("Helvetica", 12))
decrypt_button = ttk.Button(text_decrypt_frame, text="Decrypt", command=decrypt_text, style="Bold.TButton")

cipher_label.grid(row=0, column=0, padx=5, pady=5)
cipher_entry.grid(row=0, column=1, padx=5, pady=5)
key_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
key_entry.grid(row=1, column=1, padx=5, pady=5)
n_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
n_entry.grid(row=2, column=1, padx=5, pady=5)
decrypt_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# File tab
file_tab = ttk.Frame(notebook)
notebook.add(file_tab, text="File")

# File encryption section
file_encrypt_frame = ttk.LabelFrame(file_tab, text="File Encryption")
file_encrypt_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

file_size_var = tk.IntVar()
file_size_var.set('') 
file_size_label = ttk.Label(file_encrypt_frame, text="Enter the Size:", font=("Helvetica", 12, "bold"))
file_size_entry = ttk.Entry(file_encrypt_frame, textvariable=file_size_var, font=("Helvetica", 12))
select_file_button_encrypt = ttk.Button(file_encrypt_frame, text="Select File", command=lambda: open_file(select_file_button_encrypt), style="Bold.TButton")
encrypt_file_button = ttk.Button(file_encrypt_frame, text="Encrypt", command=encrypt_file, style="Bold.TButton")

file_size_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
file_size_entry.grid(row=1, column=1, padx=5, pady=5)
select_file_button_encrypt.grid(row=2, column=0, padx=5, pady=5)
encrypt_file_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# File decryption section
file_decrypt_frame = ttk.LabelFrame(file_tab, text="File Decryption")
file_decrypt_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

file_cipher_var = tk.StringVar()
file_key_var = tk.StringVar()
file_n_var = tk.StringVar()

file_cipher_label = ttk.Label(file_decrypt_frame, text="Enter the Cipher:", font=("Helvetica", 12, "bold"))
file_cipher_entry = ttk.Entry(file_decrypt_frame, textvariable=file_cipher_var, font=("Helvetica", 12))
file_key_label = ttk.Label(file_decrypt_frame, text="Enter the Key:", font=("Helvetica", 12, "bold"))
file_key_entry = ttk.Entry(file_decrypt_frame, textvariable=file_key_var, font=("Helvetica", 12))
file_n_label = ttk.Label(file_decrypt_frame, text="Enter the Value of N:", font=("Helvetica", 12, "bold"))
file_n_entry = ttk.Entry(file_decrypt_frame, textvariable=file_n_var, font=("Helvetica", 12))
decrypt_file_button = ttk.Button(file_decrypt_frame, text="Decrypt", command=decrypt_file, style="Bold.TButton")
select_file_button_decrypt = ttk.Button(file_decrypt_frame, text="Select File", command=lambda: open_file(select_file_button_decrypt), style="Bold.TButton")

file_cipher_label.grid(row=0, column=0, padx=5, pady=5)
file_cipher_entry.grid(row=0, column=1, padx=5, pady=5)
file_key_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
file_key_entry.grid(row=1, column=1, padx=5, pady=5)
file_n_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
file_n_entry.grid(row=2, column=1, padx=5, pady=5)
decrypt_file_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
select_file_button_decrypt.grid(row=3, column=0, padx=5, pady=5)

# Help tab
help_tab = ttk.Frame(notebook)
notebook.add(help_tab, text="Help")

help_text = """
Welcome to T&F Encryptor!

This application provides encryption and decryption functionalities for text and files.

Text Tab:
1) Enter the size and text for encryption.
2) Click 'Encrypt' to encrypt the text.
3) For decryption, enter the cipher, key, and N value, then click 'Decrypt'.

File Tab:
1) Select a file and enter the size for encryption.
2) Click 'Encrypt' to encrypt the file.
3) For decryption, enter the cipher, key, and N value, then click 'Decrypt'.

Note: For both text and file encryption, the size should be greater than 3.

Enjoy!
"""

help_label = ttk.Label(help_tab, text=help_text, wraplength=350, justify=tk.LEFT, font=("Helvetica", 12))
help_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a custom style for bold buttons
style = ttk.Style()
style.configure("Bold.TButton", font=("Helvetica", 12, "bold"))

# Start the main loop
root.mainloop()

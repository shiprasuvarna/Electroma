import tkinter as tk

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "1234":
        login_status.config(text="Login successful!")
    else:
        login_status.config(text="Invalid username or password.")

root = tk.Tk()
root.title("Login Page")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack()

login_status = tk.Label(root, text="")
login_status.pack()

root.mainloop()

# import re
# minyons_1 ="Minyon MiNyon MinYon MinyoN minyon mInyon MiNYon MINyon MInYon MInyOn MINYon"
# minyons_2 ="Minyon MiNyon MinYon MinyoN minyon  Bob mInyon MiNYon MINyon Bob MInYon MInyOn Bob MINYon"
# Bob = re.compile("Bob") 
# a = Bob.finditer(minyons_1)
# for item in a:
#     print(f"a: {item}")
# b = Bob.finditer(minyons_2)
# for item in b:
#     print(f"b: {item}")

# a = Bob.findall(minyons_1)
# b = Bob.findall(minyons_2)
# print(a)
# print(b)
# minyons ="Minyon MiNyon MinYon MinyoN minyon Bob mInyon MiNYon MINyon MInYon MInyOn MINYon"
# kevin = Bob.sub("Kevin", minyons)
# print(kevin)

import tkinter as tk
import re 

login_pattern = re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
password_pattern = re.compile(r"^\w{8,16}$")
root = tk.Tk()
root.geometry("400x250+700+500")
root.resizable(False, False)
def logining():
    login = login_entry.get()
    password = password_entry.get()
    if login_pattern.search(login):
        if password_pattern.search(password):
            login_entry.config(bg="green")
            password_entry.config(bg="green")
        else:
             login_entry.config(bg="red")
             password_entry.config(bg="red")
    else:
             login_entry.config(bg="red")
             password_entry.config(bg="red")

login_label = tk.Label(root, text="Login", font=("Arial", 14), padx=50)
password_label = tk.Label(root, text="Password", font=("Arial", 14), padx=50)
login_entry = tk.Entry(root, font=("Arial", 12), width=20)
password_entry = tk.Entry(root, font=("Arial", 12), width=20, show="*")
login_button = tk.Button(root, text="LOGING", font=("Arial", 16), width=12, command=logining)
root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(0, minsize=90)
login_button.grid(columnspan=2)

login_label.grid(column = 0, row=0, sticky="w")
password_label.grid(column = 0, row=1, sticky="w")
login_entry.grid(column = 1, row=0, sticky="w")
password_entry.grid(column = 1, row=1, sticky="w")
login_button.grid(column = 0, row=2)
root.mainloop()

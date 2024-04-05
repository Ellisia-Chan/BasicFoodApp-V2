import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
import os

# Color Palette: https://colorhunt.co/palette/b3c8cfbed7dcf1eedce5ddc5

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Food App")
        self.geometry("500x400")
        self.resizable(False, False)
        self.config(bg="#B3C8CF")

        self.create_login_widgets()

    def create_login_widgets(self):
        # Config grid
        self.columnconfigure((1, 2, 3), weight=2)
        self.columnconfigure((0, 4), weight=1)
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=10)
        
        # Label Title
        lbl_title = tk.Label(self, text="Basic Food App", font=("Arial", 18, BOLD), bg="#B3C8CF")
        lbl_title.grid(row=0, column=0, columnspan=5, sticky='n', pady=10)

        # Frame
        frame = tk.Frame(self, bg="white", bd=3, relief=tk.GROOVE)
        frame.grid(row=1, column=1, columnspan=3, sticky="nsew")

        # Label
        lbl_login = tk.Label(frame, text="Login", font=("Arial", 18), bg="white")
        lbl_usesrname = tk.Label(frame, text="Username:", font=("Arial", 16), bg="white")
        lbl_password = tk.Label(frame, text="Password:", font=("Arial", 16), bg="white")

        # Label pos
        lbl_login.place(x=150, y=20)
        lbl_usesrname.place(x=20, y=80)
        lbl_password.place(x=20, y=120)

        # Entry
        self.ent_username = tk.Entry(frame, width=18, font=("Arial", 16), bd=3, relief=tk.GROOVE)
        self.ent_password = tk.Entry(frame, width=18, font=("Arial", 16), bd=3, relief=tk.GROOVE, show="*")
        self.ent_password.bind('<Return>', lambda event: self.enter())

        # Entry pos
        self.ent_username.place(x=130, y=80)
        self.ent_password.place(x=130, y=120)

        # Button
        btn_enter = tk.Button(frame, text="Enter", font=("Arial", 16), bg="#BED7DC", width=12, command=self.enter)
        btn_enter.place(x=110, y=190)

    def enter(self):
        # Const
        credentials = False

        # Get Info
        username = self.ent_username.get()
        password = self.ent_password.get()


        # Get path of the main script and join the data
        script_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(script_dir, "data.txt")

        # Get data from file and check username and password to enter
        if username != "" and password != "":
            with open(file_path, "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(",")
                    if username == stored_username and password == stored_password:
                        credentials = True
                        break

            if credentials:
                if username == "admin":
                    self.destroy()
                    win = Window()
                    win.mainloop() 
                else:
                    self.destroy()
                    win = Window()
                    win.mainloop()                                         
            else:
                messagebox.showwarning("Error", "Incorrect username or password")    
        else:
            messagebox.showwarning("Empty Field", "Please Fill Out The Fields")

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Food App")
        self.geometry("850x500")
        self.resizable(False, False)
        self.config(bg="#B3C8CF")

        self.frame()

    def frame(self):
        #Frame
        frame1 = tk.Frame(self, width=400, height=450, bd=5, relief=tk.GROOVE, bg="#F1EEDC")
        frame2 = tk.Frame(self, width=380, height=450, bd=5, relief=tk.GROOVE, bg="#F1EEDC")

        #Frame pos
        frame1.place(x=20, y=20)
        frame2.place(x=450, y=20)


app = Login()
app.mainloop()

# For Debugging
# app = Window()
# app.mainloop()
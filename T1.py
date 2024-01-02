import tkinter
from tkinter import messagebox
root = tkinter.Tk()

#Login button function 
def submit_form():
    username = usernameentry.get()
    password = passwordentry.get()

    if username and password:
        messagebox.showinfo("Success", "Registration successful!\nUsername: {}\nPassword: {}".format(username, password))
    else:
        messagebox.showerror("Error", "Please fill in both username and password fields.")


#gui title
root.title("Registration Form")
root.geometry("2048x1536")
root.configure(bg='grey')

#with in a frame
f = tkinter.Frame(bg='grey')



#creating_widgets
login = tkinter.Label(f, text = 'Registration Form', font=("Arial", 25), fg='white', bg='grey')
username = tkinter.Label(f, text = 'Username', font=("Arial", 16), fg='white', bg='grey')
usernameentry = tkinter.Entry(f, font=("Arial", 16))
passwordentry = tkinter.Entry(f, show='*', font=("Arial", 16))
password = tkinter.Label(f, text = 'Password', font=("Arial", 16), fg='white', bg='grey')
loginbutton = tkinter.Button(f, text = 'Submit', font=("Arial", 16), command=submit_form, fg='black', bg='white')


#placing widgets
login.grid(row=0, column=0, columnspan=2, pady=40)
username.grid(row=1, column=0)
usernameentry.grid(row=1, column=1,  pady=10)
password.grid(row=2, column=0)
passwordentry.grid(row=2, column=1, pady=10)
loginbutton.grid(row=3, column=0, columnspan=2, pady=30)

#packing the frame to the center
f.pack()
root.mainloop()
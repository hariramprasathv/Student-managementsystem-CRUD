from tkinter import *
from tkinter import messagebox
from PIL import ImageTk



def login():
    if passwordEntry.get()=='' or usernameEntry.get()=='':
        messagebox.showerror(title='ERROR',message='Fields cannot be empty')
    elif passwordEntry.get()=='1234' and usernameEntry.get()=='hari':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error','Please enter correct credentials')

window=Tk()

window.geometry('1280x700+0+0')
window.title('Login System of student managemnet system')

window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')
bglabel = Label(window,image = backgroundImage)
bglabel.place(x=0,y=0)

loginFrame = Frame(window,bg='dodgerblue4')
loginFrame.place(x=400,y=190)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame,image= logoImage)
logoLabel.grid (row=0,column=0,columnspan=2,pady=10)

usernameImage = PhotoImage(file= 'user.png')
usernameLabel = Label(loginFrame,image= usernameImage , text='UserName', compound=LEFT, font= ('times new roman',20,'bold'),bg='dodgerblue4')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry = Entry(loginFrame,font= ('times new roman',20,'bold'),bd=5,fg='black')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage = PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text= ' Password',compound=LEFT,font=('times new roman',20,'bold'),bg='dodgerblue4')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='black')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',width=15,font=('times new roman',14,'bold'),fg='white',bg='royalblue',activebackground='royalblue',activeforeground='white',cursor='hand2',command=login)

loginButton.grid(row=3,column=1)

window.mainloop()
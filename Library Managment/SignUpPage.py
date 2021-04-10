from tkinter import *
from tkinter import messagebox
from mysql import connector


class SignUpPage:

    def goBack(self):
        self.signUpRoot.destroy()

    def next(self):
        if self.confirmPassVar.get() != self.passVar.get():
            messagebox.showerror("!", "Password didn't match!")
        else:
            query = 'insert into User (UserName,Password) values(%s,%s);'
            values = (self.userVar.get(), self.passVar.get())
            self.myCursor.execute(query, values)
            self.myDb.commit()
            messagebox.showinfo("", 'Account created successfully.')
            self.signUpRoot.destroy()

    def __init__(self):
        self.myDb = connector.connect(host='localhost', user='root'
                                      , password='1234', port=3307, database='library')
        self.myCursor = self.myDb.cursor()

        self.signUpRoot = Tk('450x300')
        self.signUpRoot.minsize(450, 300)
        self.signUpRoot.maxsize(450, 300)
        self.signUpRoot.title("Sign Up")

        signUpLabel = Label(self.signUpRoot, text='Sign Up', fg='green', font='normal 30 bold')
        signUpLabel.place(x=150, y=24)

        frame1 = Frame(self.signUpRoot, width=450, height=150)
        frame1.place(x=0, y=100)

        userLabel = Label(frame1, text='User Name', font='normal 17 bold')
        passLabel = Label(frame1, text='Password', font='normal 17 bold')
        confPassLable = Label(frame1, text='Confirm Pass', font='normal 17 bold')


        self.userVar = StringVar()
        self.passVar = StringVar()
        self.confirmPassVar = StringVar()

        userEntry = Entry(frame1, textvariable=self.userVar, width=40)
        passEntry = Entry(frame1, textvariable=self.passVar, width=40, show='*')
        confPassEntry = Entry(frame1, textvariable=self.confirmPassVar, width=40, show='*')


        userLabel.grid(row=0, column=0)
        userEntry.grid(row=0, column=1)
        passLabel.grid(row=1, column=0)
        passEntry.grid(row=1, column=1)
        confPassLable.grid(row=2, column=0)
        confPassEntry.grid(row=2, column=1)

        nextButton = Button(self.signUpRoot, text='Next', bg='sky blue', fg='white', command=self.next)
        nextButton.place(x=30, y=220, width=100, height=40)

        backButton = Button(self.signUpRoot, text='Back', bg='green', fg='white', command=self.goBack)
        backButton.place(x=160, y=220, width=100, height=40)

        self.signUpRoot.mainloop()

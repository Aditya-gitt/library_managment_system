from SignUpPage import SignUpPage
from tkinter import *
from PIL import ImageTk
from PIL import Image
#from mysql import connector

class LoginPage:

    def createAccount(self,event):
        self.root.destroy()
        SignUpPage()
        LoginPage()

    def __init__(self):

        self.root  = Tk('380x420')
        self.root.title("Log in")
        self.root.minsize(340,420)
        self.root.maxsize(340,420)
        self.root.configure(bg='medium aquamarine')

        userLabel = Label(self.root ,text = 'User Name',font = "comicscasm 30 bold"
                          ,bg = 'medium aquamarine')
        userLabel.pack(anchor = 'nw',padx = 20, pady = 30 )
        passLabel = Label(self.root , text='Password', font="comicscasm 30 bold"
                          ,bg = 'medium aquamarine')
        passLabel.place(x = 20,y = 130)

        self.userVar = StringVar()
        self.passVar = StringVar()

        userEntry = Entry(self.root  , textvariable = self.userVar,bg = 'light gray'
                          ,highlightcolor = 'blue')

        userEntry.place(x = 20,y = 80,width = 300,height = 30)
        passEntry = Entry(self.root , textvariable= self.passVar,bg = 'light gray',show="*")

        passEntry.place(x=20,y = 180,width = 300,height = 30)
        image = Image.open('Login button.png')
        image = image.resize((204, 40), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)

        signInButton = Button(text = 'Sign In',image = img,cursor = 'hand2')
        signInButton.place(x=68,y = 260,width = 204,height = 40)
        #signInButton.bind()

        createAccButton = Label(text = "create new account",fg = 'blue',cursor = 'hand2',
                                font = 'comicscasm 10 underline',bg = 'medium aquamarine'
                                )
        createAccButton.place(x = 20,y = '320')
        createAccButton.bind('<Button-1>',self.createAccount)

        self.root .mainloop()



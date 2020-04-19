from tkinter import *
from PIL import ImageTk as itk
import tkinter.font as tkfont
# from tkinter import ttk

class login_UI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login") #set ui title
        self.root.geometry("500x300") #set ui height and width
        self.photo = itk.PhotoImage(file = "background.png")
        self.background = Label(self.root, image=self.photo)
        self.background.pack()#put background photo in window
        self.root.resizable(0,0)#fix window size
        self.Login()
        self.openWindow = []#show window is opened

    def Login(self):
        #set front title in Login ui
        font1 = tkfont.Font(family='Fixdsys',size = 20,weight=tkfont.BOLD)
        Label(self.root, text = 'Welcome to Chat',fg='#1E90FF',font = font1).place(x=170,y=30)
        #label the username and Password
        Label(self.root, text='Username:', fg='#1E90FF').place(x=80, y=92)
        Label(self.root, text='Password:', fg='#1E90FF').place(x=80, y=142)
        # get input for usename and password
        usenameInput = Entry(self.root)
        usenameInput.place(x = 160,y=90)
        passwordInput = Entry(self.root,show = "*")
        passwordInput.place(x = 160,y=140)
        #set button for Register,Change Password and Login
        Button(self.root, text="Register",command = self.Resgister,fg='#1E90FF').place(x=360, y=93)
        Button(self.root, text="Change Password", command=self.changePassword,fg='#1E90FF').place(x=360, y=143)
        Button(self.root, text="Login", width = 10, height = 2, fg='#1E90FF').place(x=200, y=200)

    def closeWindow(self):
        self.openWindow[0].destroy()
        del self.openWindow[0]

    def Resgister(self):
        self.register = Toplevel()
        self.register.geometry("500x300")
        self.register.title("Register")
        #设置register页面背景图
        self.photo2 = itk.PhotoImage(file = "background2.png")
        canvas = Canvas(self.register,width = 500, height = 300)#设置背景图片大小
        canvas.config(highlightthickness=0)# 设置无白边距（用canvs会出现有白边距情况）
        canvas.create_image(100,300,image = self.photo2)#利用canvas截取背景图的一块
        canvas.pack()
        self.register.resizable(0, 0)#固定window的大小
        #注册信息
        Label(self.register, text='Username:',fg='#1E90FF').place(x=80, y=52)
        Label(self.register, text='Password:',fg='#1E90FF').place(x=80, y=102)
        Label(self.register, text='Repeat password:',fg='#1E90FF').place(x=80, y=152)
        usenameReg = Entry(self.register)
        usenameReg.place(x = 160,y=50)
        passwordReg = Entry(self.register,show = "*")
        passwordReg.place(x = 160,y=100)
        Reqeatpassword = Entry(self.register, show="*")
        Reqeatpassword.place(x=210, y=150)
        #提交按钮
        Button(self.register, text = "Submit",width = 10, height = 2, fg='#1E90FF').place(x=200,y=200)

    def changePassword(self):
        self.ChangePassword = Toplevel()
        self.ChangePassword.geometry("500x300")
        self.ChangePassword.title("Change Password")
        self.photo3 = itk.PhotoImage(file = "background3.png")
        canvas = Canvas(self.ChangePassword,width = 500, height = 300)
        canvas.config(highlightthickness=0)
        canvas.create_image(200,200,image = self.photo3)
        canvas.pack()
        self.ChangePassword.resizable(0, 0)
        Label(self.ChangePassword, text='Username:',fg='#1E90FF').place(x=80, y=52)
        Label(self.ChangePassword, text='Current Password:',fg='#1E90FF').place(x=80, y=102)
        Label(self.ChangePassword, text='Change password:',fg='#1E90FF').place(x=80, y=152)
        usenameCurr = Entry(self.ChangePassword)
        usenameCurr.place(x = 160,y=50)
        passwordCurr = Entry(self.ChangePassword,show = "*")
        passwordCurr.place(x = 210,y=100)
        passwordChange = Entry(self.ChangePassword, show="*")
        passwordChange.place(x=210, y=150)
        Button(self.ChangePassword, text="Submit", width=10, height=2, fg='#1E90FF').place(x=200, y=200)
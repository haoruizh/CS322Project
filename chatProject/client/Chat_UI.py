from tkinter import scrolledtext
from chatProject.client.login_UI import *

class Chat_UI:
    def __init__(self,data):
        self.root = Tk()
        self.data = data
        for id,friendlist in data.items():
            self.myid = id
            self.myfriendList = friendlist
        self.root.geometry("250x600+900+50")
        self.root.resizable(0,0)
        self.root.title(self.myid + " contact list")
        self.friendList_bg = itk.PhotoImage(file = "background4.png")
        self.mainBg = itk.PhotoImage(file="background4.png")
        # self.friendListUI = Label(self.root, image=self.friendList_bg)
        # self.friendListUI.configure(highlightthickness=0)
        # self.friendListUI.place(x = 0,y = 0)
        self.meau = Menu(self.root,tearoff = 0)
        self.meau.add_command(label = "Delete friend")
        self.friendList_Ui()

    def menu(self,event):
        self.meau.post(event.x_root, event.y_root)

    def friendList_Ui(self):
        meau = Menu(self.root,tearoff = 0)
        meau.add_command(label = "Delete friend")
        # friendlistscroll = scrolledtext.ScrolledText(self.root)
        # friendlistscroll.config(highlightthickness=0)
        # friendlistscroll.vbar.config(orient=VERTICAL,width = 10)
        # friendlistscroll.place(width = 280,height = 500, x = -1,y = -1)
        # canvas = Canvas(self.root, width=250, height=500,scrollregion=(0,0,500,800))
        # canvas.config(highlightthickness=0)
        # canvas.create_image(400, 300, image=self.mainBg)
        # vbar = Scrollbar(canvas,orient=VERTICAL)
        # vbar.place(x=240, width=20, height=500)
        # vbar.config(command=canvas.yview)
        # canvas.config(yscrollcommand=vbar.set)
        # canvas.place(x = 0, y = 0)
        count = len(self.myfriendList)
        canvas = Canvas(self.root, width=250, height=550, scrollregion=(0, 0, 520, count * 60),bg = "pink")
        # canvas.create_image(300, 350, image=self.mainBg)
        canvas.config(highlightthickness=0)
        canvas.place(x=0, y=0)
        frame = Frame(canvas,bg = "pink") #put canvas in frame
        frame.place(x=0, y=0)
        vbar = Scrollbar(canvas, orient=VERTICAL)#set varbar
        vbar.place(x=240, width=10, height=600)
        vbar.configure(command=canvas.yview)
        canvas.config(yscrollcommand=vbar.set)
        Label(frame, text="My friend List", fg='#1E90FF', bg = "pink").pack()
        for friendId in self.myfriendList:
            friendList = Frame(frame,width=230, height=50, bg="gray",borderwidth=2, relief=RIDGE)
            # friendList.grid(padx = 10, pady =10)
            friendList.pack()
            friend = Label(friendList, text=friendId, fg="blue",bg = "gray")
            friend.place(x=10, y=8)
            friend.bind('<Double-Button-1>',self.handlerAdaptor(self.chat_Ui,friendId = friendId))
            friendList.bind('<Double-Button-1>',self.handlerAdaptor(self.chat_Ui,friendId = friendId))
            friendList.bind('<Button-2>',self.menu)

        canvas.create_window(5, count * 26,window = frame, anchor = W)
        buttonframe = Frame(self.root,bg = "gold")
        buttonframe.place(width = 240,height = 50,y = 550)
        Button(buttonframe,text = "Add friend",fg='#1E90FF',width = 10,height = 2).place(x = 15,y = 5)
        Button(buttonframe,text = "Sign out",fg='#1E90FF',width = 10,height = 2,
               command = lambda :self.sign_out()).place(x = 135,y = 5)

    def sign_out(self):
        message = tkmsg.askokcancel(title="Warning", message="Are you sure to sign out")
        if(message == True):
            self.root.destroy()
            returnWindow = login_UI()
            returnWindow.root.mainloop()
        else:
            return None

    def handlerAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def chat_Ui(self,event,friendId):
        self.chatWindow = Toplevel()
        self.chatWindow.geometry("470x420")
        self.chatWindow.resizable(0,0)
        self.chatWindow.title("Chat with " + friendId)
        Label(self.chatWindow, image = self.mainBg).pack()
        text1 = scrolledtext.ScrolledText(self.chatWindow)
        text1.place(x=10, y=10, width=450, height=250)
        text1.config(state=DISABLED) #cannot text, just show record for chat
        text1.vbar.config(width = 10)
        text2 = scrolledtext.ScrolledText(self.chatWindow)
        text2.place(x=10, y=290, width=450, height=100)
        text2.vbar.config(width = 10)
        Button(self.chatWindow, text="send",fg = "#1E90FF",highlightthickness=0).place(x=423, y=393)#send button
    def sendMessage(self):
        pass
    def receiveMessage(self):
        pass
    def Search(self,usermane):
        pass
    def AddFriend(self,User):
        pass
    def DeletFirend(self):
        pass

if __name__ == "__main__":
    data = {"FGOmaster":["Saber","Lancer","Archer","Caster","Assassin","Rider",
                         "Berserker","Avenger","Ruler","Alterego","MoonCancer","Foreigner","Shielder"]}
    chat = Chat_UI(data)
    chat.root.mainloop()

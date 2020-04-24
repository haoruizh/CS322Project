from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

class Chat_UI:
    def __init__(self,data):
        self.root = Tk()
        self.data = data
        for id,friendlist in data.items():
            self.myid = id
            self.myfriendList = friendlist
        self.root.geometry("255x600+900+40")
        self.root.resizable(0,0)
        self.root.title(self.myid + " contact list")
        self.openWindow = {}
        self.friendList_Ui()

    def friendList_Ui(self):
        for friendId in self.myfriendList:
            f1 = Frame(width=240, height=50, bg="white", borderwidth=3, relief=RIDGE)
            f1.pack(side=TOP)
            friendLabel = Label(f1,text=friendId, fg="green")
            friendLabel.place(x=10, y=8)
            f1.bind('<Button-1>',self.handlerAdaptor(self.chat_Ui,friendId = friendId))

    def handlerAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def chat_Ui(self,event,friendId):
        self.chatWindow = Tk()
        self.chatWindow.geometry("470x420")
        self.chatWindow.resizable(0,0)
        self.chatWindow.title("Chat with " + friendId)


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
    data = {"Awsl":["ws","dasd","sdasd"]}
    chat = Chat_UI(data)
    chat.root.mainloop()

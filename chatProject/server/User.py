from socket import *
import json
from UserIdentify import UserIdentify
from Friendlist import Friendlist

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.uIdentify = UserIdentify(self.username,self.password)
        self.friendL = Friendlist()
    def get_name(self):
        return self.uIdentify.GetName()
    def get_password(self):
        return self.uIdentify.GetPassword()
    def change_password(self,old,new):
        self.password = self.uIdentify.ChangePassword(old,new)
    def verify_check(self):
        return self.uIdentify.VerifyCheck(self.username,self.password)
    def add_friend(self,name):
        return self.friendL.Add(name)
    def view_friend(self):
        return self.friendL.View()
    def remove_friend(self,name):
        return self.friendL.Remove(name)
    def find_friend(self,name):
        return self.friendL.Find(name)
    def get_Friendlist(self):
        return self.friendL
    def test(self):
        User('sherry',123).get_name()
        User('sherry',123).get_password()
        User('sherry',123).change_password(123,12345)
        User('sherry',123).add_friend('amy')
        User('sherry',123).add_friend('someone')
        User('sherry',123).remove_friend('someone')
        User('sherry',123).get_Friendlist()


if __name__ == '__main__':
    User('sherry',123).test()

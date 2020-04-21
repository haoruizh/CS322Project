from socket import *
import json

class UserIdentify:
    def __init__(self, userName, password):
        self.Username = userName
        self.Password = password
    def GetName(self):
        return self.Username
    def ChangePassword(self, oldPassword, newPassword):
        if self.Password == oldPassword:
            self.Password = newPassword
    def GetPassword(self):
        return self.Password
    def VerifyCheck(self, userName, password):
        if userName != self.Username or password != self.Password:
            return False
        else:
            return True
    

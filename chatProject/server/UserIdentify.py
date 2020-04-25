from socket import *
import json

class UserIdentify:
    def __init__(self, userName, password):
        self.Username = userName
        self.Password = password

    # get the username of this user
    def GetName(self):
        return self.Username

    # change the password
    def ChangePassword(self, oldPassword, newPassword):
        if self.Password == oldPassword:
            self.Password = newPassword

    # get the password 
    def GetPassword(self):
        return self.Password
        
    # check if given username and password match
    def VerifyCheck(self, userName, password):
        if userName != self.Username or password != self.Password:
            return False
        else:
            return True
    

from socket import *
import json

class UserIdentify:
    def __init__(self, userName, password):
        self.Username = userName
        self.Password = password

    # return the name value
    def GetName(self):
        return self.Username

    # change password to new password
    def ChangePassword(self, oldPassword, newPassword):
        if self.Password == oldPassword:
            self.Password = newPassword

    # return the password value
    def GetPassword(self):
        return self.Password
    
    # check if username and given password match
    def VerifyCheck(self, userName, password):
        if userName != self.Username or password != self.Password:
            return False
        else:
            return True
    

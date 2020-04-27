from socket import *
import json
from User import User

class User_dic:
    def __init__(self):
        self.all_user = {}

    def get_user(self,username):
        if username in self.all_user:
            return self.all_user[username]
        
    def add_new_user(self,username,password):
        if username not in self.all_user:
            user = User(username,password)
            self.all_user[username] = user
        else:
            print("This user is existed, please go to log in or sign up a new username.")

    def remove_user(self,username):
        if username in self.all_user:
            self.all_user.pop(username)

    def Add_friend(self,username,friendname):
        if username in self.all_user:
            friendL = self.all_user[username].add_friend(friendname)
        else:
            print("Username is not existed.")

    def remove_friend(self,username,friendname):
        if username in self.all_user:
            friendL = self.all_user[username].remove_friend(friendname)
        else:
            print("Username is not existed.")

    def saveToFile(self,fileStream,filetype):
        if filetype == 'csv':
            file = csv.writer(open(fileStream, 'w'))
            for key,val in self.all_user:
                file.writerow([key,val])

        elif filetype == 'txt':
            file = open(fileStream, 'w')
            file.write(str(self.all_user) + '\n')
            file.close()
        elif filetype == 'json':
            temp = json.dumps(self.all_user)
            file = open(fileStream, 'w')
            file.write(temp, indent = 1, sort_keys = True)
            file.close()
        else:
            print('Unsupportable file type.')

    def getFriend(username):
        friendlist = self.all_user[username].get_Friendlist()

    def get_single_friend(username,friendname):
        return self.all_user[username].find_friend(friendname)

    def changePssword(username,oldpassword,newpassword):
        if username in self.all_user:
            self.all_user[username].change_password(oldpassword,newpassword)
            

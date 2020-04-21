from socket import *
import json
import os
import openpyxl


class User:
    filename = 'C://Users/Jihui/Documents/GitHub/CS322Project/chatProject/server/user.txt'
    user_info = {}
    def __init__(self):
        pass

    def show_profile(self, userName):
        print(self.user_info[userName])
        return self.user_info[userName]

    def init_profile(self, userName, sex, birth):
        if userName not in self.user_info:
            self.user_info[userName] = {"sex": sex, "birthday":birth}
            json.dump(self.user_info, open(self.filename, 'w'))
        else:
            print("ID error")

    def test(self):
        User().init_profile('Jihui', 'male', '1994')
        User().init_profile('Sheng', 'male', '2020')
        User().init_profile('what', 'male', '2220')
    # def edit_profile(self, ):
    #     pass

    # def get_notify(self):
    #     pass

if __name__ == '__main__':
    User().test()
    User().show_profile('Jihui')
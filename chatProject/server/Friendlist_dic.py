from socket import *
import json
import openpyxl
import os
import Friendlist
class Friendlist_dict:
    filename = 'C://Users/Jihui/Documents/GitHub/CS322Project/chatProject/server/friendList.txt'
    list_friend = {}
    def __init__(self):
        pass

    def addFriend(self, user, friend):
        if user not in self.list_friend:
            self.list_friend[user] = [friend]
            json.dump(self.list_friend, open(self.filename, 'w'))
        else:
            for k,v in self.list_friend.items():
                v.append(friend)
                json.dump(self.list_friend, open(self.filename, 'w'))

    def removeFriend(self, user, friend):
        for k,v in self.list_friend.items():
            if k == user:
                if friend in v:
                    v.remove(friend)
                    json.dump(self.list_friend, open(self.filename, 'w'))
                else:
                    print("You've no friend named like this")
            else:
                print("Error")

    def display(self):
        pass

    def test(self):
        Friendlist_dict().addFriend('Jihui', 'Haorui')
        Friendlist_dict().addFriend('Jihui', 'Jiangquan')
        Friendlist_dict().removeFriend('Jihui', 'Jiangquan')
if __name__ == "__main__":
    Friendlist_dict().test()
from socket import *
import json
from Friendlist import *

class Friendlist_dict:
    filename = './friendList.txt'
    list_friend = {}
    def __init__(self):
        pass

    def addFriend(self, user, friend,sex,birth):
        if user not in self.list_friend:
            # self.list_friend[user] = [friend]
            self.list_friend[user] = {friend:1}
            self.list_friend[user][friend] = (sex,birth)
        else:
            for k,v in self.list_friend.items():
                v[friend] = (sex,birth)
        json.dump(self.list_friend, open(self.filename, 'w'))
        print(user + '\'s friend ' + str(friend)
              + ' is ' + str(self.list_friend[user][friend][0]) + ' and birth in ' + str(
            self.list_friend[user][friend][1]))

    # def addFriend(self, user, friend,sex,birth):
    #     if user not in self.list_friend:
    #         self.list_friend[user] = [friend]
    #     else:
    #         for k,v in self.list_friend.items():
    #             v.append(friend)
    #     json.dump(self.list_friend, open(self.filename, 'w'))

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

    def load_friendList(self, user):
        return self.list_friend[user]

    def display(self):
        print(self.list_friend)

    def test(self):
        Friendlist_dict().addFriend('Jihui', 'Haorui','male','2011/01/01')
        Friendlist_dict().addFriend('Jihui', 'Jiangquan','male','2011/01/02')
        # Friendlist_dict().removeFriend('Jihui', 'Jiangquan')
        Friendlist_dict().display()
if __name__ == "__main__":
    Friendlist_dict().test()
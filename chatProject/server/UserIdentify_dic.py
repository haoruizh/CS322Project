from socket import *
import json
import json
class UserIdentify:
    filename = 'C://Users/Jihui/Documents/GitHub/CS322Project/chatProject/server/UserIdentify.txt'
    all_name = {}
    def __init__(self):
        pass
        # self.username = username
        # self.password = password

    def add_user(self, userName, password):
        if userName not in self.all_name:
            self.all_name[str(userName)] = str(password)
            json.dump(self.all_name, open(self.filename, 'w'))
        else:
            print("Name has already be token")

    def remove_user(self, userName):
        if userName not in self.all_name:
            print("Can't find the user")
        else:
            # del self.all_name[userName]
            self.all_name.pop(userName)
            print(self.all_name)
            print("Deleted!")

        json.dump(self.all_name, open(self.filename, 'w'))

    def test(self):
        UserIdentify().add_user('a', '1')
        UserIdentify().add_user('b', '1')
        UserIdentify().add_user('a', '2')
        UserIdentify().remove_user('a')

if __name__=='__main__':
    UserIdentify().test()

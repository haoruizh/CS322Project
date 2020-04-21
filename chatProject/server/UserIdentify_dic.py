from socket import *
import json
import json
# import UserIdentify

class UserIdentify_dic:
    filename = './UserIdentify.txt'
    all_name = {}
    def __init__(self):
        pass

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
            # print(self.all_name)

        json.dump(self.all_name, open(self.filename, 'w'))

    # def verify(self):
    #     userName = input("Enter ur username: ")
    #     UserIdentify.Username = userName
    #     if UserIdentify.Username in self.all_name:
    #         userPassword = input("Enter password: ")
    #         UserIdentify.Password = userPassword
    #         if UserIdentify.Password == self.all_name[UserIdentify.Username]:
    #             print("Log in successful")
    #         else:
    #             print("Fail to login")
    #     else:
    #         print("Something wrong on your userName")

    def test(self):
        UserIdentify_dic().add_user('a', '1')
        UserIdentify_dic().add_user('b', '1')
        UserIdentify_dic().add_user('a', '2')
        UserIdentify_dic().remove_user('a')

if __name__=='__main__':
    UserIdentify_dic().test()
    # UserIdentify_dic().verify()

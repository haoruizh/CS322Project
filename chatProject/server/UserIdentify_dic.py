from socket import *
import json
from UserIdentify import *

class UserIdentify_dic:
    #<<<<<<< HEAD
    #=======
    all_name = {}
    filename = './UserIdentify.txt'
    #>> >> >> > 24
    #d9ed0273743bf90f8d8535161fcf4664f6806b
    def __init__(self):
        pass

    def add_user(self, userName, password):
        #newUser = UserIdentify(userName, password)
        if userName not in self.all_name:
            #self.all_name[str(userName)] = newUser
            self.all_name[str(userName)] = password
            json.dump(self.all_name, open(self.filename, 'w'))
        else:
            print("Name has already be taken")

    def remove_user(self, userName):
        if userName not in self.all_name:
            print("Can't find the user")
        else:
            # del self.all_name[userName]
            self.all_name.pop(userName)
            # print(self.all_name)

            json.dump(self.all_name, open(self.filename, 'w'))

    # def verify(self, givenUserName, givenPassword):
    #      if givenUserName not in self.all_name:
    #          return False
    #      else:
    #          return self.all_name[givenUserName].VerifyCheck(givenUserName, givenPassword)

    def test(self):
        UserIdentify_dic().add_user('a', '1')
        UserIdentify_dic().add_user('b', '1')
        UserIdentify_dic().add_user('a', '2')
        UserIdentify_dic().add_user('c', '2')
        UserIdentify_dic().remove_user('a')
        # UserIdentify_dic().verify('b', '1')

if __name__=='__main__':
    UserIdentify_dic().test()
    # UserIdentify_dic().verify()

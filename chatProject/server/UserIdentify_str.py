import json
# from UserIdentify import *

class UserIdentify_dic:
    all_name = {}
    filename = './UserIdentify_1.txt'
    def __init__(self):
        pass

    def load_store(self):
        with open(self.filename, "r") as file:
            f = file.readlines()
            for line in f:
                data = line.split()
                self.all_name[data[0]] = data[1]
                print("load successful!   " + str(data[0]) + "'s password is: " + str(data[1]))
        file.close()

    def add_user(self, userName, password):
        if userName not in self.all_name:
            self.all_name[str(userName)] = password
            with open(self.filename, "a") as file:
                file.write(userName + ' ' + password + "\n")
            file.close()
        else:
                print("Name has already be taken")

    def remove_user(self, userName):
        if userName not in self.all_name:
            print("Can't find the user")
        else:
            # del self.all_name[userName]
            self.all_name.pop(userName)
            with open(self.filename, "r") as file:
                f = file.readlines()
            with open(self.filename, "w") as file:
                for data in f:
                    if data.startswith(userName):
                        pass
                    else:
                        file.write(data)
            file.close()

    # def verify(self, givenUserName, givenPassword):
    #      if givenUserName not in self.all_name:
    #          return False
    #      else:
    #          return self.all_name[givenUserName].VerifyCheck(givenUserName, givenPassword)

    def test(self):
        UserIdentify_dic().load_store()
        UserIdentify_dic().add_user('Jihui', '123456')
        UserIdentify_dic().add_user('Haorui', '135790')
        UserIdentify_dic().add_user('Jiangquan', '111111')
        UserIdentify_dic().add_user('Jiangquan', '222222')
        UserIdentify_dic().remove_user('Jihui')
        # UserIdentify_dic().verify('b', '1')

if __name__=='__main__':
    UserIdentify_dic().test()
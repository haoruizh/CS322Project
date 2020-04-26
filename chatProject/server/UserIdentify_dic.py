from socket import *
import json
from UserIdentify import *
import csv

class UserIdentify_dic:
    def __init__(self):
        self.all_name = {}
    
    # save all_name content to given file based on type
    # seperate by a space
    def saveToFile(self, fileStream, type):
        if type == 'csv':
            # write all username and password pair as csv file type
            w=csv.writer(open(fileStream, "w"))
            for key,val in self.all_name.items():
                w.writerow([key,val])

        elif type =='txt':
            f = open(fileStream, "w")
            f.write(str(self.all_name) +'\n')
            f.close()

        elif type == 'json':
            json = json.dumps(self.all_name)
            f = open(fileStream, "w")
            f.write(json,indent = 1,sort_keys = True)
            f.close()
        else:
            print("Unsupportable file type")

    # Add a new user to the dic
    def add_user(self, userName, password):
        #newUser = UserIdentify(userName, password)
        if userName not in self.all_name:
            self.all_name[str(userName)] = password
            #json.dump(self.all_name, open(self.filename, 'w'))
        else:
            #print("Name has already be taken")
            return False

    # remove the user from the dic based on given username
    def remove_user(self, userName):
        if userName not in self.all_name:
            #print("Can't find the user")
            return False
        else:
            # del self.all_name[userName]
            self.all_name.pop(userName)
            # print(self.all_name)

    # Verify the user based on given username and password
    def verify(self, givenUserName, givenPassword):
         if givenUserName not in self.all_name.keys():
             return False
         else:
             return True if self.all_name[givenUserName] == givenPassword else False

    def test(self):
        UserIdentify_dic().add_user('a', '1')
        UserIdentify_dic().add_user('b', '1')
        UserIdentify_dic().add_user('a', '2')
        UserIdentify_dic().remove_user('a')
        UserIdentify_dic().verify('b', '1')
        UserIdentify_dic().verify('b', '2')
        UserIdentify_dic().saveToFile("C:\Users\haoru\Desktop","json")

if __name__=='__main__':
    UserIdentify_dic().test()
    # UserIdentify_dic().verify()

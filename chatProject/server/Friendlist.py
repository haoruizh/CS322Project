from socket import *
import json
class Friendlist:
    ContactList = []
    def __init__(self):
        pass
    def ViewFriendList(self):
        for i in self.ContactList:
            print(i)
    def AddFriend(self, Name):
        #if searched user not in the list
        if Name not in self.ContactList:
            #If try to add own name, throw an error
            self.ContactList.append(Name)
        else:
            print("Searched user already in the list!")
    def RemoveFriend(self, Name):
        if Name in self.ContactList:
            self.ContactList.remove(Name)
        else:
            print("Searched user not in the list!")
    def FindUser(self, Name):
        for i in range(len(self.ContactList)):
            if self.ContactList[i] == Name:
                return self.ContactList[i]
            else:
                print('User not in list')

    def test_f(self):
        Friendlist().AddFriend('na')
        Friendlist().FindUser('na')
        print(Friendlist().ContactList)

if __name__ == "__main__":
    Friendlist().test_f()

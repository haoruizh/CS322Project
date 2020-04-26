from socket import *
import json
class Friendlist:
    def __init__(self):
        self.ContactList = []
    def View(self):
        for i in self.ContactList:
            print(i)
    def Add(self, Name):
        #if searched user not in the list
        if Name not in self.ContactList:
            #If try to add own name, throw an error
            self.ContactList.append(Name)
        else:
            print("Searched user already in the list!")
    def Remove(self, Name):
        if Name in self.ContactList:
            self.ContactList.remove(Name)
        else:
            print("Searched user not in the list!")
    def Find(self, Name):
        if Name in self.ContactList:
            return self.ContactList[Name]
        else:
            print("Searched user not in list!")
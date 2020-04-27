from socket import *
import json

class Friendlist:
    def __init__(self):
        self.ContactList = []

    #print all friends
    def View(self):
        for i in self.ContactList:
            print(i)
    

    def Add(self, Name):
        #if searched user not in the list
        if Name not in self.ContactList:
            #If try to add own name, throw an error
            self.ContactList += Name
            return True
        else:
            print("Searched user already in the list!")
            return False

    # Remove friend basedon the given name
    def Remove(self, Name):
        if Name in self.ContactList:
            self.ContactList.remove(Name)
            # check if friend name has been successfully removed.
            if ( Name not in self.ContactList):
                return True
            else:
                return False
        else:
            print("Searched user not in the list!")
            return False

    # find the friend based on the name
    def Find(self, Name):
        if Name in self.ContactList:
            return Name
        else:
            print("Searched user not in list!")

    # check if friend is in the list
    def Check(self, Name):
        if Name in self.ContactList:
            return True
        else:
            return False
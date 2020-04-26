import json
import os
import pandas as pd
import xlsxwriter

class Friendlist_1:
    filename = './friendList.txt'
    list_friend = {}
    def __init__(self):
        pass

    def load_store(self):
        with open(self.filename, "r") as file:
            f = file.readlines()
            # print(len(f))
            if len(f) != 0:
                for line in f:
                    data = line.split()
                    if data[0] not in self.list_friend:
                        fList = []
                        fList.append(data[1])
                        self.list_friend[data[0]] = fList
                    else:
                        fList.append(data[1])
            else:
                print("The file is empty!")
        file.close()

    # def addFriend(self, user, friend, type):
    #     if type == 'txt':
    #         if user not in self.list_friend:
    #             self.list_friend[user] = [friend]
    #             with open(self.filename, "a") as file:
    #                 file.write(user + " " + friend + "\n")
    #             file.close()
    #         else:
    #             if friend not in self.list_friend[user]:
    #                 self.list_friend[user].append(friend)
    #                 with open(self.filename, "a") as file:
    #                     file.write(user + " " + friend + "\n")
    #                 file.close()
    #             else:
    #                 print("Friend already exist")
    #     elif type == 'json':
    #         if user not in self.list_friend:
    #             self.list_friend[user] = [friend]
    #             json.dump(self.list_friend, open(self.filename, 'w'))
    #         else:
    #             if friend not in self.list_friend[user]:
    #                 self.list_friend[user].append(friend)
    #                 json.dump(self.list_friend, open(self.filename, 'w'))
    #             else:
    #                 print("Friend already exist")
    #     else:
    #         print("Unsupportable file type")


    def addFriend(self, user, friend):
        if user not in self.list_friend:
            self.list_friend[user] = [friend]
            with open(self.filename, "a") as file:
                file.write(user + " " + friend + "\n")
            file.close()
        else:
            if friend not in self.list_friend[user]:
                self.list_friend[user].append(friend)
                with open(self.filename, "a") as file:
                    file.write(user + " " + friend + "\n")
                file.close()
            else:
                print("Friend already exist")

    def txt2json(self):
        with open(self.filename, "r") as file:
            f = file.readlines()
            result = {}
            for line in f:
                line = line.strip("\n")
                string = line.split(" ")
                result[string[0]] = string[1]
        with open(self.filename, "w") as file1:
            file1.write(json.dumps(result))

    def txt2csv(self):
        newCsv = xlsxwriter.Workbook('friendList.csv')
        worksheet = newCsv.add_worksheet()
        headings = ['User','UsersFriends']
        user = []
        userFriends = []
        with open(self.filename, 'r') as file:
            f = file.readlines()
            for line in f:
                data = line.split()
                user.append(data[0])
                userFriends.append(data[1])
        tData = [user,userFriends]

        worksheet.write_row('A1', headings)

        worksheet.write_column('A2',tData[0])
        worksheet.write_column('B2',tData[1])
        newCsv.close()

    def removeFriend(self, user, friend):
        for k,v in self.list_friend.items():
            if k == user:
                if friend in v:
                    v.remove(friend)
                    with open(self.filename, "r") as file:
                        f = file.readlines()
                    with open(self.filename, "w") as file:
                        for data in f:
                            if data.startswith(user + " " + friend):
                                pass
                            else:
                                file.write(data)
                    file.close()
                else:
                    print("You've no friend named like this")
            else:
                print("Error")
    # def addFriend(self, user, friend):
    #     if friend != self.list_friend[1]:
    #         self.list_friend[user] = friend
    #         with open(self.filename, "a") as file:
    #             file.write(user + ' ' + friend + "\n")
    #     else:
    #         print("Friend already in ur list")
    # def removeFriend(self, user, friend):
    #

    def load_friendList(self, user):
        return self.list_friend[user]

    def display(self):
        print(self.list_friend)

    def test(self):
        Friendlist_1().load_store()
        Friendlist_1().addFriend('jihui', 'kema')
        Friendlist_1().addFriend('jihui', 'Jiangquan')
        Friendlist_1().addFriend('Jiangquan', 'jihui')
        Friendlist_1().removeFriend('jihui', 'Jiangquan')
        Friendlist_1().txt2csv()

        Friendlist_1().display()
#         Friendlist_dict().display()
if __name__ == "__main__":
    Friendlist_1().test()
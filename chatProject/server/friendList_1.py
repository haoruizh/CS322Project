
class Friendlist_1:
    filename = './friendList_1.txt'
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

                # if data[0] not in nList:
                #     fList = []
                #     nList.append(data[0])
                #     if data[1] not in fList:
                #         fList.append(data[1])
                #         self.list_friend[data[0]] = [data[1]]
                #     else:
                #         print("Friend already in list")
                # else:
                #     if data[1] not in fList:
                #         fList.append(data[1])               # {user:[friend1,f2,f3...]}
                #         self.list_friend[data[0]] = fList
                #     else:
                #         print("Friend already in list")



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


        # bList = []
        # with open(self.filename, "r") as file:
        #     f = file.readlines()
        #     for line in f:
        #         data = line.split()
        #         if data[0] == user:
        #             if data[1] not in bList:
        #                 bList.append(data[1])
        #                 with open(self.filename, "a") as file:
        #                     file.write(data[0] + " " + bList + '\n')
        #         else:
        #             print("Not searched such user")

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

        Friendlist_1().display()
#         Friendlist_dict().display()
if __name__ == "__main__":
    Friendlist_1().test()
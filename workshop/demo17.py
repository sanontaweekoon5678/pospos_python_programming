# Define Class

class User:
    username = ""
    password = ""

    def __init__(self, username="admin", password="admin"):
        self.username = username
        self.password = password

# Inheritance / subclass


class UserV1(User):
    def clear(self):
        self.username = ""
        self.password = ""

    def __str__(self):
        return "username: {}, password: {}".format(self.username, self.password)

    # def __str__(self):
    #     return "username : {} , password: {}".format(self.username, self.password)

    # def print(self):
    #     print("created : {}, {}".format(self.username, self.password))

    # def clear():
    #     pass


# Create an Object from above class
user1 = User("sanon", "1234")
print(user1)
user = UserV1("sanon", "5678")
print(user)
# user1.print()
# print(user1)


# class Payment:
#     pass

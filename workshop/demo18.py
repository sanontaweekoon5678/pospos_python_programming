# Define Class

class User:
    username = ""
    password = ""

    def __init__(self, username="admin", password="admin"):
        self.username = username
        self.password = password

    def clear(self):
        self.username = ""
        self.password = ""


class UserV1(User):
    def __init__(self, username, password, level):
        super().__init__(username, password)
        self.level = level

    def __str__(self):
        return "{}, {}, {}".format(self.username, self.password, self.level)

    def clear(self):
        super().clear()
        self.level = ""


user = UserV1("root", "1234", "")
print(user)
user.clear()
print(user)

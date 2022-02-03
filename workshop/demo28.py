# Elipsis ...
from time import process_time_ns


def test():
    ...


def login(account: ...) -> ...:
    print(account)
    print(account["username"])
    return {"result": "success"}


print("Hi")
acc = {"username": "admin", "password": "1234"}
result = login(acc)
print(result)

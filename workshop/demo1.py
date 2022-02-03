print("HelloWorld")

# Demonstrate indentation
if 3 > 1 and True:
    print("3 > 1")
    print("3 > 1")
else:
    print("3 <= 1")

print("===================================")

# Implicit Declaration
tmp1 = 1  # int
tmp2 = "Hey"  # str
tmp3 = True  # bool
tmp4 = 1.3  # float

print(tmp1)
print(type(tmp1))
print(type(tmp2))

print("===================================")

# Explicit Declaration
exp1: int = 1
exp2: str = "sanon"
exp3: bool = False
exp4: float = 1.2

print(exp1)
print(type(exp1))

# list
tmp5 = ["Angular", "React", "Vue"]
tmp6 = {"user": "admin", "password": "1234"}
print(tmp5)
print(tmp6)

tmp11 = dict(username="admin", password="1234")
tmp12 = list(("Angular", "React", "Vue"))
print(tmp11)
print(tmp12)

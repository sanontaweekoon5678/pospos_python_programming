# condition if-else

from re import T


data = 5
if data > 3 and data < 5:
    print("data {}".format(data))
    print("data {}".format(data))
    print("data {}".format(data))
elif data > 4:
    print("data is > 4 : {} " .format(data))
else:
    print("data is not > 3")

if True:
    print("a is greater then b")
print("Yes") if False else print("No")

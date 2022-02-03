# Asterisks
numbers = [1, 2, 3]
anotherNumbers = [4, 5, 6]
allNumber = [*numbers,  *anotherNumbers]
print(allNumber)

colorSet1 = {"Red": "#F00", "Green": "#0F0"}
colorSet2 = {"Yellow": "#FF0", "Blue": "#00F"}
allColors = {**colorSet1, **colorSet2}
print(allColors["Yellow"])

print(allNumber)
print(allNumber[0], allNumber[1])
print(*allNumber)


def show(msg1, msg2, msg3):
    print(msg1)
    print(msg2)
    print(msg3)


show(*["Angular", "React", "Vue"])


def test(*messages):
    print(len(messages))
    print(messages[1])


test("sanon", "sanon", "weaw")

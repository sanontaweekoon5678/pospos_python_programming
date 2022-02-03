# List
dataList1 = ["angular", "Vuejs", "react"]  # implicit
dataList2: list = ["angular", "Vuejs", "react"]  # explicit
dataList3 = list(("angular", "Vuejs", "react"))  # constr

print(dataList1)
print(dataList2)
print(type(dataList2))
print(dataList3)

extraArray = ["raspberrypi", "flutter"]
dataList1.append("python")
dataList1.extend(extraArray)
dataList1.insert(1, "sanon")
dataList1.extend(dataList2)
dataList1.remove("Vuejs")
dataList1.pop()
print(dataList1)

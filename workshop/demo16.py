# For loop

courses = ["Angular", "React", "VueJs", "Python", "Golang"]

for course in courses:
    print(course)
    if course == 'Vuejs':
        # break
        continue
    print(course)

for count in [1, 2, 3, 4]:
    print(count)

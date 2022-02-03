from cgi import print_form
import mymodule1
import mycal_module

mymodule1.greeting("test")
print(mycal_module.plus(1, 2))
print(mycal_module.minus(1, 2))
print(mycal_module.allNumber)
mycal_module.allNumber[0] = -1
print(mycal_module.allNumber)

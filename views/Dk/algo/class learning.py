#class MyClass:
#    x = 5
#
#p1 = MyClass()
#print(p1.x)

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name + " I am " + str(abc.age))



p1 = Person("Dk", 16)
p1.myfunc()
'''
Created on Feb 13, 2020

@author: zhangwei
'''
class Person:
    def __init__(self, name, age, career):
        self.__name = name # private attribute
        self.__age = age
        self.__career = career
    def __str__(self):
        return "name is "+ self.__name + ", age is " + str(self.__age) + ", career is " + self.__career
    def study(self):
        print(self.__name + " am studying ...")
        
mary = Person("Mary", 16, "Student")


print(mary)
mary.study()
print(mary.__name)
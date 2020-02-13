'''
Created on Feb 13, 2020

@author: zhangwei
'''




class Person:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career
    def __str__(self):
        return "name is "+ self.name + ", age is " + str(self.age) + ", career is " + self.career
    def study(self):
        pass 
        # I am still think about how to implement this method
        
mary = Person("Mary", 16, "Student")

print(mary)
mary.study()


'''
Created on Feb 13, 2020

@author: zhangwei
'''
class Hotdog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []
    def __str__(self):
        msg = "Hot dog"
        if len(self.condiments) > 0:
            msg = msg + " with "
        for i in self.condiments:
            msg = msg +  i + ", "
        msg = msg.strip(", ") # be careful
        msg = self.cooked_string + " " + msg + "." 
        return msg
    def cook(self, time):
        if time > 8:
            self.cooked_string = "Charcoal"
        elif time > 5:
            self.cooked_string = "Well done"
        elif time > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"
    def addCondiments(self, c):
        self.condiments.append(c)
        

hotdog = Hotdog()
print("cook hotdog for 4 minutes...")
hotdog.cook(4)
print(hotdog)

print("cook hotdog for 2 minutes...")
hotdog.cook(2)
print(hotdog)

print("cook hotdog for 10 minutes...")
hotdog.cook(10)
print(hotdog)

hotdog.addCondiments("Ketchup")
hotdog.addCondiments("Mustard")
print(hotdog)
#Task 1

#A Person class

#Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing, for example like this:

#"Hello, my name is Carl Johnson and I’m 26 years old"

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
    def talk(self):
        print (f"Hello my name is {self.firstName} {self.lastName} and I'm {self.age} years old")
    

person1=Person("Erza","Berbatovci",20)
person1.talk()
# class is framework => datamember, member-function

# data members => value/characteristic
# member-function => behaviour/function

class student:
    name="Devanshu" # data member
    age=13 # data member
    def intro(self): # self to take latest object
        print("Hi this is",self.name)
    def details(self):
        print("I am",self.age,"years old")

o1=student()
o1.intro()
o1.details()
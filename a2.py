
class parrot:
    species="bird" #global datamember => common for all objects

    def __init__(self,n,a): #function for initialization
        self.name=n #instance datamember
        self.age=a

    def intro(self):
        print("Hello... my name is",self.name)
    
    def details(self):
        print("I am",self.age,"years old")

    def sing(self,s):
        print(self.name,"is singing",s,"song")

o1=parrot("Hoo",10) #object=instance, object creation=instantiation, constructor is called automatically
o2=parrot("Woo",12)
o1.intro()
o1.details()
o2.intro()
o2.details()
o2.sing("hurray")
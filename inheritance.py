# Parent Class/Super/Base class- This is the class you borrow from

class animal :
    isMammal = True

    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is moving")
# Child class/Sub class/Derived class

class cat(animal):
    def sound(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")

class horse(animal):
    hasTail= True

    def neigh(self):
        print("Horse is neighing")


a = animal()
a.speak
c= cat()

h= horse()

    
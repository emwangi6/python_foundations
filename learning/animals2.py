#multiple inheritance -> inherit from more than one parent class
#                        C(A B)
# multilevel inheritance ->inherit from a parent which inherits from another parent
#                         C(B) <-B(A)<-A
class Animal:
    def __init__(self,name):
        self.name =name
    def eat(self):
        print(f'{self.name} is eating')


class Prey (Animal):
    def flee(self):
        print('This animal is fleeing.')


class Predator(Animal):
    def hunt(self):
        print('This animal is hunting.')


class Rabbit (Prey):
    pass


class Hawks (Predator):
    pass


class Fish (Prey , Predator):#multiple inheritances
    pass

rabbit = Rabbit('Rabbit')
hawks = Hawks('Hawks')
fish = Fish('Fish')
rabbit.flee()
hawks.hunt()
fish.flee()
fish.hunt()
rabbit.eat()
hawks.eat()
fish.eat()

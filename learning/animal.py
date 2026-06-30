
class Animal:
    def __init__(self,name):
        self.name =name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def speak(self):
        print(f'{self.name} makes a sound')


class Dog(Animal):
    def __init__(self ,name,breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f'The {self.name} goes Wolf')

    def introduce(self):
        print(f'This is a {self.breed} dog. ')

class Cat(Animal):
    def speak(self):
        print(f'The {self.name} goes Meow')

class Mouse(Animal):
    def speak(self):
        print(f'The {self.name} goes Squeek')

dog =Dog('Dog','German shepherd')
cat = Cat('Cat')
mouse = Mouse('Mouse')

print(dog.name)
dog.introduce()
print(cat.name)
print(mouse.name)

dog.speak()
cat.speak()
mouse.speak()

dog.eat()
cat.eat()
mouse.eat()

dog.sleep()
cat.sleep()
mouse.sleep()


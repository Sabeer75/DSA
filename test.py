class Animal:
    def speak(self):
        return "I am an animal."


class Dog(Animal):
    def speak(self):
        return "Woof!"


print(Dog().speak())


# 2 Duck Typing
class Cat:
    def speak(self):
        return "Meow!"


def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()


print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))

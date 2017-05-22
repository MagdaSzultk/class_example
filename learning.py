class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


class Dog(Animal):
    def __init__(self, age, name, breed):
        super(Dog, self).__init__(age, name)
        self.breed = breed

    def get_breed(self):
        return self.breed


my_dog = Dog(5, "punio", "shih tzu")

print(my_dog.get_breed(), my_dog.get_age(), my_dog.get_name())

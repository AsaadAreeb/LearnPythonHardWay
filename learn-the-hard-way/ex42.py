## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def animal_do():
        print("Animal did the task.")
    pass

## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## self.name has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        ## self.name has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ## self.name has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ## ???
        super(Employee, self).__init__(name)
        ## self.salary has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    def fish_do():
        print("Fish did the task")
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("satan")

## mary is-a Person
mary = Person("mary")

## mary.pet has-a satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank.pet has-a rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

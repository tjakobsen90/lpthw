## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## make a class named dog that is an animal
class Dog(Animal):

	def __init__(self, name):
	## class dog has-a __init__ that takes self and name parameters
		self.name = name

## make a class named cat that is an animal
class Cat(Animal):

	def __init__(self, name):
	## class cat has-a __init__that takes self and name parameters
		self.name = name

##  make a class named person that is an object
class Person(object):

	def __init__(self, name):
	## class person has-a __init__ that takes self and name parameters
		self.name = name

	## Person has-a pet of some kind
		self.pet = None

## make a class named employee that has-a __init__ that takes self, name and salary as parameters
class Employee(Person):

	def __init__(self, name, salary):
		## hmm what is this strange magic?
		## fggt, self komt van __init__ die een waarde krijgt uit salary / __init__ = self
		super(Employee, self).__init__(name)
		## employee has a salary attribute
		self.salary = salary

## make a class named fish that is an object
class Fish(object):
	pass

## make a class named salmon that is a fish
class Salmon(Fish):
	pass

## make a class named halibut that is a fish
class Halibut(Fish):
	pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## from mary get the pet attribute and set it to satan
mary.pet = satan

## set frank to an instance of clas employee that takes frank/self and 120000 as parameters
frank = Employee("Frank", 120000)

## from frank get the pet attribute and set it to rover
frank.pet = rover

## set flipper to an instance of class Fish
flipper = Fish()

## set crouse to an instance of class Salmon
crouse = Salmon()

## set harry to an instance of Halibut
harry = Halibut()

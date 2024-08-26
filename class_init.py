class Dog:
	# Class attribute
	attr1 = 'mammal'

	# Instance attribute

	def __init__(self, name):
		self.name = name

roger = Dog("Roger")
tommy = Dog("Tommy")

print("Roger is a {}".format(roger.__class__.attr1))
print("Tommy is a {}".format(tommy.__class__.attr1))
# print("Hello")

print("My name is {}".format(roger.name))
print("My name is {}".format(tommy.name))
class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

	def override(self):
		print "PARENT override()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print "-" * 10

dad.override()
son.override()

print "-" * 10

dad.altered()
son.altered()

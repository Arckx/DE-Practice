# class MyClass: # Class initialization
#     x = 5

# p1 = MyClass() # This is an object

# print(p1.x)

# del p1 # Object has been deleted

# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
"""Note: The self parameter must be the first parameter of any method in the class."""

# p1 = Person("Emil", 36)
# p2 = Person("Tobias")

# print(p1.name, p1.age)
# print(p2.name, p2.age)


# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def printname(self):
#         print(self.name)

# p1 = Person("Tobias")
# p2 = Person("Linus")

# p1.printname()
# p2.printname()

# Modifying Properties in a class

# class Person:
#     species = "Human"  # Class property

#     def __init__(self, name, age):
#         self.name = name  # Instance property
#         self.age = age 

# p1 = Person("Tobias", 25)
# print(p1.age)

# p1.age = 26
# print(p1.age)

# Person.species = "Animal"  # Modifying class property

# print(p1.species)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello, my name is ", self.name)

# p1 = Person("Emil")
# p1.greet()

# class Calculator:
#     def add(self, a, b):
#         return a + b
    
#     def multiply(self, a, b):
#         return a * b 

# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(5, 3))


""""The __str__() method is a special method that controls what is returned when the object is printed:"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name} ({self.age})"

# p1 = Person("Tobias", 36)
# print(p1)


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         # Person.__init__(self, fname, lname)
#         super().__init__(fname, lname) # super() function that will make the child class inherit all the methods and properties from its parent
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


# """When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:"""

# x = Student("Mike", "Olsen", 2019)
# x.welcome()


# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.__age = age # Private Property

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age) # This will cause error

""""Note: Private properties cannot be accessed directly from outside the class."""

# Get Private Property Value

"""Note: A single underscore _ is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction."""
# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.__age = age # Private Property
#         self._salary = salary # Protected Property
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, age): #Setting age
#         if age > 0:
#             self.__age = age
#         else:
#             print("age must be positive")

# p1 = Person("Tobias", 25, 50000)
# print(p1.get_age())
# print(p1._salary) #Can access, but shouldn't

# p1.set_age(30)
# print(p1.get_age())


# Private methods
# You can also make methods private using the double underscore prefix

# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def __validate(self, num):
#         if not isinstance(num, (int, float)):
#             return False
#         return True
    
#     def add(self, num):
#         if self.__validate(num):
#             self.result += num
#         else:
#             print("Invalid number")

# calc = Calculator()
# calc.add(30)
# calc.add(5)
# print(calc.result)
# calc.__validate(5) # This would cause an error 

# Inner Classes

# class Outer:
#   def __init__(self):
#     self.name = "Outer"

#   class Inner:
#     def __init__(self):
#       self.name = "Inner"

#     def display(self):
#       print("Hello from inner class")

# outer = Outer()
# inner = outer.Inner()
# inner.display() 

"""Inner classes in Python do not automatically have access to the outer class instance.

If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter."""

# class Outer:
#     def __init__(self):
#         self.name = "Emil"

#     class Inner:
#         def __init__(self, outer):
#             self.outer = outer

#         def display(self):
#             print(f"Outer class name: {self.outer.name}")

# outer = Outer()
# inner = outer.Inner(outer)
# inner.display()
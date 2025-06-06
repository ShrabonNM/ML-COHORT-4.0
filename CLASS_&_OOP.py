#class 

class Point: # Point class with methods to move and draw
     
    def move(self): # This method simulates moving the point
        # In a real application, this would change the point's position
        print("move") # Indicating the point has moved

    def draw(self): # This method simulates drawing the point
        # In a real application, this would render the point on a canvas
        print("draw") # Indicating the point has been drawn


my_point = Point() # Creating an instance of Point # Instantiate the Point class # Using the methods of the Point class
my_point.move() # Call the move method to simulate moving the point
my_point.draw() # Call the draw method to simulate drawing the point
my_point.x=10 # Setting the x attribute of the point # attribute is set to 10 it's a dynamic attribute
print(my_point.x) # Print the x attribute of the point to verify it's set to 10# Output: 10
my_point.y=20 # Setting the y attribute of the point    # attribute is set to 20 it's a dynamic attribute
print(my_point.y) # Print the y attribute of the point to verify it's set to 20 # Output: 20



# constructor
#class PointWithConstructor: # Point class with a constructor to initialize attributes
#    def __init__(self, x=0, y=0): # Constructor to initialize x and y attributes
   

class Point: # Point class with methods to move and draw
     
    def __init__(self, x=0, y=0): # Constructor to initialize the point's coordinates with default values
        self.x = x # Set the x coordinate
        self.y = y # Set the y coordinate

    def move(self): # This method simulates moving the point
        # In a real application, this would change the point's position
        print("move") # Indicating the point has moved

    def draw(self): # This method simulates drawing the point
        # In a real application, this would render the point on a canvas
        print("draw") # Indicating the point has been drawn



point_with_constructor = Point(10, 20) # Creating an instance of Point with specific coordinates
print(point_with_constructor.x) # Output: 10
print(point_with_constructor.y) # Output: 20




# class is a blueprint for creating objects
# OOP is a programming paradigm that uses classes and objects
# OOP allows for encapsulation, inheritance, and polymorphism

class Student:
    name="Noor Mohammed Shrabon" # Class attribute



#creatinfg objects instance of the Student class
s1= Student() # Creating an instance of the Student class
print(s1.name) # Accessing the class attribute through the instance

class Car:
     color = "Black" 
     model = "mercedes"

car1 =Car()
print(car1.color)
print(car1.model)


#constructor
# All classes havse a function called __init__() which is used to initialize the attributes of the class

class Student:

#parameterized constructor
    # This constructor initializes the instance attributes fullname and marks
    def __init__(self,fullname,marks): # we can write abcd instead of self 
        self.name = fullname # Instance attribute initialized through the constructor
        self.marks = marks
        print("Adding new student in database") # This message is printed when a new instance is created    

s1 = Student("NM NOOR",98)  
print(s1.name,s1.marks) # Accessing the instance attribute through the instance
s2= Student("Shrabon",87)
print(s2.name,s2.marks) # Accessing the instance attribute through another instance

# default constructor
class Student:
    def __init__(self):
        pass # This constructor does not initialize any attributes




# attribute
#class and instance attributes
# instance attributes are specific to each instance of the class for example, each student can have different names and marks
# instance attributes are defined in the __init__() method and are accessed using self  like-- self.name, self.marks
# class attributes are defined directly in the class body and are accessed using the class name like--Student.name
# class attributes are shared by all instances of the class
#object attributes are instance attributes that are specific to each object


class Student:
    # Class attribute
    school_name = "ABC High School" # This is a class attribute shared by all instances of the class
    name = "anonymous" # class attribute for the student's name, default value is "anonymous"
    def __init__(self, name, marks): # Constructor to initialize instance attributes
        self.name = name # object attribute for the student's name ,Objectt attribute > class attribute 
        self.marks = marks # object attribute for the student's marks.Object attributes precedence are higher than class attributes so object attributes will override class attributes if they have the same name 

s1 = Student("Ahammed" ,77)
print(s1.name, s1.marks) # Accessing instance attributes through the instance 


#there two things in the class . one is data and another is methods
# data is the attributes of the class and methods are the functions of the class
# example of methods are like we have car class and it has methods like start(), stop(), accelerate() etc.or color of the car, model of the car etc.
# Easiest way to understand methods is methods are functions that belongs to a object 


#creating class with mehods
class Car:
    def start(self): # Method to start the car #self is a reference to the instance of the class.instance is the object created from the class
        print("Car started") # Indicating the car has started

    def stop(self): # Method to stop the car # self refers to the current instance of the class. It’s a way to access data or methods inside the object.
        print("Car stopped") # Indicating the car has stopped

    def accelerate(self): # Method to accelerate the car
        print("Car is accelerating") # Indicating the car is accelerating


# Creating an instance of the Car class
my_car = Car() # Creating an instance of the Car class
my_car.start() # Calling the start method to start the car  



#Task 
class Student:
    def __init__(self,name,marks_physics,marks_chemistry,marks_math):
        self.name = name
        self.marks_physics = marks_physics
        self.marks_chemistry = marks_chemistry
        self.marks_math = marks_math


s1 = Student("Sabbir", 88,90,97)
average = (s1.marks_physics + s1.marks_chemistry + s1.marks_math) / 3 # Calculating the average marks
print(f"Average marks of {s1.name} is {average}") #both line are same
# print("Average marks of",s1.name,"is",average) # Another way to print the average marks
print("Average marks if",s1.name,"is",average) 


# same task with using loops
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0 # Initialize sum to 0
        for mark in self.marks: # Loop through each mark in the marks list
            sum += mark # Add the mark to the sum
        print("hi", self.name, "your average mark is", sum / len(self.marks)) # Print the average mark after the loop ends
            
s1 = Student("Sabbir", [88, 90, 97]) # Creating an instance of the Student class with a list of marks
s1.average() # Calling the average method to calculate and print the average marks




# static method

# static methods are methods that belong to the class rather than an instance of the class
# they are defined using the @staticmethod decorator
# static methods do not take self or cls as the first parameter
# they can be called on the class itself or on an instance of the class
# they are used for utility functions that do not require access to instance or class data
# they can be called without creating an instance of the class
# they can be used to perform operations that are related to the class but do not require access to instance or class data
# they can be used to create factory methods that return instances of the class

class Industry:
    @staticmethod 
    def calculate_salary(hours_worked, hourly_rate):
        return hours_worked * hourly_rate

salary = Industry.calculate_salary(40, 20)
print("Calculated salary:", salary)

#another way :
class Industry2:
    @staticmethod 
    def calculate_salary(hours_worked11, hourly_rate11):
        print(hours_worked11 * hourly_rate11)

Industry2.calculate_salary(40, 20)


#abstract 
# ABSTRACT CLASS IN PYTHON
# ------------------------
# An abstract class is a base class that cannot be used to create objects directly.
# It is meant to be inherited by other classes.
# Abstract classes can have regular methods and abstract methods.
# Abstract methods do not have any code in them — they just define what a method should look like.
# Any class that inherits from an abstract class must provide its own version of the abstract methods.
# Abstract classes are used to show only the important features to the user
# and hide the internal details of how things work.hide implementaion details
# To create an abstract class, use the 'abc' module and the @abstractmethod decorator.

# Example:
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")
#
# dog = Dog()       # This works
# animal = Animal() # Error: Cannot create an object from an abstract class

#more aesy code to undertand:
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..🚗")

car1 = Car()
car1.start()


#Encapsulation
# ENCAPSULATION IN PYTHON
# -----------------------
# ENCAPSULATION IN PYTHON
# -----------------------
# Encapsulation means wrapping data and the functions that work on that data
# into a single unit, which is called an object.
# It helps to hide the internal details of how an object works,
# and only shows what is necessary to the outside world.
# This keeps the data safe and makes the code easier to use and maintain.

#Mainy encapsulation is wrapping data and function into single unit (object




#Task
class Account :
        def __init__(self,bal,acc_n):
            self.balance=bal
            self.account_no=acc_n


        # debit method 
        def debit(self,amount):
            self.balance -= amount
            print("BDT",amount,"was debited")
            print("Total balance = ",self.get_balance())

        # credit method
        def credit(self,amount):
            self.balance += amount
            print("BDT",amount,"was credited",)
            print("Total balance = ",self.get_balance())


        def get_balance(self):
            return self.balance

acc1= Account(15000,1234598765)
acc1.debit(1000)
acc1.credit(17000)










      

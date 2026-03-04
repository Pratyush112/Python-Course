#Print Statement: Used to output data to the console.
print("Hello, World!")

#Python supports 3 categrories of data types:
# 1. Basic Data Types: int, float, boolean, complex, string
# 2. Container Types: List, Tuples, Sets, and Dictionary
# 3. User Defined Types: Class and Object

#Basic Data Types: 
    # 1. int: Whole number without a decimal point. It can be positive, negative, or zero. (range: -1e308 to 1e308)
print(type(42))  # Output: <class 'int'>

    # 2. float: Number with a decimal point. It can also be in scientific notation. (range: -1.7e308 to 1.7e308)
print(type(3.14))  # Output: <class 'float'>

    # 3. boolean: Represents one of two values: True or False.
print(type(True))  # Output: <class 'bool'>
print(type(False))  # Output: <class 'bool'>

    # 4. complex: Represents a complex number with a real and imaginary part. (e.g., 3 + 4j)
print(type(3 + 4j))  # Output: <class 'complex'>

    # 5. string: A sequence of characters enclosed in single, double, or triple quotes. (e.g., 'Hello', "World", '''Python''')
print(type("Hello, World!"))  # Output: <class 'str'>


#Container Types:
    # 1. List: An ordered, mutable collection of items. It can contain elements of different data types. (e.g., [1, 'Hello', 3.14])
print(type([1, 'Hello', 3.14]))  # Output: <class 'list'>

    # 2. Tuple: An ordered, immutable collection of items. It can also contain elements of different data types. (e.g., (1, 'Hello', 3.14))
print(type((1, 'Hello', 3.14)))  # Output: <class 'tuple'>

    # 3. Set: An unordered collection of unique items. It is mutable and does not allow duplicate values. (e.g., {1, 2, 3})
print(type({1, 2, 3}))  # Output: <class 'set'>

    # 4. Dictionary: An unordered collection of key-value pairs. It is mutable and allows for fast lookups based on keys. (e.g., {'name': 'Alice', 'age': 30})  
print(type({'name': 'Alice', 'age': 30}))  # Output: <class 'dict'>


#User Defined Types:
    # 1. Class: A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have. (e.g., class Person: ...)
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
print(type(Person))  # Output: <class 'type'>

    # 2. Object: An instance of a class. It is created using the class and can have its own unique attributes and behaviors. (e.g., person1 = Person())
person1 = Person("Alice", 30)
print(type(person1))  # Output: <class '__main__.Person'>
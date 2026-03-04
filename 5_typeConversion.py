#Type Convesion 
#Type conversion is the process of converting one data type to another.
# There are two types of type conversion:
    # 1. Implicit type conversion: This is the automatic conversion of one data type to another data type by the python interpreter.
    # 2. Explicit type conversion: This is the manual conversion of one data type to another data type using built-in functions like int(), float(), str(), etc.

num_1 = 10 
num_2 = 20.5
# Implicit type conversion:
res = num_1 + num_2 # The result will be a float because num_2 is a float and python will convert num_1 to a float before performing the addition.
print(res, "This is the result of implicit type conversion.")

num_1 = int(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
# Explicit type conversion:
res = num_1 + num_2 # The result will be a float because num_2 is a float and python will convert num_1 to a float before performing the addition.
print(res, "This is the result of explicit type conversion.")
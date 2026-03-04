# User Input: 
    # Very import for dynamic applications
    # user input is always a string, and by performing type conversion, we can convert it to the desired data type. 
    
name = input("What is your name?")
print(name)

age = input("What is your age?")
print(age, "This is in string format")
# To change the type of the string to an integer, we need to perform type conversion using the int() funtion. 
age = int(age)
print(age, "This is in integer format")

#another way to get user input and convert it to an integer is: 
age = int(input("What is your age?")) # This is the best practice. 
print(age, "This is in integer format, the industry standard way to get user input and convert it to the desired data type.")
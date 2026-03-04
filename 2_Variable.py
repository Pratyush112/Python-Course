# In python we do not need to declare a variable before using it.

# Dynamic Typing:  
# We can simply assign a value to a varibale and it will be created automatically. The type of the variable will be determined based on the value assigned. This is knwon as dynamic typing.
# Example of Dynamic Typing: name = 'Pratyush' (string), age = 30 (integer), pi = 3.14 (float), complex_num = 3 + 4j (complex), is_valid = True (boolean) -> The type of the variable is determined at runtime based on the value assigned to it.
a = b = c = 10 
c, d, e = 1, 2, 3
f = 1; g = 2; h = 3
print(a, b, c)  # Output: 10 10 10
print(c, d, e)  # Output: 1 2 3
print(f, g, h)  # Output: 1 2 3


# Dynamic Binding: 
# In dynamic binding, we can reassign a variable to a different type of value. The variable can hold values of different types at different times during the program execution. 
# Example of Dynamic Binding: name = 'Pratyush' (string), name = 42 (integer), name = 3.14 (float), name = 3 + 4j (complex), name = True (boolean)
name = "Pratyush"
print(name)  # Output: Pratyush
name = 42
print(name)  # Output: 42
name = 3.14
print(name)  # Output: 3.14
name = 3 + 4j
print(name)  # Output: (3+4j)
name = True
print(name)  # Output: True

# Literals:
# Literals are the fixed values that we use in our code. They can be of various types such as:

# 1. String Literals: These are sequences of characters enclosed in quotes. For example:
name = "John Doe"
unicode = u"\U0001F600" # Unicode string literal for the character '😀'
unicode2 = u"\u00A9" # Unicode string literal for the character '©'
raw_str = r"raw \n str" # Raw string literal where backslashes are treated as literal characters
print(name, unicode, unicode2, raw_str)
# 2. Numeric Literals: These are numbers that can be integers or floating-point numbers. For example:
age = 30
b = 0b1010 # binary literal for 10
c = 0o12 # octal literal for 10
d = 0x1A # hexadecimal literal for 26
pi = 3.14
b1 = 1.5e2 # scientific notation for 150.0
c1 = 1.5e-2 # scientific notation for 0.015
e = 1.5j # complex number literal with imaginary part 1.5
print(age, b, c, d, pi, b1, c1, e)
# 3. Boolean Literals: These are the values True and False. For example:
is_student = True
is_employed = False
print(is_student, is_employed)
#special_literals: These are the literals 'None', which represents the absence of a value. For example:
result = None
a= None # 'a' is assigned the value 'None', means it does not have any value or it is not defined yet. We can later assign a value to 'a' when we have the necessary information or when we want to use it in our code. 
print(result, a)
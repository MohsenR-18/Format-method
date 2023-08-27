# **********************************************
# Beginning of #1 Example

subject = "cat"
object = "mouse"

# Normal type of printing the message
print("Your " + subject + " ate my " + object)

# Using format() method to print the message
print("Your {} ate my {}".format(subject, object))
print("Your {0} ate my {1}".format(subject, object)) # You can use index to put a value instead of {}
print("Your {sub} ate my {obj}".format(sub=subject, obj=object)) # You can use keyword arguments to pass values

# End of #1 Example

# **********************************************

# Beginning of #2 Example

name = "Mohsen"

# Normal type of printing the message
print("Hello, my name is " + name + ". nice to meet you")

# Using format() method to print the message
print("Hello, my name is {}. nice to meet you".format(name))

# You can add padding before, after or between the variable
print("Hello, my name is {:10}. nice to meet you".format(name)) # added 10 spaces after the variable
print("Hello, my name is {:<10}. nice to meet you".format(name)) # added 10 spaces after the variable
print("Hello, my name is {:>10}. nice to meet you".format(name)) # added 10 spaces before the variable
print("Hello, my name is {:^10}. nice to meet you".format(name)) # put the variable between 10 spaces

# End of #2 Example

# **********************************************

# Beginning of #3 Example

PI = 3.14159
num = 1000000

# Normal type of printing the numbers
print("The number PI is " + str(PI))
print("The number is " + str(num))

# Using format() method to print the numbers
print("The number PI is {}".format(PI))
print("The number PI is {:.2f}".format(PI)) # shows only 2 digits after decimal portion (The f is short for float)

print("The number is {}".format(num))
print("The number is {:,}".format(num)) # add "," to split number like 1,000,000
print("The number is {:b}".format(num)) # convert the number into Binary
print("The number is {:o}".format(num)) # convert the number into Octal
print("The number is {:x}".format(num)) # convert the number into Hexadecimal (x or X for uppercase or lowercase)
print("The number is {:e}".format(num)) # convert the number into Scientific numbers (e or E for uppercase or lowercase)

# End of #3 Example

# **********************************************

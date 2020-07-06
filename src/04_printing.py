"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
#print("% 2d " %(10)) not correct??
print("% 2d " %(x))
print("% 2.5f " %(y))
print("%s " % (z))

# Use the 'format' string method to print the same thing
print('{}'.format('10'))
print('{}'.format('2.24552'))
print('{}'.format('I like turtles!'))

# Finally, print the same thing using an f-string
print(f"{x}")
print(f"{y}")
print(f"{z}")
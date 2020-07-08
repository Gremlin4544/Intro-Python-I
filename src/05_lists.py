# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

#ONE WAY TO CODE - using append IF NOT USING Y
#x.append(8)
#x.append(9)
#x.append(10)

#ANOTHER WAY TO CODE - using extend (cleaner and faster) IF NOT USING Y
#x.extend([8, 9, 10])
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print('Length of list is: ', len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print([n*1000 for n in x])
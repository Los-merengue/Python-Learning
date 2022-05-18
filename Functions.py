"""
Print vs. Return in Functions
Here are two valid functions. One returns a value and one simply 
prints a value, without returning anything. Test run this code 
and experiment to understand the difference.
"""

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)


# this returns something
def add_ten(num):
    return(num + 10)

'''
Default Arguments of Functions
'''
def cylinder_volume(height, radius=5):
    """This aspect of code is demonstrating Default Arguments"""
    pi = 3.14159
    return height * pi * radius ** 2
'''
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1           # casted to int
# y = 2.5         # casted to float
# name = 'fady'   # casted to str
# is_cool = True  # casted to bool

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'fady', True)

# show something
print("hello", name)

# Basic math
a = x + y


# Casting
x = str(x)      # "1"
y = int(y)      # 2
z = float(y)    # 2.0

print(type(z), z)

# Operators
# +, -, *, / (float division)
# // (init division)
# % (modulo): 'mod' remainder

print(10 / 2)  # 5.0
print(10 // 3)  # 3
print(10 % 3)  # 1
print(10 ** 3)  # 1000

# = : assignment operator
number = 7
number = number + 3

# += : increment operator
number -= 2
print('number =', number)

number /= 2
print('number =', number)

# Boolean Operators (True or False)
# Boolean (bool) is a type of value that can only be True or False
print(3 == 4)
print(3 != 4)

# > : greater than
print(3 > 4)
print(3 <= 4)

#
x = 1
print(3 < 4 < 5)

print((3 < x) or (x < 5))
print((3 < x) and (x < 5))

num = 10
print((num > 10) and (num / 0 == 0))
print((num > 1) or (num / 0 == 0))
# print((num > 10) or (num / 0 == 0))
print(not True)
print(not False)
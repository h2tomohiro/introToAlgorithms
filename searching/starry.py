# print("*")
# print("*")
# print("*")
#
# print("*", end="\n")
# print("*", end="\n")
# print("*", end="\n")

# What does the code below do? Write a comment explaining each line for Drawing 1.
n = int(input("Choose a number: "))

#Drawing Example
# for row in range(n):  # for each row
#     for column in range(row+1):  # for each column
#         print('*', end='')  # print without newline at the end
#     print()

# Drawing 1
# YOUR CODE BELOW (feel free to comment out previous drawings to make newer ones more clear)

# for each row from 0 to n-1
# for row in range(n):
# # print spaces n -row -1
#     print(" " * (n - row -1), end="")
# # print starts 2 * row + 1
#     print("*" * (2 * row + 1))

# for row in range(n):
# # print spaces n -row -1
#     for col in range(n - row -1):
#         print(" ", end="")
# # print starts 2 * row + 1
#     for col in range(2 * row + 1):
#         print("*")

# for row in range(n):  # for each row
#     for column in range(int(7 - (row+1))):  # for each column
#         print(' ', end='')
#     for column in range(((row+1)*2)-1):  # for each column
#         print('*', end='')
#     print()
# (13)
# 6..1
# 5..3
# 4..5
# 3..7
# 2..9
# 1..11
# 0..13

# Drawing 2
# for row in range(n):  # for each row
#     for column in range(int(7 - (row))):  # for each column
#         print('*', end='')
#     for column in range((row+1)-1):  # for each column
#         print(' ', end='')
#     print()

# for row in range(7,0,-1):
#     print("*" * row)
#
# for row in range(7,0,-1):
#     for col in range(row):
#         print("*", end="")
#     print()

#1..7
#2..6..1
#3..5..2
#4..4..3
#5..3..4
#6..2..5
#7..1..6


# Drawing 3

# for row in range(0,4):  # for each row
#     for column in range(row+1):  # for each column
#         print('*', end='')  # print without newline at the end
#     print()
# for row in range(4,7):  # for each row
#     for column in range(8-(row+1)):  # for each column
#         print('*', end='')  # print without newline at the end
#     print()

# for row in range(1, n//2 + 2):
#     print("*" * row)
# for row in range(n // 2, 0, -1):
#     print("*" * row)

#1..1..3
#2..2..2
#3..3..1
#4..4..0
#5..3..1
#6..2..2
#7..1..3

# Drawing 4
# for row in range(0,4):  # for each row
#     for column in range(int(7 - (row+1))):  # for each column
#         print(' ', end='')
#     for column in range(((row+1)*2)-1):  # for each column
#         print('*', end='')
#     print()

# for row in range(n//2, -1, -1): # 3,2,1,0
#     print(" " * (n//2 - row), end="")
#     print("*" * (2 * row + 1))
#
# for row in range(1, n//2 + 1): # 1, 2, 3
#     print(" " * (n//2 - row), end="")
#     print("*" * (2 * row + 1))

# for row in range(n):
# # print spaces n -row -1
#     print(" " * (n - row -1), end="")
# # print starts 2 * row + 1
#     print("*" * (2 * row + 1))

# Drawing 5
for row in range(n // 2 + 1):# 3,2,1,0
    print(" " * (n // 2 - row), end="")
    print("*" * (2 * row + 1))

for row in range(1, n // 2 + 1, +1):
    print(" " * row, end="")
    print("*" * (n - row * 2))

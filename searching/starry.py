# What does the code below do? Write a comment explaining each line for Drawing 1.
n = int(input("Choose a number: "))

#Drawing Example
# for row in range(n):  # for each row
#     for column in range(row+1):  # for each column
#         print('*', end='')  # print without newline at the end
#     print()

# Drawing 1
for row in range(n):
    print(" " * (n - row -1), end="")
    print("*" * (2 * row + 1))


# Drawing 2
for row in range(n):
    for column in range(int(7 - (row))):
        print('*', end='')
    for column in range((row+1)-1):
        print(' ', end='')
    print()


# Drawing 3
for row in range(0,4):
    for column in range(row+1):
        print('*', end='')
    print()
for row in range(4,7):
    for column in range(8-(row+1)):
        print('*', end='')
    print()


# Drawing 4
for row in range(n//2, -1, -1):
    print(" " * (n//2 - row), end="")
    print("*" * (2 * row + 1))
for row in range(1, n//2 + 1):
    print(" " * (n//2 - row), end="")
    print("*" * (2 * row + 1))


# Drawing 5
for row in range(n // 2 + 1):
    print(" " * (n // 2 - row), end="")
    print("*" * (2 * row + 1))
for row in range(1, n // 2 + 1, +1):
    print(" " * row, end="")
    print("*" * (n - row * 2))

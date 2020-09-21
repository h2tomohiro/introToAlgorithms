# Write a program that takes an user input for an exam mark, and prints
# the grade for that mark - according to the following scheme:
#
#
#   Mark      Grade
#   >= 90       A
#  [80-90)      B
#  [70-80)      C
#  [60-70)      D
#    < 60       F
#
#
# The square and round brackets denote closed and open intervals(range).
# A closed interval includes the number, and open interval excludes it.
# Test your program by print the mark and the grade for a number of different marks.

Mark = int(input("Enter your Mark:"))

if Mark >= 90:
    print("Your Grade is A!")
elif 80 <= Mark < 90:
    print("Your Grade is B!")
elif 70 <= Mark < 80:
    print("Your Grade is C!")
elif 60 <= Mark < 70:
    print("Your Grade is D!")
else:
    print("Your Grade is F")

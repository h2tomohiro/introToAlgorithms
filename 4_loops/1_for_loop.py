# for i in range(10):
#     print(i)

# range(start, end) - start <= < end
# for i in range(100, 0, 1):
#     print(i)

# for i in range(1, 11):
#     print(i, end="10")
#
#
# for i in range(101):
#     print(i%2)

# for i in range(101):
#     if i % 2 == 0:
#      print(i)

# for i in range(101):
#     if i % 2 != 0:
#       print(i)

# school = "Cornerstone"
# for i in school:
#     print(i)

# v = 'a','e','i','o','u'
# w = 'Vancouver'
# count = 0
# for i in w:
#     if i in v:
#      count += 1
# print (count)

#v = 'a','e','i','o','u'
w = 'Vancouver'
count = 0
for i in w:
    if i in "aeiouAEIOU":
     count += 1
print (count)
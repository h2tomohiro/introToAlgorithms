
age = int(input("Enter your age:"))

if age >= 18:
    print("You can start drinking...")
elif 15 <= age <= 17:
    print("Highschool student")
elif 13 <= age <15:
    print("Junior-school student")
elif 7 <= age < 13:
    print("Elementary-school student")
elif 5 <= age < 7:
    print("Kindergarden")
else:
    print("Baby")

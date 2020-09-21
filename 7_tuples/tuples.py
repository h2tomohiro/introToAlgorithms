vowels = ("a", "e", "i", "o", "u")
print(vowels[0])
print("k" in vowels)

vowels.index("e")
vowels.count("i")

# ["hello", "world", "bye", "world"]
# def split_name(): #(name: str) -> (str,str):
#     fullname = name.split("Tomohiro Meo")
#     first = fullname[0]
#     last = fullname[1]
#
#     return first, last
#
# name = split_name("Tomohiro Meo")

livable_provinces = ("BC", "ON", "AB", "QC")

a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)

x = 50
y = 70

x, y = y, x
print(x)
print(y)

def split_names(*names):
    print(names)

split_names("Jinya")
split_names("Carlos", "Martinez", "Redrigo", "Santos")
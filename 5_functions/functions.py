def f(x):
    return x + 2

print(f(3))
print(f(5))
print(f(7))

def print_one():
    print(1)

print_one()

def get_fullname(fn, ln):
    full = fn + "" + ln
    return full

print(get_fullname("Derrick", "Park"))
print(get_fullname("Leo", "Park"))
print(get_fullname("Sean", "Park"))

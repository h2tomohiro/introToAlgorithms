a = [1,2,3]

contacts = {
    "Kazu": {"Canada": "888-998-999", "Japan": "212-123-1234"},
    "Tomo": ["087-823-827", "778-221-332"],
    7: "Hello"
}

print(contacts["Kazu"])
print(contacts["Kazu"]["Canada"])
print(contacts[7])
contacts["Tomo"] = "23344332"
print(contacts)

contacts["Arel"] = "3333333333333333"
print(contacts)

contacts["Shintaro"] = "113233222"
print(contacts)

del contacts[7]
print(contacts)

for key in contacts.keys():
    print(key)

print(contacts.keys())
#print(contacts.keys()[0])

key_list = list(contacts.keys())
print(key_list[0])

key_list = list(contacts.keys())
print(key_list)

for val in contacts.values():
    print(val)

print(type(contacts.values()))
value_list = list(contacts.values())
print(value_list)

if "John" in contacts:
    print("I have John's contacts info")
if "Kazu" in contacts:
    print("I have Kazu's contacts info")

values = list(contacts.values())
#i = values.index("087-823-827")

# 8. iterate through a dictionary with a (key, value) pair
for (k, v) in contacts.items():
    if v == "2333222":
        print(k)

print(type(contacts.items()))
print(list(contacts.items()))

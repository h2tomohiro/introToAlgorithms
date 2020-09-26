# Brainteaser Problems
# 100 Lockers
lockers = []  # 1 means open, 0 means close
# day one
for i in range(100):
    lockers.append(1)

# from day two to day 100 (99 days)
for day in range(2, 100):  # j means the number of days
    for l in range(100):  # k means the number of lockers from 0 to 99
        if l % day == 0:  # every j locker
            if lockers[l] == 1:
                lockers[l] = 0
            else:
                lockers[l] = 1
count = 0
for n in range(len(lockers)):
    if lockers[n] == 1:
        count += 1
print(count)
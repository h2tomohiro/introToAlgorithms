#print(list(range(11)))

def mrange(start,end,steps):
    l = []
    while start < end:
        l.append(start)
        start += steps
    return l
#print(mrange(1,6,2))

def xrange(*args):
    if len(args) == 1:
        return mrange(0, args[0])
    elif len(args) == 2:
        return mrange(args[0], args[1])
    elif len(args) == 3:
        return mrange(args[0], args[1], args[2])
    else:
        raise TypeError("Invalid Number of Arguments!")

print(xrange(1,10,2))
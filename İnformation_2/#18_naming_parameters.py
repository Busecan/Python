def add(*a, extra=0):
    total = 0
    for item in a:
        total += item + extra
    return total


print(add(3, 5, 9, 15.2, 36, extra = 2), file = "a.txt")
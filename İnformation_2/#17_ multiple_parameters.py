def function(*a):
    total = 0
    for item in a:
        total += item
    return total


print(function(3, 5, 9, 15.2, 36))

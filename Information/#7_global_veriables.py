a = 5
def b():
    a = 10 # local variable.
    print(a)


b()
print(a)


def c():
    global a
    a = 10
    print(a)


c()
print(a)
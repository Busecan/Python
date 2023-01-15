a = 5
while a < 10:
    a += 1
    if a == 8:
        continue
    if a == 12:
        break
    print(a)
else:
    print("a = 15 or a > 15")
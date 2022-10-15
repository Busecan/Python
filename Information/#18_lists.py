list = ["Elma", "Armut", "Ayva"]

list.sort()
print(list)

list.reverse()
print(list)

def fonksiyon(n):
  return abs(n - 50)

nmbr_list = [100, 50, 65, 82, 23]
nmbr_list.sort(key=fonksiyon)
print(nmbr_list)
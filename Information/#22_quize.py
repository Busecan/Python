"""
1 - Klavyeden girilen 5 tane sayıyı bir listeye atarak
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca
    göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
"""
list = []
for i in range(0, 5):
    list.append(eval(input()))


def sort_function(a):
    return a * a - 20


list.sort(key=siralama_fonksiyonu)
print(list)
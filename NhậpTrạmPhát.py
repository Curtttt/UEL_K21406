import string
ten = string.ascii_uppercase
n = int(input("Số trạm: "))
tram = []

for i in range(n):
    tg = []
    for j in range(n):
        if i == j:
            tam = 0
            tg.append(tam)
        elif i > j:
            tam = tram[j][i]
            tg.append(tam)
        else:
            tam = float(input("Khoảng cách từ trạm " + str(ten[i]) + " đến trạm " + str(ten[j]) + ": "))
            tg.append(tam)
    tram.append(tg)

print()
for i in range(n):
    print("Khoảng cách trạm", ten[i],":",tram[i])






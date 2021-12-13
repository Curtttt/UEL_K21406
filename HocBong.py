sv, drl, diem, hb , dathb = [], [], [], [], []
mon = ["Toán cao cấp", "Giới thiệu ngành", "Tư duy lập trình", "Kinh tế học vi mô", "Lý luận nhà nước và pháp luật", "Tư tưởng Hồ Chí Minh", "Xã hội học", "Quan hệ quốc tế"]
tc = [3, 2, 3, 3, 3, 2, 2, 2]

def nhapten():
    tam = input("Tên sinh viên: ")
    sv.append(tam)

def nhapdiem():
    tg, j = [], 0
    while j != len(mon):
        try:
            tam = float(input(" " + mon[j] + ": "))
            if tam<0 or tam>10:
                raise Exception
            tg.append(tam)
            diem.append(tg)
            j += 1
        except:
            print("Điểm nhập không hợp lệ!!!")

def nhapdrl():
    tam = float(input("Điểm rèn luyện: "))
    drl.append(tam)

def diemxethb(a, b, c):
    tg = []
    for j in range(len(a)):
        tam = b[j] * a[j]
        tg.append(tam)
    return ( (sum(tg) / sum(tc)) + (c * 0.2) )

n = int(input("Số sinh viên: "))
m = int(input("Số sinh viên đạt được học bổng: "))
print("*" * 62)
for i in range(n):
    print(i+1, end=".")
    nhapten()
    nhapdiem()
    nhapdrl()
    print("*" * 62)

for i in range(len(sv)):
    hb.append( diemxethb(tc, diem[i], drl[i]) )

while len(dathb) != m:
    x = hb.index(max(hb))
    dathb.append(x)
    sv.pop(x)

print("Sinh viên đạt được học bổng: ", end="")
for i in range(len(dathb)):
    print(sv[i] + "(" + str(dathb[i]) + ")", end=" ")

print(hb)
print(diem)












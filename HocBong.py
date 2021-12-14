sv, drl, diem, hb, dathb, tg1, tg2 = [], [], [], [], [], [], []
mon = ["Toán cao cấp", "Giới thiệu ngành", "Tư duy lập trình"] #, "Kinh tế học vi mô", "Lý luận nhà nước và pháp luật", "Tư tưởng Hồ Chí Minh", "Xã hội học", "Quan hệ quốc tế"]
tc = [3, 2, 3] #, 3, 3, 2, 2, 2]

def nhapten(sv):
    tam = input("Tên sinh viên: ")
    sv.append(tam)

def nhapdiem(diem):
    tg, j = [], 0
    while j != len(mon):
        try:
            tam = float(input(" " + mon[j] + ": "))
            if tam < 0 or tam > 10:
                raise Exception
            tg.append(tam)
            diem.append(tg)
            j += 1
        except:
            print("Điểm nhập không hợp lệ!!!")


def nhapdrl(drl):
    tam = float(input("Điểm rèn luyện: "))
    drl.append(tam)


def diemxethb(a, b, c):
    tg = []
    for j in range(len(a)):
        tam = b[j] * a[j]
        tg.append(tam)
    return round((sum(tg) / sum(tc)) + (c * 0.2), 2)

n = 0
while n < 5:
    try:
        n = int(input("Số sinh viên: "))
        if n < 5:
            raise Exception
    except:
        print("Số lượng tối thiểu là 5 bạn!!!")

for i in range(n):
    print("*" * 62)
    print(i + 1, end=".")
    nhapten(sv)
    nhapdiem(diem)
    nhapdrl(drl)
    print("Điểm xét học bổng:", diemxethb(tc, diem[i], drl[i]))
    hb.append(diemxethb(tc, diem[i], drl[i]))

while len(tg1) != 5:
    x = hb.index(max(hb))
    tg2.append(hb[x])
    tg1.append(sv[x])
    hb.pop(x)
    sv.pop(x)
dathb.append(tg1)
dathb.append(tg2)

print("Sinh viên đạt được học bổng: ", end="")
for i in range(5):
    print(dathb[0][i] + "(" + str(dathb[1][i]) + ")", end=" | ")












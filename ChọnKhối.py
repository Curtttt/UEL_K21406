diem, i = [], 0
mon = ["Toán", "Lí", "Hóa", "Sinh", "Sử", "Địa", "Văn", "Anh"]
khoi = ["A", "B", "C", "D"]
diemkhoi = [0, 0, 0, 0]

def tinhdiem(a, b, c):
        return a + b + c

while len(diem) != len(mon):
        try:
                tam = float(input(mon[i] + ": "))
                if tam < 0 or tam > 10:
                        raise Exception
                diem.append(tam)
                i += 1
        except:
                print("Điểm không hợp lệ!!!")

diemkhoi[0] = tinhdiem(diem[0], diem[1], diem[2])
diemkhoi[1] = tinhdiem(diem[0], diem[2], diem[3])
diemkhoi[2] = tinhdiem(diem[6], diem[5], diem[4])
diemkhoi[3] = tinhdiem(diem[7], diem[6], diem[0])
x = diemkhoi.index(max(diemkhoi))

for i in range(len(khoi)):
        print("Tổng điểm khối %s: %s" %(khoi[i], diemkhoi[i]))
print("Khối nên chọn: ", khoi[x])





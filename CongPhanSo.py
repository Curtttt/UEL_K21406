kq ,ms, ts = [], [], []
tich, i, n = 1, 0, 0

while n <= 1:
    try:
        n = int(input("số phân số cần tính: "))
        if n <= 1:
            raise Exception
    except:
        print("Số phân số tối thiểu là 2!!!")

while len(ms) != n:
    try:
        tgt = input("Phân số thứ " + str(i + 1) + ": ")
        tg = tgt.split("/")
        ts.append(int(tg[0]))
        ms.append(int(tg[1]))
        i += 1
    except:
        print("Không hợp lệ!!!")

for i in reversed(range(1, min(ms)+1)):
    dem = 0
    for m in ms:
        if m % i == 0:
            dem += 1
    if dem == len(ms):
        ucln = i
        break
    else: ucln = 1

for m in ms:
    tich *= m
bcnn = tich / ucln

for i in range(n):
    tg = ts[i] * (bcnn / ms[i])
    kq.append(tg)

tsc, msc = int(sum(kq)), int(bcnn)

for i in reversed(range(1, min(msc, tsc)+1)):
    if (tsc % i == 0) and (msc % i == 0):
        ucc = i
        break

print("Kết quả: ", int(tsc/ucc), "/" , int(msc/ucc), sep="")

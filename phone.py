sl, tong= [], []
m = 5
gia = [21990000, 24990000, 30990000, 33990000 ]
mat_hang = ["iphone 13 mini", "iphone 13", "iphone 13 pro", "iphone 13 pro max"]

def mau_ma(mat_hang, b, n):
    tam = int(input("Số lượng " + mat_hang[n] + ": "))
    b.append(tam)

def nhapsolieu(mat_hang, b):
    j = 0
    if m == 4:
        for i in range(m):
            mau_ma(mat_hang, b, i)
    else:
        while j != m:
            try:
                mau = input("Nhập mẫu iphone: ")
                match mau:
                    case "mini":
                        mau_ma(mat_hang, b, 0)
                    case "thường":
                        mau_ma(mat_hang, b, 1)
                    case "pro":
                        mau_ma(mat_hang, b, 2)
                    case "prm":
                        mau_ma(mat_hang, b, 3)
                    case _:
                        raise Exception
                j += 1
            except:
                print("Không hợp lệ!!!")


def tinhdoanhthu(a, b, c):
    x = a * b
    c.append(x)
    return c

while m > 4:
    try:
        m = int(input("Số lượng mẫu iphone bán đc: "))
        if m > 4:
            raise Exception
    except:
        print("Không hợp lệ!!!")
nhapsolieu(mat_hang, sl)

for i in range(m):
    tinhdoanhthu(sl[i], gia[i], tong)

print("Doanh thu cuối ngày:", format(sum(tong), ',d'))

x = input("Bạn có muốn cập nhật doanh thu? ")
while x == "có":
    print( "*" * 62)
    sl2, tong_moi = [], []
    nhapsolieu(mat_hang, sl2)
    for i in range(m):
        sl[i] += sl2[i]
    for i in range(m):
       tinhdoanhthu(sl[i], gia[i], tong_moi)
    tien_moi = sum(tong_moi) + sum(tong)
    print("Doanh thu cuối ngày:", format(tien_moi, ',d'))
    x = input("Bạn có muốn cập nhật doanh thu? ")
else:
    print("Hoàn tất")

print(sl2)
print(sl)



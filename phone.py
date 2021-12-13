x, tong = "có", 0
gia = [1, 2, 3, 4]#[21990000, 24990000, 30990000, 33990000]
mat_hang = ["iphone 13 mini", "iphone 13", "iphone 13 pro", "iphone 13 pro max"]

def xuli_sl(gia, mat_hang, sl_gia, n):
    tg = [0, 0]
    tam = int(input("Số lượng " + mat_hang[n] + ": "))
    tg[0], tg[1] = tam, gia[n]
    sl_gia.append(tg)
    return sl_gia

def tinhdoanhthu(sl_gia):
    y = 0
    for i in range(len(sl_gia)):
        tam = sl_gia[i][0] * sl_gia[i][1]
        y += tam
    return y

while x == "có":
    print("*" * 62)
    m,j = 5, 0
    sl_gia = []

    while m > 4:
        try:
            m = int(input("Số lượng mẫu iphone bán đc: "))
            if m > 4:
                raise Exception
        except:
            print("Không hợp lệ!!!")

    if m == 4:
        for i in range(m):
            xuli_sl(gia, mat_hang, sl_gia, i)
    else:
        while j != m:
            try:
                mau = input("Nhập mẫu iphone: ")
                if mau == "mini":
                    xuli_sl(gia, mat_hang, sl_gia, 0)
                elif mau == "thuong":
                    xuli_sl(gia, mat_hang, sl_gia, 1)
                elif mau == "pro":
                    xuli_sl(gia, mat_hang, sl_gia, 2)
                elif mau == "prm":
                    xuli_sl(gia, mat_hang, sl_gia, 3)
                else:
                    raise Exception
                j += 1
            except:
                print("Không hợp lệ!!!")

    tong += tinhdoanhthu(sl_gia)
    print("Doanh thu: ", format(tong, ',d'))
    x = input("Bạn có muốn cập nhật doanh thu? ")









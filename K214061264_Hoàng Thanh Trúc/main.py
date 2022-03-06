from function import *

print("*" * 62)
print("1.Kiểm tra năm nhuận")
print("2.Chuyển đổi năm dương lịch sang âm lịch")
print("3.Kiểm tra số nguyên tố, số chính phương")
print("4.Tính tổng n số hạng")
print("5.Tính tổng n số hạng(đệ quy)")
print("6.Tìm ước số chung lớn nhất của 2 số")
print("7.Tìm ước số chung lớn nhất của 2 số(đệ quy)")
print("8.Tính biểu thức cộng lũy thừa")
print("9.tính biểu thức cộng lũy thừa (đệ quy)")
print("10.Tính tổng phân số")
print("11.Tính tổng phân số(đệ quy)")
print("12.Tính chỉnh hợp, tổ hợp chập k của n phần tử")
print("13.Giải phương trình bậc 2")
print("14.Tính chỉ số BMI")
print("15.Kiểm tra số hoàn thiện, số thịnh vượng")
print("0.Thoát")

def inp(m):
    try:
        while True:
            m = int(input(f"Nhập {m}: "))
            break
        return m
    except: print("Không hợp lệ!!!")

while True:
    while True:
        try:
            print("*" * 62)
            x = int(input("Nhập chương trình bạn muốn thực hiện: "))
            if not 0 <= x <= 15:
                raise Exception
            else:
                break
        except:
            print("Hãy nhập số từ 0 đến 15!!!")

    if x == 0: break

    if x == 1:
        n = inp("năm")
        print(cau1(n))

    if x == 2:
        n = inp("năm")
        print(cau2(n))

    if x == 3:
        n = inp("n")
        print(cau3(n))

    if x == 4:
        n = inp("n")
        print(cau4(n))

    if x == 5:
        n = inp("n")
        print(cau4_dequy(n))

    if x == 6:
        a = inp("số thứ nhất")
        b = inp("số thứ hai")
        print(cau5(a, b))

    if x == 7:
        a = inp("số thứ nhất")
        b = inp("số thứ hai")
        print(cau5_dequy(a, b))

    if x == 8:
        n = inp("n")
        x = inp("x")
        print(cau6(x, n))

    if x == 9:
        n = inp("n")
        x = inp("x")
        print(cau6_dequy(x, n))

    if x == 10:
        n = inp("n")
        print(cau7(n))

    if x == 11:
        n = inp("n")
        print(cau7_dequy(n))

    if x == 12:
        while True:
            try:
                n = int(input("Nhập n: "))
                k = int(input("Nhập k: "))
                if n < k: raise Exception
                break
            except:
                print("Không hợp lệ!!!")
        print(cau8(n, k))

    if x == 13:
        try:
            while True:
                a = float(input("Nhập a: "))
                b = float(input("Nhập b: "))
                c = float(input("Nhập c: "))
                if a == 0 and b == 0:
                    raise Exception
                break
        except:
            print("Không hợp lệ!!!")
        print(cau9(a, b, c))

    if x == 14:
        try:
            while True:
                cao = float(input("Nhập chiều cao(m): "))
                nang = float(input("Nhập cân nặng(kg): "))
                break
        except:
            print("Không hợp lệ!!!")
        print(cau10(cao, nang))

    if x == 15:
        n = inp("n")
        print(cau11(n))




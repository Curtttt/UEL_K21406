import math

def cau1(n):
    if (n % 400 == 0) or ((n % 4 == 0) and (n % 100 != 0)):
        return "Năm nhuận"
    else:
        return "Không phải năm nhuận"

def cau2(n):
    can = ['Canh', 'Tân', 'Nhâm,', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
    return f"{can[n%10]} {chi[n%12]}"

def cau3(n):
    if math.sqrt(n).is_integer():
         scp = True
    else: scp = False
    snt = True
    if n < 2: snt = False
    else:
        for i in range(2, n):
            if n % i == 0: snt = False
    if snt: return "Số nguyên tố"
    if scp: return "Số chính phương"

def cau4(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def cau4_dequy(n):
    if n == 0:
        return 0
    else:
        return n + cau4_dequy(n-1)

def cau5(a, b):
    while not a == b:
        if a > b:
            a -= b
        else: b -= a
    return a

def cau5_dequy(a, b):
    return a if b == 0 else cau5_dequy(b, a % b)

def cau6(x,n):
    s = 0
    for i in range(1, n+1):
        s += x**(2*i)
    return s

def cau6_dequy(x, n):
    if n == 0:
        return 0
    else:
        return x**(2*n) + cau6_dequy(x, n-1)

def cau7(n):
    m, s = 0, 0
    for i in range(1, n+1):
        m += i
        s += 1/m
    return s

def cau7_dequy(n):
    if n == 0:
        return 0
    else:
        return 1/sum(range(1, n+1)) + cau7_dequy(n-1)

def giaithua(n):
    return 1 if n == 0 else n * giaithua(n-1)

def cau8(n, k):
    A = giaithua(n) / giaithua(n-k)
    C = giaithua(n) / (giaithua(k) * giaithua(n-k))
    return f"Chỉnh hợp chập k của n phần tử: {int(A)} \nTổ hợp chập k của n phần tử: {int(C)}"

def cau9(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        return f"Phương trình có nghiệm kép x1 = x2 = {-(b / (2 * a))} "
    else:
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 = ", (-(b) + math.sqrt(delta)) / (2 * a))
        print("x1 = ", (-(b) - math.sqrt(delta)) / (2 * a))

def cau10(h, w):
    BMI = w / (h**2)
    if BMI<18.5:
        return "Gầy"
    elif BMI<25:
        return "Bình thường"
    elif BMI<30:
        return "Mập"
    else: return "Béo phì"

def cau11(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return "Số hoàn thiện"
    else: return "Số thịnh vượng"





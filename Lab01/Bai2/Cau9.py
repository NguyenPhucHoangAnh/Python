n = int(input("Nhập n: "))

if n < 0:
    print("Vui lòng nhập lại!")
elif n == 0 or n == 1:
    print(f"Giai thừa của {n} là 1")
else:
    kq = 1
    for i in range (2, n + 1):
        kq = kq*i
    print(f"Giai thừa của {n} là {kq}")
n = int(input("Nhập n:"))
if (n < 0):
    print("Vui lòng nhập số nguyên dương")
elif (n == 0 or n == 1):
    print(f"Số Fibonacci thứ {n} là : {1}")
else:
    a = 1
    b = 1
    for i in range (n - 2):
            a, b = b, a + b
    print(f"Số Fibonacci thứ {n} là: {b}")
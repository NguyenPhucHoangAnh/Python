def is_perfect_square(x):
    s = int(x ** 0.5)
    return s * s == x

def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    
    # Kiểm tra xem 5 * n^2 + 4 hoặc 5 * n^2 - 4 có phải là số chính phương
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Số nguyên cần kiểm tra
number = int(input("Nhập số nguyên cần kiểm tra: "))

if is_fibonacci(number):
    print(f"{number} là số Fibonacci.")
else:
    print(f"{number} không phải là số Fibonacci.")
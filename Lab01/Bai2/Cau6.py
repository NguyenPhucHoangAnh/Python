def fibonacci_sum(n):
    fib = [0, 1]  # Bắt đầu với hai số Fibonacci đầu tiên
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return sum(fib)

# Số lượng số Fibonacci cần tính tổng
n = int(input("Nhập số lượng số Fibonacci: "))
total_sum = fibonacci_sum(n)
print(f"Tổng của {n} số Fibonacci đầu tiên là: {total_sum}")
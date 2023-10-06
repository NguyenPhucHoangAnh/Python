import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

delta = a*a - 4*b*c

if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = (-b/(2*a))
    print(f"Phương trình có nghiệm kép x = {x}")
else:
    x1 = ((-b + math.sqrt(delta))/(2*a))
    x2 = ((-b - math.sqrt(delta))/(2*a))
    print(f"Phương trình có 2 nghiệm x1 = {x1} và x2 = {x2}")
import math
import array as arr

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array('i', a)

#Xuất tất cả các số lẻ không chia hết cho 5:
for x in a:
    if x % 2 != 0 and x % 5 != 0:
        b.append(x)
        print("Tất cả các số lẻ không chia hết cho 5 là:", b)
        
#Xuất tất cả các số Fibonacci:

#Tìm số nguyên tố lớn nhất:

        
#Tính trung bình các số lẻ:
dem = 0
tong = 0
kq = 0

for x in b:
    if x %2 != 0:
        dem += 1
        tong += x
        kq = tong/dem
        
        print("Trung bình các số lẻ là: ", kq)
        
#Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng:
        
    
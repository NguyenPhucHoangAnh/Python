import math
 
def kiemTraSoNguyenTo(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
 
    # check so nguyen to khi n >= 2
    a = int(math.sqrt(n));
    for i in range(2, a + 1):
        if (n % i == 0):
            return False;
    return True;
n = int(input("Nhập số nguyên dương n = "));
print ("Tất cả các số nguyên tố nhỏ hơn", n, "là:");
sb = "";
if (n >= 2):
    sb = sb + "2" + " ";
for i in range (3, n+1):
    if (kiemTraSoNguyenTo(i)):
        sb = sb + str(i) + " ";
    i = i + 2;
print(sb);
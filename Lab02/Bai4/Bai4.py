from math import gcd

from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self.rut_gon()

    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __str__(self):
        return f"{self.tu}/{self.mau}"

    def __add__(self, other):
        new_tu = self.tu * other.mau + self.mau * other.tu
        new_mau = self.mau * other.mau
        return PhanSo(new_tu, new_mau)

class DanhSachPhanSo:
    def __init__(self, danh_sach=[]):
        self.danh_sach = danh_sach

    def dem_so_am(self):
        count = 0
        for phan_so in self.danh_sach:
            if phan_so.tu * phan_so.mau < 0:
                count += 1
        return count

    def tim_duong_nho_nhat(self):
        duong_nho_nhat = None
        for phan_so in self.danh_sach:
            if phan_so.tu * phan_so.mau > 0:
                if duong_nho_nhat is None or phan_so.tu / phan_so.mau < duong_nho_nhat.tu / duong_nho_nhat.mau:
                    duong_nho_nhat = phan_so
        return duong_nho_nhat

    def tim_vi_tri_cua_phan_so(self, x):
        vi_tri = []
        for i, phan_so in enumerate(self.danh_sach):
            if phan_so.tu == x.tu and phan_so.mau == x.mau:
                vi_tri.append(i)
        return vi_tri

    def tong_so_am(self):
        tong = PhanSo(0, 1)
        for phan_so in self.danh_sach:
            if phan_so.tu * phan_so.mau < 0:
                tong = tong + phan_so
        return tong

    def xoa_phan_so(self, x):
        self.danh_sach = [phan_so for phan_so in self.danh_sach if phan_so.tu != x.tu or phan_so.mau != x.mau]

    def xoa_tu(self, x):
        self.danh_sach = [phan_so for phan_so in self.danh_sach if phan_so.tu != x]

    def sap_xep(self, key=None, reverse=False):
        self.danh_sach.sort(key=key, reverse=reverse)

    def hien_thi(self):
        for phan_so in self.danh_sach:
            print(phan_so)

# Tạo danh sách phân số
ds_phan_so = DanhSachPhanSo([
    PhanSo(3, 4),
    PhanSo(-2, 5),
    PhanSo(1, -3),
    PhanSo(2, 7),
    PhanSo(4, 9),
    PhanSo(1, 2),
    PhanSo(-3, 8)
])

print("Danh sách phân số:")
ds_phan_so.hien_thi()

print("\nSố phân số âm trong danh sách:", ds_phan_so.dem_so_am())

duong_nho_nhat = ds_phan_so.tim_duong_nho_nhat()
print("\nPhân số dương nhỏ nhất:", duong_nho_nhat)

x = PhanSo(1, 2)
vi_tri = ds_phan_so.tim_vi_tri_cua_phan_so(x)
print("\nVị trí của phân số", x, "trong danh sách:", vi_tri)

tong_so_am = ds_phan_so.tong_so_am()
print("\nTổng các phân số âm:", tong_so_am)

xoa_phan_so = PhanSo(3, 4)
ds_phan_so.xoa_phan_so(xoa_phan_so)
print("\nDanh sách sau khi xóa phân số", xoa_phan_so)
ds_phan_so.hien_thi()

ds_phan_so.xoa_tu(1)
print("\nDanh sách sau khi xóa các phân số có tử bằng 1")
ds_phan_so.hien_thi()

ds_phan_so.sap_xep(key=lambda phan_so: phan_so.tu, reverse=False)
print("\nDanh sách sau khi sắp xếp tăng theo tử:")
ds_phan_so.hien_thi()

ds_phan_so.sap_xep(key=lambda phan_so: phan_so.tu, reverse=True)
print("\nDanh sách sau khi sắp xếp giảm theo tử:")
ds_phan_so.hien_thi()

ds_phan_so.sap_xep(key=lambda phan_so: phan_so.mau, reverse=False)
print("\nDanh sách sau khi sắp xếp tăng theo mẫu:")
ds_phan_so.hien_thi()

ds_phan_so.sap_xep(key=lambda phan_so: phan_so.mau, reverse=True)
print("\nDanh sách sau khi sắp xếp giảm theo mẫu:")
ds_phan_so.hien_thi()

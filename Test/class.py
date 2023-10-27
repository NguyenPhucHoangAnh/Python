from datetime import datetime
import pandas as pd
import tkinter as tk
from tkinter import ttk

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime):
        self.__maSo = maSo  # private
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso

    @property
    def hoTen(self):
        return self.__hoTen

    @hoTen.setter
    def hoTen(self, hoten):
        self.__hoTen = hoten

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @ngaySinh.setter
    def ngaySinh(self, ngaySinh):
        self.__ngaySinh = ngaySinh

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    def __str__(self):
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")


class DanhSachSV:
    def __init__(self):
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.rsplit(' ', 1)[-1] == ten]

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]

#Đọc file xlsx    
dp = pd.read_excel("sinhvien.xlsx")
ds=DanhSachSV()
for index, row in dp.iterrows():
    maSo = row['MaSo']
    hoTen = row['HoTen']
    ngaySinh = row['NgaySinh']
    sv = SinhVien(maSo, hoTen, ngaySinh)
    ds.themSinhVien(sv)

#dp = pd.read_json("sinhvien.json")
# ds=DanhSachSV()
# #Đọc File Json
# for i in range(len(dp)):
#     row = dp.iloc[i]
#     maSo = row['MaSo']
#     hoTen = row['HoTen']
#     ngaySinh = row['NgaySinh']
#     sv = SinhVien(maSo, hoTen, ngaySinh)
#     ds.themSinhVien(sv)

ds.xuat()

msTim = int(input("Nhập vào mã số muốn tìm: "))
kq = ds.timSvTheoMssv(msTim)
print("Đã tìm thấy sinh viên có mã số: ", msTim)
for sv in kq:
    sv.xuat()
print(ds.timVTSvTheoMssv(msTim))  # vị trí của sinh viên, bắt đầu từ 0

# xoa sinh vien
msXoa = int(input("Nhập vào mã số muốn xóa: "))
ds.xoaSvTheoMssv(msXoa)
ds.xuat()

# tim ten Nam
ten = input("Nhập tên muốn tìm: ")
kq = ds.timSvTheoTen(ten)
print("Đã tìm thấy sinh viên có tên: ", ten)
for sv in kq:
    sv.xuat()

# tim truoc ngay sinh truoc 15/06/2000
ngay = datetime.strptime("15/06/2000", "%d/%m/%Y")
kqNgay = ds.timSvSinhTruocNgay(ngay)
print("Đã tìm thấy ngày sinh trước 15/06/2000: ")
for sv in kqNgay:
    sv.xuat()
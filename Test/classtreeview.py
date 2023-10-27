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
    
class SinhVienApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Sinh Viên")

        self.danh_sach_sv = DanhSachSV()
        self.load_du_lieu_tu_excel()
        
        self.tree = ttk.Treeview(root, columns=("maso", "hoten", "ngaysinh"), show = 'headings')
        self.tree.heading("maso", text="Mã số")
        self.tree.heading("hoten", text="Họ tên")
        self.tree.heading("ngaysinh", text="Ngày sinh")
        self.tree.pack()

        self.hien_thi_danh_sach_sinh_vien()

    def load_du_lieu_tu_excel(self):
        dp = pd.read_excel("sinhvien.xlsx")
        for index, row in dp.iterrows():
            maSo = row['MaSo']
            hoTen = row['HoTen']
            ngaySinh = row['NgaySinh']
            sv = SinhVien(maSo, hoTen, ngaySinh)
            self.danh_sach_sv.themSinhVien(sv)

    def hien_thi_danh_sach_sinh_vien(self):
        self.tree.delete(*self.tree.get_children())
        for sv in self.danh_sach_sv.dssv:
            self.tree.insert("", "end", values=(sv.maSo, sv.hoTen, sv.ngaySinh))


if __name__ == "__main__":
    root = tk.Tk()
    app = SinhVienApp(root)
    root.mainloop()
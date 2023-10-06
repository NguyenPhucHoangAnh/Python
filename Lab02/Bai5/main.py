from datetime import datetime

from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from danh_sach_sinh_vien import DanhSachSv

sv1 = SinhVienChinhQuy(2115184, "Nguyễn Phúc Hoàng Anh", datetime.strptime("27/7/2002", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(1985455, "Nguyễn Văn C", datetime.strptime("20/7/2002", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiCQ(2012154, "Thái Thị Thu", datetime.strptime("24/10/2002", "%d/%m/%Y"),"Cao đẳng", 1.5)
sv4 = SinhVienPhiCQ(1958874, "Nguyễn Thanh Trà", datetime.strptime("12/9/2003", "%d/%m/%Y"),"Cao đẳng", 2)
sv5 = SinhVienPhiCQ(2001545, "Nguyễn Thành Nam", datetime.strptime("30/7/2003", "%d/%m/%Y"),"Trung cấp", 2)
sv6 = SinhVienChinhQuy(2115188, "Nguyễn Dương Công Bảo", datetime.strptime("10/11/2003", "%d/%m/%Y"), 70)
sv7 = SinhVienPhiCQ(2001245, "Lê Hoài Nam", datetime.strptime("15/8/2002", "%d/%m/%Y"), "Trung cấp", 2.5)
sv8 = SinhVienChinhQuy(2111878, "Võ Mạnh Quốc", datetime.strptime("10/3/2003", "%d/%m/%Y"), 50)

dssv = DanhSachSv()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

dssv.xuat()

vt = dssv.timSVTheoMs(2115184)
print(f"Sinh viên ở vị trí thứ {vt + 1} trong danh sách")

kq = dssv.timSVTheoLoai("chinhquy")
print("Danh sách sinh viên theo loại: ")
for sv in kq:
    print(sv)
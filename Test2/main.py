import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import pandas
from DanhSachSinhVien import DanhSachSinhVien

dssv = DanhSachSinhVien()
dssv.DocTuExcel()

def btnClick():
    HienThiTreeView()
    tk.messagebox.showerror(title='Loi!',message='Doc that bai!')

#Ham treeview
def HienThiTreeView():
    tree= ttk.Treeview(root, columns=("mssv","hoTen","lop","diemTB"), show = 'headings')
    tree.heading('mssv',text="Ma So")
    tree.heading('hoTen',text="Ho ten")
    tree.heading('lop',text="Lop")
    tree.heading('diemTB',text="Diem TB")
    tree.grid(row=2, columnspan=3)
    for sv in dssv.danhSach:
        tree.insert("","end", values=(sv.mssv, sv.hoTen, sv.lop, sv.diemTB))

def VeDiemTB():
    x=[sv.hoTen for sv in dssv.danhSach]
    y=[sv.diemTB for sv in dssv.danhSach]
    plt.bar(x,y)
    plt.show()
    #Two  lines to make our compiler able to draw:
    plt.savefig(sys.stdout.buffer)
    sys.stdout.flush()

root = tk.Tk()
root.title("Form Sinh Vien")

lbl= tk.Label(root,text='Nhap Duong Dan')
txt= tk.Entry(root)
btn= tk.Button(root, text = 'Doc File', command= btnClick)
btn_Line=tk.Button(root, text = 'Bieu Do Cot', command=VeDiemTB)


lbl.grid(row = 0, column=0)
txt.grid(row =0, column = 1)
btn.grid(row =0, column = 2)
btn_Line.grid(row=1, column=0)

root.mainloop()
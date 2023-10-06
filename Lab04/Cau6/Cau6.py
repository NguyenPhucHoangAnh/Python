import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import *
import re
import openpyxl

# Hàm kiểm tra mã số sinh viên hợp lệ
def is_valid_student_id(student_id):
    return bool(re.match(r'^\d{7}$', student_id))

# Hàm kiểm tra email hợp lệ
def is_valid_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+$', email))

# Hàm kiểm tra số điện thoại hợp lệ
def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$', phone))

# Hàm kiểm tra học kỳ hợp lệ
def is_valid_semester(semester):
    return semester in ['1', '2', '3']

# Hàm kiểm tra định dạng ngày sinh hợp lệ
def is_valid_date_of_birth(date_of_birth):
    return bool(re.match(r'^\d{2}/\d{2}/\d{4}$', date_of_birth))

# Hàm lưu thông tin vào tệp Excel
def save_to_excel(student_id, full_name, email, phone, semester, date_of_birth, academic_year, selected_courses):
    wb = openpyxl.load_workbook('C:\\Python\\Lab04\\Cau6\\student_info.xlsx')
    sheet = wb.active
    row = [student_id, full_name, email, phone, semester, date_of_birth, academic_year] + selected_courses
    sheet.append(row)
    wb.save('C:\\Python\\Lab04\\Cau6\\student_info.xlsx')
    messagebox.showinfo("Thông báo", "Đăng ký thành công!")

# Hàm xử lý sự kiện khi nhấn nút Đăng ký
def register():
    student_id = student_id_entry.get()
    full_name = full_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    semester = semester_var.get()
    date_of_birth = date_of_birth_entry.get()
    academic_year = academic_year_var.get()
    
    selected_courses = []
    for course_var in course_vars:
        if course_var.get():
            selected_courses.append(course_var.get())
    
    if not student_id or not full_name or not email or not phone or not semester or not date_of_birth or not academic_year:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        return
    
    if not is_valid_student_id(student_id):
        messagebox.showerror("Lỗi", "Mã số sinh viên không hợp lệ!")
        return
    
    if not is_valid_email(email):
        messagebox.showerror("Lỗi", "Email không hợp lệ!")
        return
    
    if not is_valid_phone(phone):
        messagebox.showerror("Lỗi", "Số điện thoại không hợp lệ!")
        return
    
    if not is_valid_semester(semester):
        messagebox.showerror("Lỗi", "Học kỳ không hợp lệ!")
        return
    
    if not is_valid_date_of_birth(date_of_birth):
        messagebox.showerror("Lỗi", "Ngày sinh không hợp lệ! (dd/mm/yyyy)")
        return
    
    if not selected_courses:
        messagebox.showerror("Lỗi", "Vui lòng chọn ít nhất một môn học!")
        return
    
    save_to_excel(student_id, full_name, email, phone, semester, date_of_birth, academic_year, selected_courses)

# Tạo giao diện
root = tk.Tk()
root.title("Đăng ký sinh viên")
root.geometry("600x450")

# Mã số sinh viên
student_id_label = tk.Label(root, text="THÔNG TIN SINH VIÊN")
student_id_label.grid(row=0, column=1, sticky= W, pady = 2)
student_id_label = tk.Label(root, text="Mã số sinh viên:")
student_id_label.grid(row=1, column=0, sticky = W, pady = 2)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=1, column=1, ipadx=100)

# Họ tên sinh viên
full_name_label = tk.Label(root, text="Họ tên sinh viên:")
full_name_label.grid(row=2, column=0, sticky = W, pady = 2)
full_name_entry = tk.Entry(root)
full_name_entry.grid(row=2, column=1, ipadx=100)

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=3, column=0, sticky = W, pady = 2)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, ipadx=100)

# Số điện thoại
phone_label = tk.Label(root, text="Số điện thoại:")
phone_label.grid(row=4, column=0, sticky = W, pady = 2)
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1, ipadx=100)

# Học kỳ
semester_label = tk.Label(root, text="Học kỳ:")
semester_label.grid(row=5, column=0, sticky = W, pady = 2)
semester_var = tk.StringVar()
semester_var.set("1")
semester_radio1 = tk.Radiobutton(root, text="1", variable=semester_var, value="1")
semester_radio2 = tk.Radiobutton(root, text="2", variable=semester_var, value="2")
semester_radio3 = tk.Radiobutton(root, text="3", variable=semester_var, value="3")
semester_radio1.grid(row=5, column=1, sticky = W, pady = 2)
semester_radio2.grid(row=6, column=1, sticky = W, pady = 2)
semester_radio3.grid(row=7, column=1, sticky = W, pady = 2)

# Ngày sinh
date_of_birth_label = tk.Label(root, text="Ngày sinh (dd/mm/yyyy):")
date_of_birth_label.grid(row=8, column=0, sticky = W, pady = 2)
date_of_birth_entry = tk.Entry(root)
date_of_birth_entry.grid(row=8, column=1, ipadx=100)

# Năm học
academic_year_label = tk.Label(root, text="Năm học:")
academic_year_label.grid(row=9, column=0, sticky = W, pady = 2)
academic_year_var = tk.StringVar()
academic_year_var.set("2022-2023")
academic_year_optionmenu = tk.OptionMenu(root, academic_year_var, "2022-2023", "2023-2024", "2024-2025")
academic_year_optionmenu.grid(row=9, column=1, sticky = W, pady = 2)

# Môn học
courses_label = tk.Label(root, text="Chọn môn học:")
courses_label.grid(row=10, column=0, sticky = W, pady = 2)
course_vars = []
course_checkboxes = []
course_names = ["Lập trình Java", "Lập trình Python", "Công nghệ phần mềm", "Phát triển ứng dụng web"]
for i, course_name in enumerate(course_names):
    course_var = tk.StringVar()
    course_var.set("")
    course_vars.append(course_var)
    course_checkbox = tk.Checkbutton(root, text=course_name, variable=course_var, onvalue=course_name, offvalue="")
    course_checkbox.grid(row=10 + i, column=1, sticky = W, pady = 2)
    course_checkboxes.append(course_checkbox)

# Nút Đăng ký
register_button = tk.Button(root, text="Đăng ký", command=register)
register_button.grid(row=14, column=0, columnspan=4)

root.mainloop()

import tkinter as tk

self=tk.Tk()
self.title("Form đăng nhập")
self.geometry("600x400")
  
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("Tài khoản là : " + name)
    print("Mật khẩu là : " + password)
     
    name_var.set("")
    passw_var.set("")
     
     
name_label = tk.Label(self, text = 'Tên đăng nhập', font=('calibre',10, 'bold'))
  
name_entry = tk.Entry(self,textvariable = name_var, font=('calibre',10,'normal'))
  
passw_label = tk.Label(self, text = 'Mật khẩu', font = ('calibre',10,'bold'))
  
passw_entry=tk.Entry(self, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
sub_btn=tk.Button(self,text = 'Đăng nhập', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
self.mainloop()
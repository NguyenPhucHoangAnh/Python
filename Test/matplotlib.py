import matplotlib.pyplot as plt

#Biểu đồ cột
def Show_Bieu_Do(namw):
  x = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
  #========================================
  def Xuat_bieu_do_theo_nam(year):
    y = [40, 86, 95, 4, 78, 556,562, 625, 789, 123, 456, 753]
    
    # Vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color='#1C6EEC')
    plt.xlabel('Tháng')
    plt.ylabel('Doanh thu (VND)')
    plt.title(f'Biểu đồ thể hiện doanh thu năm {year}')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Hiển thị biểu đồ
    plt.show()
  Xuat_bieu_do_theo_nam(namw)

#biểu đồ line
def Xuat_bieu_do_theo_nam(year):
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    doanh_thu_sql = [40, 86, 95, 4, 78, 556, 562, 625, 789, 123, 456, 753]

    # Vẽ biểu đồ đường
    plt.figure(figsize=(10, 6))
    plt.plot(thang, doanh_thu_sql, marker='o', color='#1C6EEC', linestyle='-', linewidth=2, markersize=8)
    plt.xlabel('Tháng')
    plt.ylabel('Doanh thu (VND)')
    plt.title(f'Biểu đồ thể hiện doanh thu năm {year}')
    plt.xticks(rotation=45)
    plt.grid(True)  # Hiển thị lưới để dễ theo dõi
    plt.tight_layout()

    # Hiển thị biểu đồ
    plt.show()

#biểu đồ đường tròn
def Xuat_bieu_do_tron_theo_nam(year):
    thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
    doanh_thu_sql = [40, 86, 95, 4, 78, 556, 562, 625, 789, 123, 456, 753]

    # Vẽ biểu đồ hình tròn
    plt.figure(figsize=(8, 8))
    plt.pie(doanh_thu_sql, labels=thang, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Đảm bảo biểu đồ là hình tròn

    plt.title(f'Biểu đồ thể hiện doanh thu năm {year}')

    # Hiển thị biểu đồ
    plt.show()

Xuat_bieu_do_tron_theo_nam("2023")
Xuat_bieu_do_theo_nam("2023")
Show_Bieu_Do("2023")
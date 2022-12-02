# Sử dụng try except để bắt lỗi nếu người dùng nhập sai
try:
    t = int(input("Nhập số dòng: "))
    if (t > 0 and t <= 100) :
        ds_chuoi = []
        for i in range(t):
            chuoi = input(f"Nhập dòng thứ {i + 1}: ")
            ds_chuoi.append(chuoi)
        for i in range(len(ds_chuoi)):
        # hàm split() để tách ds_chuoi[i] thành nhiều chuỗi con được phân tách bởi khoảng trống(dấu cách, dấu tab)
            print(f"Test {i + 1}:\n {len(ds_chuoi[i].split())}")
    else:
        # Thông báo khi người dùng nhập sai số dòng so với điều kiện
        print("Nhập sai! số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100)")
except:
    print("Số dòng nhập không đúng!") #Thông báo lỗi khi nhập sai input
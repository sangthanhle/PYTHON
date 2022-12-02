# Sử dụng try except để bẫy lỗi
try:
    t = int(input("Nhập số dòng: "))
    if (t > 0 and t <= 100) :
        ds_ch = []
        for i in range(t):
            chuoi = input(f"Nhập dòng thứ {i + 1}: ")
            ds_ch.append(chuoi)
        for i in range(len(ds_ch)):
            print(f"\nTest {i + 1}:")
            for j in (ds_ch[i].split()):
            #và dùng hàm split() để tách ds_chuoi[i] thành nhiều chuỗi con được phân tách bởi khoảng trống(dấu cách, dấu tab)
                print(f"{j}", end=" ")
    else:
        # Thông báo khi người dùng nhập sai số dòng so với điều kiện
        print("Nhập sai! số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100)")
except:
    print("Số dòng nhập không đúng!")   #Thông báo lỗi khi nhập sai input
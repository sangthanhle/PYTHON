# Sử dụng try except để bẫy lỗi
try:
    t = int(input("Nhập số dòng: "))
    if t > 0 and t <= 100 :
        ds_ch = []
        for i in range(t):
            chuoi = input(f"Nhập dòng thứ {i + 1}: ")
            ds_ch.append(chuoi)
        for i in range(len(ds_ch)):
            print(f"Test {i + 1}:\n {ds_ch[i].title()}")
            #Htitle()trả về một bản sao của chuỗi trong đó tất cả ký tự đầu tiên của tất cả các từ được chuyển thành chữ hoa.

    else:
        # Thông báo khi người dùng nhập sai số dòng so với điều kiện
        print("Nhập sai! số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100)")
except:
    print("Số dòng bạn nhập không đúng!")   #Thông báo lỗi khi nhập sai input
# Sử dụng try except để bẫy lỗi
try:
    t = int(input("Nhập số dòng muốn nhập: "))
    if(t > 0 and t <= 100):
        for i in range(t):
            Str1 = input(f"Dòng thứ {i + 1}: ")
            Str2 =input(f"Chuỗi con thứ {i+1}: ")
            # sử dụng hàm count() để đếm số lần xuất hiện của chuỗi con
            # in ra kết quả trên 1 dòng dạng Test i: kết quả (Trong đó i là thứ tự bộ test tính từ 1)
            print(f"Test {i+1}: {Str1.count(Str2, 0, len(Str1))}")
    else:
        # thông báo nhập lại số dòng cho đúng yêu cầu
        print("Vui lòng nhập lại số dòng ( số dòng lớn 0 và nhỏ hơn 100)")

except:
    print("nhập sai!\nVui lòng nhập lại số dòng ( số dòng lớn 0 và nhỏ hơn 100)!")
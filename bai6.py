# dùng try except để bẫy lỗi
try:

    t = int(input("Nhập số bộ test: "))

    if(t > 0 and t <= 100):

        for i in range(t):

            Str = input(f"Chuỗi string thứ {i + 1}: ")
            # nhập chuỗi con
            Old = input(f"Chuỗi old thứ {i+1}: ")
            New = input(f"Chuỗi new thứ {i+1}: ")
            # hàm replace(old, new) để thay thế chuỗi old bằng chuỗi new trong string
            print(f"Test {i+1}: {Str.replace(Old, New)}")
    else:
        # thông báo nhập lại số bộ test cho đúng yêu cầu
        print("Vui lòng nhập lại số bộ test ( số bộ test lớn 0 và nhỏ hơn 100)")
# hiển thị ra thông báo khi người dùng nhập sai đầu vào
except:
    print("nhập sai!\nVui lòng nhập lại số bộ test ( số bộ test lớn 0 và nhỏ hơn 100)!")
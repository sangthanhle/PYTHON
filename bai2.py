# Sử dụng try except để bẫy lỗi
try:
    t = int(input("Nhập số dòng: "))
    if t > 0 and t <= 100 :
        ds_ch= []
        for i in range(t):
            chuoi = input(f"Nhập dòng thứ {i + 1}: ")
            ds_ch.append(chuoi)
        for i in range(len(ds_ch)):
            na = 0
            pa = 0
            for j in ds_ch[i]:
            #Điều kiện để đếm các nguyên âm kể cả chữ in hoa trong danh sách đã nhập
                if (j == "a" or j == "e" or j == "i" or j == "o" or j == "u" or
                        j == "A" or j == "E" or j == "I" or j == "O" or j == "U"):
                            na += 1
                elif(j == ' '):
                    continue
                else:
                    pa += 1
            print(f"Test {i + 1}:\n{na}\n{pa}")
    # else:
    #     #Thông báo khi người dùng nhập sai số dòng so với điều kiện
    #     print("Nhập sai! số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100)")
except:
    print("Số dòng nhập không đúng!")   #Thông báo lỗi khi nhập sai input

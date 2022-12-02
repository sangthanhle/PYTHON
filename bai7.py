try:
    t = int(input("Nhập số dòng: "))
    if (t > 0 and t <= 100) :
        ds_ch = []
        for i in range(t):
            chuoi = input(f"Nhập dòng thứ {i + 1}: ")
            ds_ch.append(chuoi)
        for i in range(len(ds_ch)):
            print(f"Test {i + 1}:")
            ds_tulap = []
            for j in (ds_ch[i].split()):
                if j not in ds_tulap:
                    print(f"{j}", end=" ")
                    ds_tulap.append(j)
    else:
        print("Nhập sai! số dòng phải lớn hơn 0 và nhỏ hơn hoặc bằng 100)")
except:
    print("Số dòng bạn nhập không đúng!")

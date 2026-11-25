with open('data/review_raw.txt', 'r', encoding='utf-8') as f:
    line_list_km = []
    i= 0
    for line in f:
        i += 1 
        if line.strip():
           line_list = line.strip().split(',')
        try:   
            line_list_km.append(int(line_list[2]))
        except ValueError:
            print(f"数据有误，跳过第{i}行:{line_list}")
            continue
    print(f"有效车数量：{len(line_list_km)}",f"平均公里数：{sum(line_list_km)/len(line_list_km):.2f}")

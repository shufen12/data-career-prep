with open('data/drive_log.txt', 'r', encoding='UTF-8') as f:  #读取文件
    lines = f.readlines()
clean_line = []
for line in lines:
    if line.strip():  # 判断是否为空行
        if not line.endswith('\n'): #判断是否以换行符结尾
           line = line + '\n'
        clean_line.append(line)
clean_line.insert(2, "08:22 急刹车一次\n")  # 在第3行插入新内容

with open('data/drive_log.txt', 'w',encoding='UTF-8') as f:
    f.writelines(clean_line)  #写入

with open('data/drive_log.txt', 'a', encoding='UTF-8') as f:
    f.write("08:35 车辆熄火\n")  #追加

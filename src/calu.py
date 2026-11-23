numbers = []
with open('data/numbers.txt', 'r', encoding='UTF-8') as f: #读文件
    for line in f: #一行一行的读
        number = int(line.strip())  #去除空格和换行符，并转换为整数
        if number is not None:
            numbers.append(number)  #将数字添加到列表中

avg = sum(numbers) / len(numbers) #计算平均值

with open('out/result.txt', 'w', encoding='UTF-8') as f:  #写文件
    f.write(f"平均值：{avg:.2f}")

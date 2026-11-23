numbers = []
try:  #捕捉文件读取异常
    with open('data/numbers.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            try:  #捕捉 ValueError 异常
                strip = line.strip()
                if strip:
                    numbers.append(float(strip))
            except ValueError:
                print(f"无法将 '{strip}' 转换为数字，已跳过。")
except Exception as e:
    print(f"读取文件时发生错误: {e}")

else:

    try:  #捕捉 ZeroDivisionError 异常

        avg = sum(numbers) / len(numbers)
        max_num = max(numbers)
        min_num = min(numbers)
        sum_num = sum(numbers)
        
    except ZeroDivisionError:

        print("没有有效的数字可供计算。")

    else:

        with open('out/summary.txt', 'w', encoding='UTF-8') as f:
            f.write(f"平均值：{avg:.2f}\n")
            f.write(f"最大值：{max_num}\n")
            f.write(f"最小值：{min_num}\n")
            f.write(f"总和：{sum_num}\n")

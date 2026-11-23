def read_numbers(file_path):
    numbers = []
    try:  #捕捉文件读取异常
        with open(file_path, 'r', encoding='UTF-8') as f:
            for line in f:
                try:  #捕捉 ValueError 异常
                    strip = line.strip()
                    if strip:
                        numbers.append(float(strip))
                except ValueError:
                    print(f"无法将 '{strip}' 转换为数字，已跳过。")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    return numbers

def calc_stats(numbers):
    try:
        avg = sum(numbers) / len(numbers)
        max_num = max(numbers)
        min_num = min(numbers)
        sum_num = sum(numbers)
    except ZeroDivisionError:
        print("没有有效的数字可供计算。")
        return None
    else:
        return {
            "avg": avg,
            "max": max_num,
            "min": min_num,
            "sum": sum_num
        }

if __name__ == "__main__":
    print(read_numbers('data/numbers.txt')) 

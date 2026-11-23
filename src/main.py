from my_tools import read_numbers
numbers = read_numbers('data/numbers.txt')
if numbers:
    print(f"平均值：{sum(numbers) / len(numbers):.2f}")
else:
    print("没有有效的数字可供计算。")

from my_tools import read_numbers, calc_stats
list_numbers = read_numbers('data/numbers.txt')
if list_numbers:
    stats = calc_stats(list_numbers)
    if stats:
        print(f"平均值：{stats['avg']:.2f}")
        print(f"最大值：{stats['max']}")
        print(f"最小值：{stats['min']}")
        print(f"总和：{stats['sum']}")

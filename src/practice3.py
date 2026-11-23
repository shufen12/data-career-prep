big_numbers = []
with open('data/numbers.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()  #读取每行数据
for line in lines:
    strip = line.strip()
    if strip:
        if int(strip) > 50:
            big_numbers.append(int(strip))

with open('out/big_numbers.txt', 'w', encoding='UTF-8') as f:
    for n in big_numbers:
        f.write(f"{n}\n")

    f.write(f"总共有 {len(big_numbers)} 个大于 50 的数字\n")
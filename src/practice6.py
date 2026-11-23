with open("data/numbers.txt", "r", encoding="UTF-8") as f:
    line_no = 0
    valid_nums = []
    bad_rows = []
    for line in f:
        line_no += 1
        stripped = line.strip()
        if not stripped: 
            continue
        try:
            num = float(stripped)
            valid_nums.append(num)
            print(f"第 {line_no} 行的数字是: {num}")

        except ValueError:
            bad_rows.append(f"第 {line_no} 行无法转换：{stripped}\n")
            print(f"第 {line_no} 行无法转换为数字，已跳过。")


with open("out/clean_result.txt", "w", encoding="UTF-8") as out_f:
    for num in valid_nums:  
        out_f.write(f"{num}\n")
    avg = sum(valid_nums) / len(valid_nums) if valid_nums else 0
    out_f.write(f"平均值: {avg:.2f}\n")

if bad_rows:
    with open("out/bad_rows.txt", "w", encoding="UTF-8") as bad_f:
        bad_f.writelines(bad_rows)

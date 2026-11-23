def parse_speeds(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            speeds = []
            bad_rows = []
            line_no = 0
            for line in file:
                line_no += 1
                if line.strip():  # Check if the line is not empty  
                    try:
                        speed = float(line.strip())
                        speeds.append(speed)
                    except ValueError:
                        print(f"第 {line_no} 行: {line.strip()} 是错误值，请检查数据")
                        bad_rows.append(f"第 {line_no} 行: {line.strip()}")
                        continue  # Skip lines that cannot be converted to float
        return speeds, bad_rows
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到，请检查路径")
        return None, None

def analyze_speeds(speeds):
    number_of_valid_entries = 0
    number_of_speeding_incidents = 0
    if speeds:
        for speed in speeds:
            if speed < 0:
                print(f"{speed}速度不能为负数，请检查数据")
                return None
            else:
                if speed >= 0:
                    number_of_valid_entries += 1
                    if speed > 80:
                        number_of_speeding_incidents += 1
                    


        average_speed = sum(speeds) / len(speeds)
        max_speed = max(speeds)
    
        return {
            'average_speed': average_speed,
            'max_speed': max_speed,
            '有效条数': number_of_valid_entries,
            '超速次数': number_of_speeding_incidents
        }
    else:
        print("没有有效的速度数据，请检查数据")
        return None


if __name__ == "__main__":
    file_path = "data/speed_log.txt"  # Replace with your actual file path
    speeds, bad_rows = parse_speeds(file_path)
    analysis_results = analyze_speeds(speeds)
    if analysis_results:
        print("分析结果:")
        print(f"平均速度: {analysis_results['average_speed']:.2f}")
        print(f"最大速度: {analysis_results['max_speed']}")
        print(f"有效条数: {analysis_results['有效条数']}")
        print(f"超速次数: {analysis_results['超速次数']}")
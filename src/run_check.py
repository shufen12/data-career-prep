from log_parser import parse_speeds, analyze_speeds

def run_check(file_path):
    speeds, bad_rows = parse_speeds(file_path)
    if speeds is None:
        return  # Exit if the file was not found or there was an error

    analysis_results = analyze_speeds(speeds)
    if analysis_results:
        with open("out/speed_report.txt", "w", encoding="UTF-8") as out_f:
            out_f.write("分析结果:\n")
            out_f.write(f"平均速度: {analysis_results['average_speed']:.2f}\n")
            out_f.write(f"最大速度: {analysis_results['max_speed']}\n")
            out_f.write(f"有效条数: {analysis_results['有效条数']}\n")
            out_f.write(f"超速次数: {analysis_results['超速次数']}\n")
    else:
        print("分析未能完成，请检查数据。")
    if bad_rows:
        with open("out/speed_errors.txt", "w", encoding="UTF-8") as bad_f:
            bad_f.writelines([f"非正常数据: {row}\n" for row in bad_rows])


run_check("data/speed_log.txt")  # Replace with your actual file path
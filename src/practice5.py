def safe_divide(a_str, b_str):
    try:
        a = float(a_str)
        b = float(b_str)
        result = a / b
    except ValueError:
        print("输入的不是合法数字")
    except ZeroDivisionError:
        print("除数不能为零")
    else:
        return round(result, 2)
    finally:
        print("计算结束")

if __name__ == "__main__":
    # print(safe_divide("10", "2"))
    if safe_divide("10", "0") is not None:
        print(safe_divide("10", "0"))
    # print(safe_divide("abc", "2"))
    # print(safe_divide("15", "4"))
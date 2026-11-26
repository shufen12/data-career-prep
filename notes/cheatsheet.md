# 学习知识速查字典（按需翻阅，日常对话不自动读取）

> **用途**：存放已学过、做项目怕忘的**高频语法、易错参数对比与防坑结论**。
> **使用原则**：平时开新对话**不需要**让 AI 读本文件（省上下文）；只有做题/写项目忘了写法、或每学完一块新知识想追加沉淀时，才按需翻阅或追加。

---

## 1. Python 文件操作与工程基础（Day 1–Day 2）

- **文件读写模板**：
  ```python
  with open('data/xxx.txt', 'r', encoding='utf-8') as f:
      lines = f.readlines()
  ```
  - 模式：`'r'` 读、`'w'` 覆盖写、`'a'` 末尾追加。
- **字符串不可变性**：`line.strip()` 不会改动原 `line`，且**必须带括号 `()`**；清洗切分写 `line.strip().split(',')`（`if line.strip():` 仅用于判断空行）。
- **异常兜底与模块隔离**：
  - `try ... except ValueError ... else ... finally` 精确捕获脏数据行或除零 `ZeroDivisionError`。
  - 工具文件底部加 `if __name__ == "__main__":`，避免被 `import` 时自动运行自测代码。
- **命名避坑**：绝不用 `list`、`sum`、`str`、`strip` 当变量名，也少用 `a`/`b` 等无意义变量名。

---

## 2. Linux 命令行 & Git 备查（Day 3–Day 4）

- **高频看文件与操作命令**：
  - 位置与目录：`pwd`（当前目录）、`ls -la`（看全部文件含隐藏文件）、`mkdir 目录`、`cd 目录`、`cd ..`（退回上一级）
  - 读写与查内容：`touch 文件`、`echo "内容" > 文件`（覆盖）/ `>>`（追加）、`cat`（看全文）、`head -n 5`（前 5 行）、`tail`（末尾）、`grep "词" 文件`（搜关键词）
  - 复制/改名/删除：`cp 原 新`（复制）、`mv 原 新`（移动或改名）、`rm -r 目录`（删目录）
- **相对路径铁律**：Python 按**终端当前工作目录**找文件；在 `src/` 下开的 `.ipynb` 读上级 `data/` 须写 `../data/xxx.csv`。
- **Git 维修与忽略**（日常提交可用 VS Code 图形界面）：
  - 查绑定与改绑定：`git remote -v`、`git remote set-url origin 新地址`
  - `.gitignore` 常见忽略：`__pycache__/`、`*.pyc`、`out/`

---

## 3. Pandas 核心写法与高频防坑（Day 6–Day 8）

### 3.1 `pd.read_csv` 参数规则
| 场景 | 正确写法 | 常见踩坑 |
|---|---|---|
| 原文件**没有表头**，自己起列名 | `pd.read_csv(path, header=None, names=['a', 'b'])` | 误写 `header=0` 会静默吞掉第 1 行真数据 |
| 原文件**有旧表头**，想替换列名 | `pd.read_csv(path, header=0, names=['a', 'b'])` | 漏写 `header=0` 会把老表头当第 0 行数据 |
| Tab 分隔文本 | 加 `sep='\t'` | 默认按逗号 `,` 切 |

### 3.2 取列、二维切片与布尔筛选
- **取单列 vs 多列**：`df['col']` 返回 `Series`；`df[['col1', 'col2']]` 返回 `DataFrame`。
- **二维切片固定结构 `[管行 , 管列]`**：
  - `df.loc[1:3, ['brand', 'city']]`：按**标签名**，切片**两边全闭**（含 `3`）。
  - `df.iloc[1:4, [0, 4]]`：按**0 起始整数位置**，切片**左闭右开**（不含 `4`），只认数字不认列名。
  - 单格取值：`df.at[行名, 列名]` / `df.iat[行号, 列号]`。
- **多条件筛选**：使用 **`&`（且）、`|`（或）、`~`（取反）**，每个条件各自用 `(...)` 括起来；多值匹配用 `df['city'].isin(['上海', '深圳'])`。

### 3.3 缺失值 `NaN` 与常用清洗/统计
- **判空照妖镜**：禁止用 `!= None` / `== None` 比较 `NaN`，必须用 `.notna()` 或 `~列.isna()`；统计每列缺失用 `df.isna().sum()`（默认 `axis=0`）。
- **排序与 Top N**：
  - 多列混合升降序：`df.sort_values(by=['price_wan', 'mileage_km'], ascending=[False, True])`（方法名是 `sort_values`，不是 `sort_index`）。
  - 取前几名：`df.nlargest(3, columns=['price_wan'])`。
- **改表与去重（默认不改原表，必须用变量接住）**：
  - 删列 / 改名：`df.drop(columns=['city'])`、`df.rename(columns={'旧': '新'})`
  - 重置乱序行号：`df = df.reset_index(drop=True)`（不加 `drop=True` 会多出旧 `index` 列）
  - 去重与计数：`df['city'].drop_duplicates()`（返回 `Series`）vs `df.drop_duplicates(subset=['city'])`（返回完整行 `DataFrame`）；单个列去重计数 `df['brand'].nunique()`。
  - 链式计算保留小数：`(df['a'] / df['b']).round(2)`（外层必须加括号）。
- **数据分析防误判**：看 `describe()` 时不能只凭 `mean` 与 `50%` 接近就断定“数据平稳”，必须结合 `min`、`max`、`std` 判断真实离散度。

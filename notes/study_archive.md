# 历史学习打卡日志归档（冷数据）

> **说明**：为控制 [AI学习进度与跨会话交接.md](../AI学习进度与跨会话交接.md) 的上下文体积，超过 3 天的历史打卡日志按时间归档至此。**日常新开对话默认不读取本文件**，仅在需要回溯早期阶段细节时查阅。

---

### Day 0（2026-11-21｜规划定稿日）
- **已完成**：完成真实知识框架摸底；避让 11 月底考试、12/15 开题、春节与 2–5 月毕设；在 `C:\Users\ShuFen\学习初级数据` 搭建完成终版规划书、工作区自动规则与跨会话进度追踪系统。
- **下一步（Day 1）**：在 `C:\Users\ShuFen\学习初级数据` 下建 `src/`、`data/`、`out/`，攻克 Python 文件读写（`with open`）与 `pip install pandas matplotlib`。

### Day 1（2026-11-22｜阶段一）
- **今日学习内容**：大白话理解 `with open` 与 `pip`；看完黑马程序员《8天Python从入门到精通》第 8 章（文件操作）；搞懂"为何文件不能直接中间插队，任意位置插入需先 `readlines()` 读入列表 `insert` 再 `'w'` 写回"；完成 `pip install pandas matplotlib`。
- **实操产出**：
  - 建立目录 `data/`、`out/`、`src/` 与测试数据 `C:\Users\ShuFen\学习初级数据\data\numbers.txt`（7 个整数）、`data\drive_log.txt`（5 行日志）；
  - 亲手写出并跑通 `C:\Users\ShuFen\学习初级数据\src\calu.py`，生成 `C:\Users\ShuFen\学习初级数据\out\result.txt`（`平均值：12412.71`）；
  - 额外完成 3 道巩固练习：`src\practice1.py`（→ `out\summary.txt`）、`src\practice2.py`（中间插入+空行过滤+末尾补 `\n` 保护）、`src\practice3.py`（→ `out\big_numbers.txt`，过滤大于 50 的数并统计）；
  - 终端成功安装并导入验证 `pandas 3.1.1`、`matplotlib 3.11.2`（Python 3.13 环境）。
- **抽查与掌握度**：
  - 已掌握：`with open` 读写文件流程、`'w'` 覆盖与 `'a'` 追加区别、逐行 `.strip()` 清洗与 `int()` 转类型后用 `sum(numbers) / len(numbers)` 计算均值（收尾 2 道小测全对）。
  - 新暴露薄弱点：开局 `sum(a, b, c)` 传参误区；PowerShell 终端误输入 `exit()`；`calu.py` 缩进位置与空文件/小数容错待优化。
- **明日精确第一步**：开局抽查 Day 1 错题本 2 题 → 顺手精简 `src/calu.py`（把 `avg` 移出 `with` 块）→ 学黑马 Python 第 9 章（异常、模块与包），给 `calu.py` 加上异常兜底以冲刺完成 M1。

### Day 2（2026-11-22｜阶段一｜M1 通关）
- **今日学习内容**：看完黑马 Python 第 9 章（异常捕获 `try/except/else`、模块与包 `import`、`if __name__ == "__main__":`）。
- **实操产出**：
  - 升级 `C:\Users\ShuFen\学习初级数据\src\practice1.py`：用双层 `try/except/else` 兼容脏数据行（`ValueError`）、文件缺失（`Exception`）与空文件除零（`ZeroDivisionError`），验证 `'data/ABC.txt'` 与 `'data/numbers.txt'`（含 `abs` 与空行）均不崩溃，输出 `out\summary.txt`；
  - 拆分模块化工程：`C:\Users\ShuFen\学习初级数据\src\my_tools.py`（封装 `read_numbers(file_path)` 返回数字列表与 `calc_stats(numbers)` 返回统计字典 + 底部 `__main__` 自测）与 `C:\Users\ShuFen\学习初级数据\src\main.py`（导入并计算均值 `12412.71`，屏蔽模块测试输出）；
  - 额外完成 Day 2 巩固练习：`src\practice4.py`（多函数导入统计）、`src\practice5.py`（`safe_divide` 练 `ValueError`/`ZeroDivisionError`/`else`/`finally`）、`src\practice6.py`（脏数据行号记录 → `out\clean_result.txt` + `out\bad_rows.txt`）。
- **抽查与掌握度**：
  - 已掌握：`try/except/else` 执行时机、`if __name__ == "__main__":` 原理（收尾 2 题全对）；Day 1 错题本两项抽查通过（1/2）。
  - 新暴露薄弱点：写 `main.py` 时曾用 `list` 做变量名撞车内置函数，以及三元表达式配合 `:.2f` 对 `None` 格式化的坑（已现场改通）。
- **下一步精确起点**：进入 **M2（GeekHour 30 分钟 Linux 命令行 + 安装 Git + 盲敲 10 条命令）**。

### Day 3（2026-11-22｜阶段一｜M2 通关）
- **今日学习内容**：理解 Linux 命令行与工作目录/相对路径概念（`.`、`..`、`~`）；了解 Git Bash 与真 Linux 服务器的 80% 重合与 20% 差异；学习 GeekHour《30分钟Linux入门教程》及常见看日志命令（`head` / `tail` / `grep`）。
- **实操产出**：
  - 确认本机已安装 Git 2.54.0（`C:\Users\Git\cmd\git.exe`），并在 VS Code 成功切出 `Git Bash`（`$`）；
  - 在 `Git Bash` 完成 3 关全量实操：安全沙盒 `test_cli` 内跑通 `pwd / ls -la / mkdir / cd / touch / echo > / cat / cp / mv / rm -r / clear` 并清理干净；亲手复现并理解 `cd src` 后 `python main.py` 找不到 `data/numbers.txt` 的相对路径原理；实测 `head`、`tail`、`grep`。
- **抽查与掌握度**：
  - 已掌握：10 条核心命令行主干动作、相对路径与工作目录关系、`sum()` 命名避坑（第 2 次复核通过，已从错题本毕业）。
  - 暴露薄弱点：`>>>` 退出仍误答为 `exit`（重置待连续 2 天通过）；盲敲测试时曾出现 `echo` 方向写反、`echp"done"` 少空格与拼写错、`head - n` 多空格、漏 `.txt` 后缀及 `data/` 前缀（已现场纠偏）。
- **明日精确第一步**：进入 **M3（GeekHour 一小时 Git `BV1HM411377j` + 注册 GitHub + 完成 3 次 `commit` 并 `push`）**，并在开局先执行「Linux 高频命令 5 轮间隔强化计划」第 2 轮（+1 天）闭卷抽查。

### Day 4（2026-11-23｜阶段一｜M3 通关）
- **今日学习内容**：通过间隔记忆第 2 轮（+1 天）抽查；学习 Git 与 GitHub 核心概念与 `.gitignore` 忽略机制；看完 GeekHour《一小时Git教程》（`BV1HM411377j`）。
- **实操产出**：
  - 重新配置本地全局 Git 署名并对齐 GitHub 绑定邮箱（`lvjunhan` / `2983136618@qq.com`）与中文路径显示（`core.quotepath false`）；
  - 新建 `C:\Users\ShuFen\学习初级数据\.gitignore`（成功忽略 `__pycache__/`、`*.pyc`、`out/`）；
  - 本地完成 `git init` 及分模块 `commit`，修正远程仓库地址（`git remote set-url`）后 `push` 至 GitHub 公开仓库 `https://github.com/shufen12/data-career-prep`；
  - 掌握 VS Code 源代码管理图形界面（新增 `README.md` 并推云端），并独立完成 **M1–M3 三合一无提示综合检验《车速日志质检小工具》**：命令行造 `data/speed_log.txt`、`src/log_parser.py`、`src/run_check.py` → `out/speed_report.txt` + `out/speed_errors.txt`，提交 `5dc319e` 已同步 `origin/main`。
- **抽查与掌握度**：
  - 已掌握：Git 三区流转与 `add` / `commit` / `push` 区别、`.gitignore` 忽略机制（收尾 2 题全对）；间隔记忆第 2 轮完成（`echo` 方向、`-n 3`、`data/` 全对；仅遗留 `>` 覆盖 vs `>>` 追加区分，留 11-25 第 3 轮追查）；`>>>` 用 `exit()` 通过 1/2；独立跑通 Python 异常+模块化+命令行+Git 推送闭环（曾遇 `mkdir` 建文件误区与 `speed <= 0` 提前 `return` 误区，均已改通）。
- **明日精确第一步**：启动 **M4（市场校准日）**：调研 20 份上海/深圳真实 JD（10 份智驾/车企数据岗 + 10 份通用数据分析岗），汇总高频技能词；同时在 11-25 开局执行 Linux 命令行第 3 轮间隔抽查。

### Day 5（2026-11-24｜阶段一｜M4 通关）
- **今日学习内容**：通过 BOSS 直聘与牛客网一线检索完成真实招聘市场校准；学会甄别并排除"AI 算法岗、硬件射频测试、机械臂采集操作员、爬虫开发"4 类伪对口坑位，理清「数据可视化」在岗位中的真实考查方式。
- **实操产出**：
  - 整理并去重 11 份高质量真实 JD（A 组车企/智驾/车辆运营 4 份 + B 组通用/制造业/AI 数据运营 7 份）存入 `C:\Users\ShuFen\学习初级数据\notes\jd_research.md`；
  - 完成真实词频统计与校准结论：Python（82%）、SQL（73%）、BI 看板（45%）、AI 提效（36%）、Excel 透视/函数（27%，集中在 8–15K 入门岗），决定投递前预留 2 天补齐 Excel 透视/`XLOOKUP` + BI 看板。
- **抽查与掌握度**：
  - 已掌握：`>>>` 敲 `exit()` 与 `$` 敲 `exit` 连续 2 天通过（已从错题本毕业）；`>` 覆盖与 `>>` 追加区分答对。
  - 待复核：`git remote set-url origin 新地址` 曾遗忘，留下一轮抽查；11-25 起触发 Linux 高频命令第 3 轮（+3 天）场景串联闭卷测试。
- **明日精确第一步**：开局抽查 `git remote set-url`（若已到 `2026-11-25` 同步执行 Linux 第 3 轮场景闭卷测试）→ 3 句大白话理解 Pandas DataFrame/Series → 开启 **M5（蚂蚁学Python《Pandas数据分析从入门到实战》P1–P3）**。

### Day 6（2026-11-24｜阶段一｜M5 起步与课程校准）
- **今日学习内容**：
  - 3 句大白话吃透 `DataFrame`、`Series` 与 `Jupyter Notebook` 定位，核实 VS Code Python 解释器路径（`Python315\python.exe` 已装 `pandas 3.1.1`、`ipykernel 7.4.0`）；
  - 看完原定蚂蚁学Python P1–P3 后因节奏跳跃、缺过渡与环境割裂，经 `/grill-me` 拆解将 M5 主教程统一切换为 **尚硅谷《Python数据分析》第 022–052 集（Pandas）+ 第 053–060 集（Matplotlib）**（跳过 001–021 装软件与 NumPy，遇零星 `np.` 现查），并改用 VS Code 安装 `Jupyter` 插件跟练。
- **实操产出**：
  - 独立编写并跑通 `C:\Users\ShuFen\学习初级数据\src\day6_pandas_intro.py`：
    - 读入 `data/cars_sample.csv` 并识别 `mileage_km` 缺失值（`7 non-null`）；
    - 修正 `read_csv` 与 `to_csv` 混淆，用 `sep='\t', header=None, names=[...]` 读入无表头 `data/sensor_log.txt`；
    - 验证单列 `Series`（均价 `18.97`）与双列列表包裹 `df[['price_wan', 'brand']]` 返回 `DataFrame` 的差异。
  - 在 VS Code 安装微软官方 `Jupyter` 插件，并新建 `src/test_nb.ipynb` 结合 `os.getcwd()` 自行修正相对路径 `../data/cars_sample.csv` 成功渲染出交互表格。
  - 已同步更新 `转行AI数据岗-零基础重构规划书.md` 与交接单中的 M5 课程方案。
- **抽查与掌握度**：
  - 已掌握：避免变量名覆盖内置名（`str` 避坑原理 Day 6 答对）；`read_csv` 参数分工、`df[[]]` 双层方括号原理与 `.ipynb` 相对路径定位。
  - 待复核：`git remote set-url origin 新地址` 连续两次未写出（已附常用 Git 速查表，Day 7 继续巩固）；11-25 触发 Linux 高频命令第 3 轮（+3 天）场景串联闭卷考。
- **明日精确第一步**：开局执行 **Linux 第 3 轮（11-25）场景串联闭卷测试** + 复核 `git remote set-url` → 直接开看 **尚硅谷《Python数据分析》第 022–027 集（Pandas 概述与 Series）**（VS Code Jupyter 环境已就绪）。

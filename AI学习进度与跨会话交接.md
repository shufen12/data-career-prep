# AI 数据岗学习进度与跨会话交接单

> **文件用途**：本文件是跨会话连续学习的**唯一进度事实源**。每次学习结束时由 AI 更新；以后新开任何对话，AI 读取本文件即可无缝接上之前所有天的学习内容、薄弱点和代码路径。
> **学习主目录**：`C:\Users\ShuFen\学习初级数据`
> **配套总规划书**：`C:\Users\ShuFen\学习初级数据\转行AI数据岗-零基础重构规划书.md`
> **最后更新时间**：2026-11-26

---

## 0. 给新会话 AI 的接手协议（严格遵守）

1. **不要重新论证要不要转行、不要重写规划书、不要推荐付费班或英文大部头文档。** 方案已定稿。
2. **开局先做 2 分钟旧知复核**：根据下方「每日学习打卡日志」中最近 1–2 天学过的内容与「4. 遗留薄弱点 / 错题本」（**含其中的「Linux 高频命令 5 轮间隔强化表」**，按当前日期自动触发对应轮次抽查），先出 **2 道简短口头/代码/命令行抽查题** 确认用户真的记住了，再进入当天新任务。
3. **坚持小白大白话带练法**：每个新概念先用 3 句大白话讲清"它是干嘛的"，绝不直接塞一大段代码让用户无脑复制。
4. **阶梯式阻力排错协议（2026-11-23 确立，防止 AI 拐杖依赖）**：
   - **第一轮检查/排错**：用户发代码请求检查或问为何报错时，**默认先不直接点破具体出错行号与改法**，而是先指明**出问题的方向/函数**，并引导用户用 `print(...)` 调试或核对终端报错关键词自己定位（除非只是纯命令行操作失误或环境配置阻塞）。
   - **第二轮点破**：只有当用户自己动手排查一轮仍未找到（或明确要求"直接告诉我具体哪行错"）时，再点破具体行号与底层原因，仍由用户亲手改通。
5. **三类分级出题协议（2026-11-26 `/grill-me` 确立）**：
   - **触发节奏（负荷分级）**：12/15 低负载期每日新课后**只出第 1 + 第 2 类（总计控制在 25 分钟内）**；**第 3 类**仅在章节收官、周末或 12/16 进入每日 5h 整块期后触发。
   - **第 1 类（5–8 分钟｜闭卷微变形防坑小测）**：不照搬视频原例，换表/改边界条件或埋 1 个易错坑要求不看笔记手敲排雷（次日开局继续保留 2 分钟旧知复核）。
   - **第 2 类（15–20 分钟｜当堂知识应用题）**：用本轮刚学核心知识点独立完成 1 道贴近业务/车辆数据场景的实操题。
   - **第 3 类（25–30 分钟｜真实工作流综合题）**：仅串联现实工程中真实上下游配合的旧技能（如命令行探查 → Pandas 清洗统计 → 函数封装/异常兜底 → Git 推仓），不强行拼盘已被替代的原生语法。
   - **超时止损**：单处卡壳超 10–15 分钟或整题超时，立刻贴代码与报错走第 4 条"阶梯式阻力排错"，绝不硬耗挤压主线进度。
6. **结束时强制写回**：当天学习告一段落或用户说"打卡/更新进度/今天先到这里"时，**必须立即编辑本文件**，把当天日期、学完的视频/知识点、写完的代码路径、新暴露的薄弱点以及下一天精确第一步写入下方日志，并勾选对应里程碑。

---

## 1. 学习者真实基线卡（勿再重复摸底）

- **背景**：桂林航天工业学院（二本）车辆工程 2027 届本科生，不考研，**毕业前确认 100% 无法实习**，目标上海 / 深圳 8k+ 数据/智驾评测岗（双线并行：车企智驾数据评测 + 通用/车企数据分析）。
- **起点**：已装好 Python + VS Code 并跑通过代码；Python 语法半熟但无工程经验（不懂 `pip`/第三方库/文件读写）；没用过 Excel 透视、没敲过命令行、零 SQL 基础；**车辆专业课基本还给老师，项目绝不依赖深奥车辆动力学或 MATLAB**；英语弱（高中三四十分），但**有稳定科学上网环境**（可顺畅打开 GitHub）。
- **学业冲突已排清**：11 月底 1 门考试 + 12/15 前论文开题报告（期间每日自学降载至 2–3h）→ 12/16–02/04 整块 5h/天 → 02/05–02/13 春节只刷 SQL → 2 月居家低强度毕设并行 → 3–5 月高强度毕设 + 春招。
- **风格要求**：客观严谨、直击本质、禁止鸡汤美化，严格使用规划书第三节指定的免费中文资料。

---

## 2. 当前进度仪表盘

| 项 | 当前状态 |
|---|---|
| **当前所在阶段** | 阶段一：低负载打底期（11/22 – 12/15） |
| **累计已完成学习天数** | **8 天**（已完成 Day 1–Day 8，M1–M4 已通关，M5 已学完 `Series` 全章 + `DataFrame` 核心 034–042 集） |
| **下一次对话的精确起点** | **Day 9｜M5（尚硅谷 DataFrame 进阶与清洗）**：开局 2 分钟抽查 `header=None` 配合、`NaN` 判空（`~isna`/`notna`）、`reset_index(drop=True)` 与 `describe()` 离散度逻辑 → 3 句大白话前置建模 → 开看 **尚硅谷《Python数据分析》第 043 集起（至 052 集收尾后触发第 3 类真实工作流综合题）** |
| **本地学习主目录** | `C:\Users\ShuFen\学习初级数据`（已建好） |
| **GitHub 仓库 URL** | `https://github.com/shufen12/data-career-prep` |
| **已累计刷 SQL 题数** | 0 题 |

---

## 3. 全程里程碑勾选清单

### 阶段一：低负载打底期（11/22 – 12/15，每日 2–3h）
- [x] **M1（11/22–11/30）**：黑马 Python 第 8 章（文件操作）+ 第 9 章（异常/模块/包/pip），跑通 `pip install pandas matplotlib`
- [x] **M2（11/22–11/30）**：GeekHour 30 分钟 Linux 命令行 + 安装 Git，盲敲 10 条常用命令
- [x] **M3（11/22–11/30）**：GeekHour 一小时 Git（`BV1HM411377j`）+ 注册 GitHub + 首次 `push` 3 次提交
- [x] **M4（12/01–12/02｜11-24 提前完成）**：调研 11 份去重真实 JD（A 组 4 份 + B 组 7 份），完成高频技能词统计与市场校准
- [ ] **M5（12/03–12/15）**：尚硅谷《Python数据分析》Pandas（022–052 集）+ Matplotlib（053–060 集），完成汽车数据清洗脚本 + 3 张高清图推 GitHub

### 阶段二：整块加速期（12/16 – 12/31，每日 5h）
- [ ] **M6（12/16–12/23）**：通关 SQL 之母（`sqlmother.yupi.icu`）+ 戴师兄 SQL（含 `JOIN` 与窗口函数）+ Python `sqlite3` 重写查询
- [ ] **M7（12/24–12/31）**：启动每日 45 分钟 SQL 刷题 + 封板**副项目《汽车市场多维数据清洗与 SQL 诊断报告》** + 简历 v0.5 BOSS 测回复率

### 阶段三：王牌项目攻坚期（01/01 – 02/04，每日 5h）
- [ ] **M8（01/01–01/07）**：吃透 nuScenes 5 张表结构，装通 `nuscenes-devkit` + 下载 `v1.0-mini`，导出 400+ 帧基础表
- [ ] **M9（01/08–01/14）**：完成车速/加速度运动学特征提取 + 周边目标统计 + 数据质检模块
- [ ] **M10（01/15–01/21）**：完成 Corner Case 场景挖掘规则 + SQLite 3 张表入库 + 5 条业务查询 SQL
- [ ] **M11（01/22–01/28，裁剪检查点）**：懒人老刘 Streamlit 教程 + 完成 3 板块交互网页与 `render_sample_data` 真图回放联动
- [ ] **M12（01/29–02/04，除夕前硬封板）**：工程整理推 GitHub + 公网部署 + **60–90 秒国内直看录屏** + 两版简历 v1.0 初稿

### 阶段四 & 五：春节缓冲与春招实战（02/05 – 05/31）
- [ ] **M13（02/05–02/13）**：春节 9 天每天坚持 45 分钟 SQL 保手感
- [ ] **M14（02/14–02/21）**：两版简历精修 + 20 道项目追问 + 2 轮全真模拟面试
- [ ] **M15（02/22–02/28）**：春招第一波抢跑投递 ≥ 25 家
- [ ] **M16（03/01–05/31）**：毕设稳过并行 + 累计有效投递 80–150 家拿 Offer

---

## 4. 遗留薄弱点 / 错题本（新会话开局必抽查）

1. **命令行细节（Day 3 暴露 → Day 4/5 改观 → 11-25 第 3 轮暴露命令词记忆衰减）**：`>` 与 `>>` 区分、`-n 1` 不加空格、`cd ..`、`rm -r` 均实操跑通；但无提示下曾遗忘 `echo`、`head`、`grep`，且把"复制"误用成 `clone` / `mv`（正确应为 `cp`），留待 **11-29 第 4 轮**重点追查 `echo`、`cp` vs `mv`、`head`、`grep`。
2. **变量命名规范 & Git GUI/CLI 边界（常规提醒）**：不要用 `list`、`sum`、`str`、`strip` 当变量名，也少用 `a`/`b` 等无意义临时变量名；日常提交可用 VS Code 图形界面，`git remote set-url origin 新地址` / `git remote -v` 归入“懂原理+备查维修命令”（Day 8 已重讲原理并手敲通过）。
3. **`pd.read_csv` 的 `header=` 与 `names=` 配合（Day 7 加入 → Day 8 仍出错，重置进度）**：Day 8 开局曾误答为 `head=0, name=[...]`（参数拼写错 + 误用 `header=0` 会静默删掉第 1 行真数据），经纠偏后重答对。无表头必须写 `header=None, names=[...]`；仅原文件有旧表头想改名时才用 `header=0, names=[...]`。Day 9 开局再抽查 1 次。
4. **Python 字符串不可变性与方法调用括号（Day 7 暴露 → Day 8 原理已过关）**：`if line.strip():` 不会原地剥掉 `\n`，且 `strip()` 是方法必须带括号（Day 8 曾漏括号写成 `line.strip.split(',')`，已当场改对），Day 9 再顺带复核 1 次即毕业。
5. **DataFrame 核心高频坑点（Day 8 新暴露）**：
   - **二维切片与 `NaN` 过滤**：`iloc[行, 列]` 只认从 `0` 开始的整数位置（曾错写成 `[1,2,4]` 漏掉第 0 列，已自查改为 `[0,2,4]`）；判断缺失/非空绝不能用 `!= None`（会放行 `NaN`），必须用 `.notna()` 或 `~列.isna()`。
   - **方法拼写、返回值接住与统计视角**：注意拼写 `sort_values()`（非 `sort_vlaue`）与 `DataFrame`（非 `datafream`）；`reset_index(drop=True)` 默认不改原表需重新赋值接住；看 `describe()` 时不能只因 `mean` 与 `50%` 接近就断定“无大起大落”，必须结合 `min`/`max`/`std` 判断离散度。

### 专项记忆追踪：Linux 高频命令 5 轮间隔强化计划（基于间隔重复 + 主动回忆）

> **执行协议**：每次开新会话时，AI 对照当前日期与下表；若已到某轮目标日期且状态为 `待完成`，在开局 2 分钟内执行该轮闭卷测试，通过后更新状态与实际通过日期；**未通过的命令单独标出，下一天继续追查**。

| 轮次 | 建议日期 | 间隔 | 考核方式（每次 2–3 分钟，严禁看表） | 重点覆盖范围 | 状态 & 记忆记录 |
|---|---|---|---|---|---|
| **第 1 轮** | 2026-11-22（Day 3） | 第 0 天 | `Git Bash` 3 关实操 + 10 题盲写验收 | `pwd / ls -la / mkdir / cd / touch / echo > >> / cat / cp / mv / rm -r / head / tail / grep` | `[x]` **已完成**（主干全通；暴露 `echo` 方向/空格、`-n` 空格、后缀、`data/` 前缀 4 处细节） |
| **第 2 轮** | 2026-11-23（+1 天） | +1 天 | 聊天框**闭卷盲写 5–6 条**：主攻第 1 轮暴露细节 + 随机抽 5 条 | 必考 `echo "内容" >> 文件`、`head -n` 相对路径、`mv` 改名、`rm -r` | `[x]` **2026-11-23 已完成**（`echo` 方向、`-n 3`、`data/` 全对；仅追加误用 `>` 而非 `>>`、手误多打 `txtx`，第 3 轮重点追查 `>>`） |
| **第 3 轮** | 2026-11-25（+3 天） | +3 天 | **场景串联闭卷**：只给中文需求，一口气写出 6–8 行连贯操作 | 建目录 → 写/追加文件 → 复制改名 → `grep`/`head` 查内容 → 退出删目录 | `[x]` **2026-11-25 已完成**（`mkdir`/`cd`/`>` vs `>>`/`-n 1`/`rm -r` 均跑通；曾忘 `echo`/`head`/`grep`，且"复制"误用 `clone`/`mv` 而非 `cp`，列为第 4 轮必考） |
| **第 4 轮** | 2026-11-29（+7 天） | +7 天 | **终端实操混考**：在 `Git Bash` 无提示真敲，混搭 `python` 与 `git` | 切进子目录再退回、用命令行跑脚本、用 `cat/head` 验证输出 | `[ ]` 待执行 |
| **第 5 轮** | 2026-12-06（+14 天） | +14 天 | **真实数据实战（毕业考）**：在 Pandas 阶段直接用命令行看汽车 CSV | 零提示用 `ls -la`、`head -n 5`、`tail`、`grep`、`pwd`、`cd` 探查真实数据 | `[ ]` 待执行（连续零失误则正式毕业） |

---

## 5. 每日学习打卡日志（持续追加）

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
  - 已同步更新 `转行AI数据岗-零基础重构规划书.md` 与本交接单中的 M5 课程方案。
- **抽查与掌握度**：
  - 已掌握：避免变量名覆盖内置名（`str` 避坑原理 Day 6 答对）；`read_csv` 参数分工、`df[[]]` 双层方括号原理与 `.ipynb` 相对路径定位。
  - 待复核：`git remote set-url origin 新地址` 连续两次未写出（已附常用 Git 速查表，Day 7 继续巩固）；11-25 触发 Linux 高频命令第 3 轮（+3 天）场景串联闭卷考。
- **明日精确第一步**：开局执行 **Linux 第 3 轮（11-25）场景串联闭卷测试** + 复核 `git remote set-url` → 直接开看 **尚硅谷《Python数据分析》第 022–027 集（Pandas 概述与 Series）**（VS Code Jupyter 环境已就绪）。

### Day 7（2026-11-25｜阶段一｜M5 `Series` 全章通关 + 1小时综合巩固）
- **今日学习内容**：
  - 彻底弄懂 `pd.read_csv` 中 `sep='\t'`、`header=None` vs `header=0` 与 `names=[...]` 潜规则，并在实测中验证了误用 `header=0` 静默丢第 1 行数据的风险；
  - 完成 **尚硅谷《Python数据分析》第 022–033 集**（`Series` 全部核心知识：自定义索引 `index`、`loc`/`iloc`/`at`/`iat` 切片左闭右开差异、常用统计/排序/去重方法、`np.random.seed`/`randint`、滑动窗口 `rolling`、重采样 `resample` 及 5 个业务案例）。
- **实操产出**：
  - 完成 **Linux 高频命令第 3 轮（11-25）场景串联闭卷考**（在 VS Code Git Bash 实操建目录、写/追加、查内容、删目录全跑通）；
  - 编写并跑通 `C:\Users\ShuFen\学习初级数据\src\day7_series.ipynb`（含全部 `Series` 笔记、5 个视频案例、自主完成电动车续航 `range_km` 筛选降序、`loc` vs `iloc` 对比验证）；
  - 完成 **Day 1–Day 7 一小时三关综合巩固**：
    - 第 1 关：Git Bash 造出 `C:\Users\ShuFen\学习初级数据\data\review_raw.txt`（含故意脏数据）并实操 `cp` / `head -n 2` / `grep` / `mv` / `rm`；
    - 第 2 关：编写并跑通 `C:\Users\ShuFen\学习初级数据\src\review_day7.py`（`with open` + `try/except ValueError` 跳过第 3 行脏数据 `bad_km`，算出 3 辆有效车平均里程 `20666.67`）；
    - 第 3 关：在 `src\day7_series.ipynb` 串联读入 `../data/review_raw.txt`（`header=None` 保住 `BYD`）、品牌索引 `Series` 筛选排序（`Tesla 23.19`、`Geely 14.77`）与 `rolling(2).sum() == 2` 车速滑动窗口（`['f3', 'f6']`）；
  - 完成 `git remote -v` 核验并提交推送至 GitHub `origin/main`（commit `Day7: 复习并跑通Series案例与...`）。
- **抽查与掌握度**：
  - 已掌握：`git remote set-url` 答对（1/2）；`header=None` vs `header=0` 答对（1/2）；`loc`（全闭）vs `iloc`（左闭右开）原理、`rolling(2).sum() == 2`、双层 `Series` 条件筛选 `&` 与 `ascending=False` 降序。
  - 新暴露/待复核：
    1. Linux 第 3 轮暴露 `echo`、`head`、`grep` 一度遗忘及“复制”误用 `clone`/`mv` 而非 `cp`，留待 **11-29 第 4 轮**必考；
    2. 复习写 `review_day7.py` 时曾把空列表 `[]` 错放进 `for` 循环内（已现场自行定位修好），并暴露 `if line.strip():` 不会原地剥掉 `line` 末尾 `\n` 的误区（已用 `line.strip().split(',')` 改通）；
    3. `day7_series.ipynb` 复习中曾把 `read_csv` 误写成 `read_txt`、`names` 少 `s`、以及混淆 `index=` 与 `name=`，经引导均已当场独立改通。
- **明日精确第一步**：开局 2 分钟抽查 **`header=`/`names=` 配合** + **`git remote set-url` 终检** + **`.strip()` 返回值原理** → 3 句大白话吃透 `DataFrame` 行列结构与索引 → 开看 **尚硅谷《Python数据分析》第 034–038 集（`DataFrame` 创建、属性与索引操作）**。

### Day 8（2026-11-26｜阶段一｜M5 `DataFrame` 核心 034–042 + 方法论沉淀）
- **今日学习内容**：
  - 复盘并修正 `header=None, names=[...]`、`line.strip().split(',')` 及 `git remote set-url` 原理（明确日常提交可用 VS Code 图形界面，低频维修命令懂原理备查即可）；
  - 完成 **尚硅谷《Python数据分析》第 034–042 集**（`DataFrame` 4 种创建方式、常用属性 `shape`/`columns`/`dtypes`/`T`、`loc`/`iloc`/`at`/`iat` 二维行列切片、多条件 `&`/`~` 布尔筛选、`isin`/`isna`/`notna`/`sort_values`/`nlargest`/`describe`/`drop`/`rename`/`reset_index(drop=True)`/`nunique`/`drop_duplicates`）；
  - 通过 `/grill-me` + `/learn /plan` 定稿**「三类分级出题协议」**（写入本文件第 0 节），并沉淀为跨领域通用全局技能 `study-coach`。
- **实操产出**：
  - 编写并跑通 `C:\Users\ShuFen\学习初级数据\src\day8_dataframe.ipynb`（4 种 `DataFrame` 创建、`cars_sample.csv` 前两关二维切片与筛选统计、新协议第 1+2 类应用题与 `drop`/`rename`/`reset_index(drop=True)`/`drop_duplicates` 补充加练）；
  - 创建全局技能 `C:\Users\ShuFen\.gemini\config\skills\study-coach\SKILL.md` 及通用模板 `resources\handoff-template.md`。
- **抽查与掌握度**：
  - 已掌握：`loc[行切片, [列名列表]]` vs `iloc[行切片, [整数列位置列表]]` 二维对齐切片；`~列.isna()` 与 `isin` 联合过滤 `NaN`；链式 `( ... ).round(2)`；`cars['city'].drop_duplicates()`（`Series`）vs `cars.drop_duplicates(subset=['city'])`（`DataFrame`）类型与数据差异。
  - 新暴露/待复核：`header=None, names=[...]`（曾误答 `head=0, name=...`）、`strip()` 括号、`NaN` 不可用 `!= None`、拼写 `sort_values`/`DataFrame`、`reset_index(drop=True)` 需接住返回值，以及 `describe()` 需结合 `min`/`max`/`std` 判断离散度。
- **明日精确第一步**：开局 2 分钟抽查 **`header=None` vs `header=0`**、**`NaN` 判空与 `reset_index(drop=True)` 原理**、**`describe()` 离散度视角** → 3 句大白话前置建模 → 开看 **尚硅谷《Python数据分析》第 043 集起（`DataFrame` 进阶清洗与分组聚合，至 052 集收尾后触发第 3 类真实工作流综合题）**。

<!-- 后续每天按以下模板由 AI 追加：
### Day X（YYYY-MM-DD｜阶段X）
- **今日学习内容**：（看了哪几集 / 学了什么概念）
- **实操产出**：（写完并跑通的文件路径或 GitHub 提交）
- **抽查与掌握度**：（已稳固项 + 今日新暴露的薄弱点）
- **明日精确第一步**：（下次打开对话直接从哪里接手）
-->

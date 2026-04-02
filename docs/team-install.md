# Team Installation Guide / 团队安装说明

This document can be forwarded directly to team members who need to install and use the WorkBuddy reimbursement skill from scratch.

这份说明适合直接转发给团队成员，用于从零开始在 WorkBuddy 中安装和使用“出差报销”能力。

## 中文

### 先选哪种安装方式

普通同事默认推荐：

- 下载 Release 页面里的 `business-trip-expense-v1.0.0.zip`

如果你希望安装内容和当前云端能力完全同步，推荐：

- 直接从仓库 `main` 分支安装
- 或联系管理员获取下一版安装包

补充说明：

- `v1.0.0` 是首个稳定发布包，覆盖核心的文件夹到 API 报销流程
- 当前仓库 `main` 分支已经按新版云端服务能力更新脚本与说明

### 安装前准备

请先确认：

- 已安装 WorkBuddy
- 本机可以访问 `http://47.111.23.9`
- 处理报销时，本机有可用的 `python`

说明：

- 安装脚本本身不依赖 Python
- Python 只在真正执行 `/出差报销` 时需要

### 支持哪些材料

- 审批材料：出差审批 PDF
- 票据材料：火车票、机票、酒店发票、保险发票、地铁票、打车电子发票、打车行程单、出租车小票图片
- 票据格式支持：
  - `.pdf`
  - `.jpg`
  - `.jpeg`
  - `.png`
  - `.bmp`
  - `.tiff`
  - `.tif`
  - `.webp`

审批单识别规则：

- 仅按 PDF 识别审批单
- 当 PDF 文件名或直接父文件夹名包含 `商旅` 或 `出差` 时，视为审批单
- 其他支持文件会作为发票、行程单或票据上传

### 从零开始安装

1. 下载 `business-trip-expense-v1.0.0.zip`，或克隆仓库最新代码
2. 解压到任意本地目录，例如：

```text
C:\Users\你的用户名\Downloads\business-trip-expense-v1.0.0
```

3. 打开 PowerShell，进入解压目录或仓库根目录
4. 执行安装脚本：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

5. 重启 WorkBuddy，或执行 `/skills` 刷新

重要说明：

- 这条命令必须在当前目录能看到 `.codebuddy` 和 `scripts` 时执行
- 如果压缩包解压在 `D:` 盘，可以这样执行：

```powershell
cd "D:\business-trip-expense-v1.0.0"
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

### 安装完成后如何使用

在 WorkBuddy 中直接执行：

```text
/出差报销 "C:\你的报销文件夹路径"
```

例如：

```text
/出差报销 "C:\Users\你的用户名\Desktop\报销材料\test01"
```

### 文件夹怎么准备

建议把一次报销的材料集中放在一个文件夹里，例如：

```text
C:\Users\你的用户名\Desktop\报销材料\test01
```

里面通常包含：

- 出差审批 PDF
- 火车票 PDF
- 机票或保险发票 PDF
- 酒店发票 PDF
- 打车电子发票 PDF
- 打车电子行程单 PDF
- 出租车纸质小票拍照图片

### 会生成什么结果

处理成功后，通常会在传入文件夹下生成：

- `preview.json`
- `HOA-001出差费用报销汇总表.xls`
- `HOA-002交通费明细单.xlsx`

输出目录通常是：

```text
expense-output-<session_id>
```

补充说明：

- WorkBuddy 斜杠命令默认下载 `preview.json`、`HOA-001` 和 `HOA-002`
- 服务端还支持打包下载 `expense-files.zip`，但默认不在斜杠命令里额外下载

### 常见问题

#### 1. WorkBuddy 里找不到 `/出差报销`

- 重启 WorkBuddy
- 或执行 `/skills` 触发刷新
- 确认以下文件存在：
  - `~/.codebuddy/commands/出差报销.md`
  - `~/.codebuddy/skills/business-trip-expense/`

#### 2. 执行时报 `python` 找不到

- 这通常发生在真正执行 `/出差报销` 的时候，不是安装阶段
- 说明本机没有把 Python 加入 PATH
- 请先安装 Python，或把 `python` 命令配置到环境变量

#### 3. API 连接失败

- 检查本机网络
- 检查是否能访问 `http://47.111.23.9`
- 检查公司网络策略是否限制访问

#### 4. 没有识别到审批单

- 确认审批 PDF 文件名中带 `商旅` 或 `出差`
- 或确认审批单的直接父文件夹名中带 `商旅` 或 `出差`
- 不要只依赖更上层目录名

#### 5. `-ExecutionPolicy` 无法识别

这通常是因为命令前面少写了 `powershell`。

正确写法：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

错误写法：

```powershell
-ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

#### 6. 什么时候该用仓库主分支，而不是 `v1.0.0` 包

以下情况建议直接从仓库 `main` 分支安装：

- 你要尽快跟上云端最新能力
- 你需要图片票据支持等较新的输入能力
- 你是管理员、维护者或测试人员

### 管理员或高级用户

如果你负责统一分发，也可以使用 `workbuddy-business-trip-expense-marketplace.zip`。它更适合团队级共享、marketplace 形式分发或后续插件化管理。

## English

### Which Installation Path Should You Choose

For most end users:

- Download `business-trip-expense-v1.0.0.zip` from the Release page

If you want the installed files to match the latest cloud behavior exactly:

- Install from the repository `main` branch
- Or ask the admin for the next packaged release

Notes:

- `v1.0.0` is the first stable installer and covers the core folder-to-API workflow
- The repository `main` branch already reflects the newer cloud-side capabilities

### Before You Start

Please make sure:

- WorkBuddy is installed
- The machine can access `http://47.111.23.9`
- `python` is available when you actually run `/出差报销`

Notes:

- The installer itself does not require Python
- Python is only needed when the reimbursement command runs

### Supported Materials

- Approval material: travel-approval PDFs
- Expense material: railway tickets, airplane tickets, hotel invoices, insurance invoices, metro tickets, ride invoices, ride itineraries, and taxi receipt images
- Supported expense input formats:
  - `.pdf`
  - `.jpg`
  - `.jpeg`
  - `.png`
  - `.bmp`
  - `.tiff`
  - `.tif`
  - `.webp`

Approval detection rules:

- Only PDFs are treated as approval candidates
- A PDF is treated as an approval file when its filename or immediate parent folder contains `商旅` or `出差`
- Every other supported file is uploaded as invoice, itinerary, or receipt material

### Fresh Installation Steps

1. Download `business-trip-expense-v1.0.0.zip`, or clone the latest repository
2. Extract it to any local folder, for example:

```text
C:\Users\YourName\Downloads\business-trip-expense-v1.0.0
```

3. Open PowerShell and enter the extracted folder or repository root
4. Run the install script:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

5. Restart WorkBuddy or run `/skills` to refresh

Important:

- Run the command where both `.codebuddy` and `scripts` are present
- If the package is extracted on drive `D:`, first change into that folder and then run the command

```powershell
cd "D:\business-trip-expense-v1.0.0"
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

### How To Use After Installation

Run this directly in WorkBuddy:

```text
/出差报销 "C:\path\to\your\expense-folder"
```

### How To Prepare the Input Folder

Put one reimbursement batch into a single folder, for example:

```text
C:\Users\YourName\Desktop\expense-materials\test01
```

That folder usually contains:

- travel-approval PDFs
- railway ticket PDFs
- airplane or insurance invoice PDFs
- hotel invoice PDFs
- ride invoice PDFs
- ride itinerary PDFs
- taxi receipt photos

### Expected Output

On success, the input folder usually gets:

- `preview.json`
- `HOA-001出差费用报销汇总表.xls`
- `HOA-002交通费明细单.xlsx`

The output folder is usually named:

```text
expense-output-<session_id>
```

Notes:

- The WorkBuddy slash command downloads `preview.json`, `HOA-001`, and `HOA-002` by default
- The server can also provide `expense-files.zip`, but the slash command does not download it unless explicitly extended later

### FAQ

#### 1. `/出差报销` does not appear in WorkBuddy

- Restart WorkBuddy
- Or run `/skills` to refresh
- Confirm these files exist:
  - `~/.codebuddy/commands/出差报销.md`
  - `~/.codebuddy/skills/business-trip-expense/`

#### 2. `python` is not found

- This usually happens when `/出差报销` is running, not during installation
- Python is not available in PATH
- Install Python or add the `python` command to the environment

#### 3. API connection failed

- Check local network connectivity
- Check whether `http://47.111.23.9` is reachable
- Check whether company network policies block the request

#### 4. No approval PDF was detected

- Make sure the approval PDF filename contains `商旅` or `出差`
- Or make sure the immediate parent folder name contains `商旅` or `出差`
- Do not rely only on higher-level parent folders

#### 5. `-ExecutionPolicy` was not recognized

This usually means the command was entered without the leading `powershell`.

Correct command:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

Wrong command:

```powershell
-ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

#### 6. When should you install from `main` instead of the `v1.0.0` package

Use the repository `main` branch if:

- you need the latest cloud-aligned behavior immediately
- you need newer inputs such as receipt images
- you are an admin, maintainer, or tester

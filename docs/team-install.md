# Team Installation Guide / 团队安装说明

This document is intended to be forwarded directly to team members who need to install and use the WorkBuddy reimbursement skill from scratch.

这份说明适合直接转发给团队成员，用于从零开始在 WorkBuddy 中安装和使用“出差报销”能力。

## 中文

### 推荐安装方式

推荐使用正式安装包 `business-trip-expense-v1.0.0.zip`。

它只包含最需要的内容：

- `.codebuddy/skills/business-trip-expense/`
- `.codebuddy/commands/出差报销.md`
- `scripts/install-user.ps1`

### 安装前准备

请先确认：

- 已安装 WorkBuddy
- 本机可用 `python`
- 本机可以访问 `http://47.111.23.9`

### 从零开始安装

1. 下载 `business-trip-expense-v1.0.0.zip`
2. 解压到任意本地目录，例如：

```text
C:\Users\你的用户名\Downloads\business-trip-expense-v1.0.0
```

3. 打开 PowerShell，进入解压目录
4. 执行安装脚本：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

5. 重启 WorkBuddy，或执行 `/skills` 刷新

### 安装完成后如何使用

在 WorkBuddy 中直接执行：

```text
/出差报销 "C:\你的报销文件夹路径"
```

例如：

```text
/出差报销 "C:\Users\你的用户名\Desktop\报销材料\test01"
```

### 会生成什么结果

处理成功后，通常会在传入文件夹下生成：

- `preview.json`
- `HOA-001出差费用报销汇总表.xls`
- `HOA-002交通费明细单.xlsx`

输出目录通常是：

```text
expense-output-<session_id>
```

### 常见问题

#### 1. WorkBuddy 里找不到 `/出差报销`

- 重启 WorkBuddy
- 或执行 `/skills` 触发刷新
- 确认以下文件存在：
  - `~/.codebuddy/commands/出差报销.md`
  - `~/.codebuddy/skills/business-trip-expense/`

#### 2. 执行时报 `python` 找不到

- 说明本机没有把 Python 加入 PATH
- 请先安装 Python，或把 `python` 命令配置到环境变量

#### 3. API 连接失败

- 检查本机网络
- 检查是否能访问 `http://47.111.23.9`
- 检查公司网络策略是否限制访问

#### 4. 没有识别到审批单

- 确认文件名或父目录名中包含 `商旅` 或 `出差`
- 否则技能会把 PDF 当作发票或行程单处理

### 管理员或高级用户

如果你负责统一分发，也可以使用 `workbuddy-business-trip-expense-marketplace.zip`。它更适合团队级共享、marketplace 形式分发或后续插件化管理。

## English

### Recommended Installation Method

Use the end-user package `business-trip-expense-v1.0.0.zip`.

It contains only the required files:

- `.codebuddy/skills/business-trip-expense/`
- `.codebuddy/commands/出差报销.md`
- `scripts/install-user.ps1`

### Before You Start

Please make sure:

- WorkBuddy is installed
- `python` is available on the machine
- The machine can access `http://47.111.23.9`

### Fresh Installation Steps

1. Download `business-trip-expense-v1.0.0.zip`
2. Extract it to any local folder, for example:

```text
C:\Users\YourName\Downloads\business-trip-expense-v1.0.0
```

3. Open PowerShell and enter the extracted folder
4. Run the install script:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

5. Restart WorkBuddy or run `/skills` to refresh

### How To Use After Installation

Run this directly in WorkBuddy:

```text
/出差报销 "C:\path\to\your\expense-folder"
```

Example:

```text
/出差报销 "C:\Users\YourName\Desktop\expense-materials\test01"
```

### Expected Output

On success, the input folder will usually contain:

- `preview.json`
- `HOA-001出差费用报销汇总表.xls`
- `HOA-002交通费明细单.xlsx`

The output folder is usually named:

```text
expense-output-<session_id>
```

### FAQ

#### 1. `/出差报销` does not appear in WorkBuddy

- Restart WorkBuddy
- Or run `/skills` to refresh
- Confirm these files exist:
  - `~/.codebuddy/commands/出差报销.md`
  - `~/.codebuddy/skills/business-trip-expense/`

#### 2. `python` is not found

- Python is not available in PATH
- Install Python or add the `python` command to the environment

#### 3. API connection failed

- Check local network connectivity
- Check whether `http://47.111.23.9` is reachable
- Check whether company network policies block the request

#### 4. No approval PDF was detected

- Make sure the filename or parent folder name contains `商旅` or `出差`
- Otherwise the skill will treat the PDF as an invoice or itinerary file

### For Admins or Advanced Users

If you are distributing this to a team at scale, you can also use `workbuddy-business-trip-expense-marketplace.zip`, which is better suited for marketplace-style distribution or plugin-oriented management.

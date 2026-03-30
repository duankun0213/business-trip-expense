# 团队安装说明

这份说明适合直接转发给团队成员，用于从零开始在 WorkBuddy 中安装和使用“出差报销”能力。

## 推荐安装方式

推荐使用正式安装包 `business-trip-expense-v1.0.0.zip`。

它只包含最需要的内容：

- `.codebuddy/skills/business-trip-expense/`
- `.codebuddy/commands/出差报销.md`
- `scripts/install-user.ps1`

## 安装前准备

请先确认：

- 已安装 WorkBuddy
- 本机可用 `python`
- 本机可以访问 `http://47.111.23.9`

## 从零开始安装

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

## 安装完成后如何使用

在 WorkBuddy 中直接执行：

```text
/出差报销 "C:\你的报销文件夹路径"
```

例如：

```text
/出差报销 "C:\Users\你的用户名\Desktop\报销材料\test01"
```

## 会生成什么结果

处理成功后，通常会在传入文件夹下生成：

- `preview.json`
- `HOA-001出差费用报销汇总表.xls`
- `HOA-002交通费明细单.xlsx`

输出目录通常是：

```text
expense-output-<session_id>
```

## 常见问题

### 1. WorkBuddy 里找不到 `/出差报销`

- 重启 WorkBuddy
- 或执行 `/skills` 触发刷新
- 确认以下文件存在：
  - `~/.codebuddy/commands/出差报销.md`
  - `~/.codebuddy/skills/business-trip-expense/`

### 2. 执行时报 `python` 找不到

- 说明本机没有把 Python 加入 PATH
- 请先安装 Python，或把 `python` 命令配置到环境变量

### 3. API 连接失败

- 检查本机网络
- 检查是否能访问 `http://47.111.23.9`
- 检查公司网络策略是否限制访问

### 4. 没有识别到审批单

- 确认文件名或父目录名中包含 `商旅` 或 `出差`
- 否则技能会把 PDF 当作发票或行程单处理

## 管理员或高级用户

如果你负责统一分发，也可以使用 `workbuddy-business-trip-expense-marketplace.zip`。它更适合团队级共享、marketplace 形式分发或后续插件化管理。

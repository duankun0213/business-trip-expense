# business-trip-expense

WorkBuddy skill repository for business-trip expense reimbursement.

WorkBuddy 出差费用报销技能仓库。

## 中文

### 项目简介

这个仓库用于在 WorkBuddy 中处理出差费用报销资料。它会从本地文件夹收集出差审批 PDF 与发票或行程单 PDF，调用远程报销 API，并下载最终生成的 HOA 报销 Excel 文件。

### 适用场景

- 团队成员需要在 WorkBuddy 中快速完成出差费用报销资料整理
- 希望通过统一的斜杠命令降低安装和使用门槛
- 希望把技能、命令、安装脚本和发布说明放进同一个 Git 仓库管理

### 核心能力

- 递归扫描本地文件夹中的 PDF
- 按文件名或父目录名中的 `商旅`、`出差` 自动识别审批单
- 将其他 PDF 视为发票或行程单
- 调用远程 API：
  - `POST http://47.111.23.9/expense/process`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa001`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa002`
- 下载以下结果文件：
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`
  - `preview.json`

### 使用方式

#### 方式 1：作为项目仓库使用

1. 克隆本仓库
2. 用 WorkBuddy 打开仓库根目录
3. 执行：

```text
/出差报销 "C:\你的文件夹路径"
```

#### 方式 2：安装到用户目录，全局使用

在仓库根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

安装后会把以下内容复制到用户目录：

- `~/.codebuddy/skills/business-trip-expense/`
- `~/.codebuddy/commands/出差报销.md`

然后重启 WorkBuddy，或执行 `/skills` 刷新。

### 发布产物

- `business-trip-expense-v1.0.0.zip`
  - 面向最终使用者的正式安装包
  - 只保留 `.codebuddy/` 和安装脚本
- `workbuddy-business-trip-expense-marketplace.zip`
  - 面向管理员或高级用户的团队分发包
  - 保留 marketplace 或 plugin 结构，适合统一分发

### 环境要求

- 本机可用 `python`
- 本机可以访问 `http://47.111.23.9`
- WorkBuddy 支持项目级 `.codebuddy/commands` 与 `.codebuddy/skills`

### 文档入口

- 发布说明：`docs/releases/v1.0.0.md`
- GitHub Release 正文模板：`docs/releases/github-release-v1.0.0.md`
- 团队安装说明：`docs/team-install.md`
- 更新日志：`CHANGELOG.md`

## English

### Overview

This repository provides a WorkBuddy skill for business-trip expense reimbursement. It scans a local folder for travel-approval PDFs and invoice or itinerary PDFs, sends them to the remote reimbursement API, and downloads the generated HOA Excel outputs.

### Use Cases

- Team members need a faster way to prepare trip-reimbursement materials in WorkBuddy
- You want a single slash command to reduce installation and usage friction
- You want to manage skills, commands, install scripts, and release notes in one Git repository

### Core Capabilities

- Recursively scan a local folder for PDF files
- Detect approval PDFs by `商旅` or `出差` in filenames or parent folder names
- Treat other PDFs as invoices or itineraries
- Call the remote API:
  - `POST http://47.111.23.9/expense/process`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa001`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa002`
- Download:
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`
  - `preview.json`

### How To Use

#### Option 1: Use it as a project repository

1. Clone this repository
2. Open the repository root in WorkBuddy
3. Run:

```text
/出差报销 "C:\path\to\your\folder"
```

#### Option 2: Install it globally for the current user

Run this command at the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

The script copies these files into the user profile:

- `~/.codebuddy/skills/business-trip-expense/`
- `~/.codebuddy/commands/出差报销.md`

Then restart WorkBuddy or run `/skills` to refresh commands and skills.

### Release Artifacts

- `business-trip-expense-v1.0.0.zip`
  - End-user installer package
  - Contains only `.codebuddy/` and the install script
- `workbuddy-business-trip-expense-marketplace.zip`
  - Team-distribution package for admins or advanced users
  - Preserves marketplace or plugin-oriented structure

### Requirements

- `python` must be available on the machine
- The machine must be able to reach `http://47.111.23.9`
- WorkBuddy must support project-level `.codebuddy/commands` and `.codebuddy/skills`

### Documentation

- Release notes: `docs/releases/v1.0.0.md`
- GitHub Release body template: `docs/releases/github-release-v1.0.0.md`
- Team installation guide: `docs/team-install.md`
- Changelog: `CHANGELOG.md`

## License

MIT License. See `LICENSE`.

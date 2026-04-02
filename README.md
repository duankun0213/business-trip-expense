# business-trip-expense

WorkBuddy skill repository for business-trip expense reimbursement.

WorkBuddy 出差费用报销技能仓库。

## 中文

### 项目简介

这个仓库用于在 WorkBuddy 中处理出差费用报销资料。当前仓库主分支已经按你最新部署在云端的报销服务能力整理说明，并提供对应的 WorkBuddy skill、斜杠命令、安装脚本和团队文档。

### 当前云端能力

- 审批材料：出差审批 PDF
- 票据材料：火车票、机票、酒店发票、保险发票、地铁票、打车电子发票、打车行程单、出租车小票图片
- 输入格式：审批单使用 PDF；票据支持 PDF 和常见图片格式
- 模板处理：服务端默认加载 HOA-001 与 HOA-002 模板，WorkBuddy 流程默认不需要用户手动上传模板
- 输出结果：
  - `preview.json`
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`
  - 可选打包下载 `expense-files.zip`

### WorkBuddy 仓库提供什么

- `business-trip-expense` skill
- `/出差报销` 斜杠命令
- 用户级安装脚本 `scripts/install-user.ps1`
- 面向团队的安装说明、同事使用说明和发布文档

### 文件识别规则

- 递归扫描以下文件类型：
  - `.pdf`
  - `.jpg`
  - `.jpeg`
  - `.png`
  - `.bmp`
  - `.tiff`
  - `.tif`
  - `.webp`
- 审批单识别规则：
  - 仅按 PDF 识别审批单
  - 当审批 PDF 的文件名或直接父文件夹名中包含 `商旅` 或 `出差` 时，视为审批单
- 其他支持的文件会按发票、行程单或票据上传

### 使用方式

#### 方式 1：作为项目仓库使用

1. 克隆本仓库
2. 用 WorkBuddy 打开仓库根目录
3. 执行：

```text
/出差报销 "C:\你的文件夹路径"
```

这条路径更适合想尽快跟上云端最新能力的使用者或维护者。

#### 方式 2：安装到用户目录，全局使用

普通同事默认推荐使用 Release 页面里的：

- `business-trip-expense-v1.1.0.zip`

不建议普通使用者下载：

- `workbuddy-business-trip-expense-marketplace.zip`

因为它更适合管理员、统一分发人员或高级用户。

说明：

- `v1.1.0` 对齐了当前云端服务能力和最新 GitHub 说明
- `v1.0.0` 仍保留为首个稳定发布包，方便历史回溯
- 如果你希望安装内容和当前仓库一致，优先使用 `v1.1.0` 或从仓库根目录执行安装脚本

在仓库根目录或解压后的安装包根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

注意：

- 这条命令要在当前目录能看到 `.codebuddy` 和 `scripts` 的位置执行
- 如果解压在 `D:` 盘，也一样先进入解压目录再执行

例如：

```powershell
cd "D:\business-trip-expense-v1.1.0"
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

安装后会把以下内容复制到用户目录：

- `~/.codebuddy/skills/business-trip-expense/`
- `~/.codebuddy/commands/出差报销.md`

然后重启 WorkBuddy，或执行 `/skills` 刷新。

补充说明：

- 安装脚本本身不依赖 Python
- 真正执行 `/出差报销` 处理文件时，需要本机可用 `python`
- 还需要本机可以访问 `http://47.111.23.9`

### 发布产物

- `business-trip-expense-v1.1.0.zip`
  - 面向最终使用者的当前推荐安装包
  - 已对齐当前云端服务能力与最新说明
- `business-trip-expense-v1.0.0.zip`
  - 历史安装包
  - 保留首个稳定发布版本
- `workbuddy-business-trip-expense-marketplace.zip`
  - 面向管理员或高级用户的团队分发包
  - 保留 marketplace 或 plugin 结构
- 当前仓库 `main` 分支
  - 跟随最新云端能力更新 skill 脚本和文档
  - 更适合维护者、测试者或需要先用到最新能力的团队成员

### 环境要求

- WorkBuddy 支持项目级 `.codebuddy/commands` 与 `.codebuddy/skills`
- 本机可用 `python`
- 本机可以访问 `http://47.111.23.9`

### 文档入口

- 团队安装说明：`docs/team-install.md`
- 同事从零使用说明：`docs/workbuddy-colleague-guide.md`
- 最新发布说明：`docs/releases/v1.1.0.md`
- 发布说明：`docs/releases/v1.0.0.md`
- 最新 GitHub Release 正文模板：`docs/releases/github-release-v1.1.0.md`
- GitHub Release 正文模板：`docs/releases/github-release-v1.0.0.md`
- 更新日志：`CHANGELOG.md`

## English

### Overview

This repository provides a WorkBuddy skill for business-trip expense reimbursement. The current `main` branch is aligned with the latest cloud service behavior and includes the WorkBuddy skill, slash command, installer, and team-facing documentation.

### Current Cloud Capabilities

- Approval material: travel-approval PDFs
- Expense material: railway tickets, airplane tickets, hotel invoices, insurance invoices, metro tickets, ride invoices, ride itineraries, and taxi receipt images
- Input formats: approval files stay in PDF; invoice files can be PDF or common image formats
- Template handling: the server loads default HOA-001 and HOA-002 templates, so the WorkBuddy flow does not require manual template upload
- Outputs:
  - `preview.json`
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`
  - optional bundled archive `expense-files.zip`

### What This Repository Provides

- `business-trip-expense` skill
- `/出差报销` slash command
- User-level installer `scripts/install-user.ps1`
- Team installation, colleague usage, and release documentation

### File Detection Rules

- The workflow recursively scans:
  - `.pdf`
  - `.jpg`
  - `.jpeg`
  - `.png`
  - `.bmp`
  - `.tiff`
  - `.tif`
  - `.webp`
- Approval detection rules:
  - Only PDFs are treated as approval candidates
  - A PDF is treated as an approval file when its filename or immediate parent folder contains `商旅` or `出差`
- Every other supported file is uploaded as invoice, itinerary, or receipt material

### How To Use

#### Option 1: Use the repository directly

1. Clone this repository
2. Open the repository root in WorkBuddy
3. Run:

```text
/出差报销 "C:\path\to\your\folder"
```

This path is best when you want the latest cloud-aligned behavior immediately.

#### Option 2: Install it globally for the current user

Most end users should use the Release package:

- `business-trip-expense-v1.1.0.zip`

Regular users usually do not need:

- `workbuddy-business-trip-expense-marketplace.zip`

Notes:

- `v1.1.0` matches the current cloud-side behavior and latest GitHub docs
- `v1.0.0` remains available as the first stable historical package
- If you want the installed files to match the repository exactly, prefer `v1.1.0` or install from the repository root

Run this command from the repository root or the extracted installer root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

Important:

- Run the command where both `.codebuddy` and `scripts` are present
- If the package is extracted on drive `D:`, first change into that folder and then run the command

Example:

```powershell
cd "D:\business-trip-expense-v1.1.0"
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

The script copies these files into the user profile:

- `~/.codebuddy/skills/business-trip-expense/`
- `~/.codebuddy/commands/出差报销.md`

Then restart WorkBuddy or run `/skills` to refresh commands and skills.

Additional notes:

- The installer itself does not require Python
- Python is required later when the user actually runs `/出差报销`
- The machine must also be able to reach `http://47.111.23.9`

### Release Artifacts

- `business-trip-expense-v1.1.0.zip`
  - Current recommended end-user installer
  - Aligned with the current cloud service behavior
- `business-trip-expense-v1.0.0.zip`
  - Historical installer
  - Preserves the first stable release
- `workbuddy-business-trip-expense-marketplace.zip`
  - Team-distribution package for admins or advanced users
  - Preserves marketplace or plugin-oriented structure
- Current `main` branch
  - Tracks the latest cloud-side behavior in the skill script and docs
  - Better for maintainers, testers, or teams that need the latest capability set before the next packaged release

### Requirements

- WorkBuddy must support project-level `.codebuddy/commands` and `.codebuddy/skills`
- `python` must be available on the machine
- The machine must be able to reach `http://47.111.23.9`

### Documentation

- Team installation guide: `docs/team-install.md`
- Colleague quick-start guide: `docs/workbuddy-colleague-guide.md`
- Latest release notes: `docs/releases/v1.1.0.md`
- Release notes: `docs/releases/v1.0.0.md`
- Latest GitHub Release body template: `docs/releases/github-release-v1.1.0.md`
- GitHub Release body template: `docs/releases/github-release-v1.0.0.md`
- Changelog: `CHANGELOG.md`

## License

MIT License. See `LICENSE`.

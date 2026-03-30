## 概览

`business-trip-expense` 的首个可用版本，提供面向 WorkBuddy 的出差费用报销能力。

支持从本地文件夹收集 PDF，自动区分出差审批单与发票/行程单，调用远程报销 API，并下载最终生成的 HOA 报销 Excel 文件。

## 本次发布内容

- 新增 `business-trip-expense` Skill
- 新增 `/出差报销` 斜杠命令
- 新增用户级安装脚本 `scripts/install-user.ps1`
- 新增项目级 `.codebuddy/skills` 与 `.codebuddy/commands` 仓库结构
- 集成远程报销 API：
  - `POST http://47.111.23.9/expense/process`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa001`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa002`

## 主要能力

- 递归扫描本地文件夹中的 PDF
- 按文件名或父目录名中的 `商旅`、`出差` 自动识别审批单
- 将其他 PDF 视为发票或行程单
- 上传文件到远程 API 并获取 `session_id`
- 下载以下结果文件：
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`
  - `preview.json`

## 使用方式

### 项目内使用

```text
/出差报销 "C:\你的文件夹路径"
```

### 全局安装后使用

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

安装完成后，可在任意 WorkBuddy 项目中执行：

```text
/出差报销 "C:\你的文件夹路径"
```

## 运行要求

- 本机可用 `python`
- WorkBuddy 支持项目级 `.codebuddy` 命令与技能
- 本机可以访问 `http://47.111.23.9`

## 已知说明

- 默认不下载 zip 打包文件
- 结果生成依赖远程 API 服务可用性
- 输出目录默认创建在传入文件夹下，命名为 `expense-output-<session_id>`

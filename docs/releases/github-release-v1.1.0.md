## 概览

`business-trip-expense` 的功能更新版本，已对齐当前云端报销服务的实际能力。

这次更新同步刷新了 WorkBuddy 技能脚本、安装说明和 GitHub 仓库文档，当前推荐安装包为 `business-trip-expense-v1.1.0.zip`。

## 本次发布内容

- 更新 `business-trip-expense` Skill
- 更新 `/出差报销` 斜杠命令说明
- 更新 README、团队安装说明和同事使用说明
- 新增 `v1.1.0` 发布说明与 Release 正文模板

## 主要变化

- 支持递归扫描以下输入文件：
  - PDF
  - JPG / JPEG
  - PNG
  - BMP
  - TIFF / TIF
  - WEBP
- 审批单识别规则更新为：
  - 仅把审批 PDF 作为审批候选
  - 当 PDF 文件名或直接父文件夹名包含 `商旅` 或 `出差` 时，视为审批单
- 票据说明更新为支持更多云端实际能力：
  - 火车票
  - 机票
  - 保险发票
  - 酒店发票
  - 地铁票
  - 打车电子发票
  - 打车电子行程单
  - 出租车小票图片
- 继续默认下载以下结果：
  - `preview.json`
  - `HOA-001出差费用报销汇总表.xls`
  - `HOA-002交通费明细单.xlsx`

## 安装方式

下载 `business-trip-expense-v1.1.0.zip`，在解压后的根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

然后在 WorkBuddy 中执行：

```text
/出差报销 "C:\你的文件夹路径"
```

## 运行要求

- 本机可用 `python`
- WorkBuddy 支持项目级 `.codebuddy` 命令与技能
- 本机可以访问 `http://47.111.23.9`

## 已知说明

- 默认不下载 zip 打包文件
- 输出目录默认创建在传入文件夹下，命名为 `expense-output-<session_id>`
- 结果生成依赖远程 API 服务可用性

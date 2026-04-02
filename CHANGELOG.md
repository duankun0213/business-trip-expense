# Changelog

所有重要变更都会记录在这个文件中。

## Unreleased

## v1.1.0 - 2026-04-02

### Changed

- 更新 WorkBuddy 技能脚本，支持递归扫描票据 PDF 与图片文件
- 审批单识别规则调整为“审批 PDF 文件名或直接父文件夹名包含 `商旅` / `出差`”
- README、团队安装说明和同事使用说明改为按当前云端服务能力描述
- 默认推荐安装包从 `v1.0.0` 切换为 `v1.1.0`
- 在文档中区分 `v1.1.0` 当前推荐包、`v1.0.0` 历史包与仓库 `main` 分支的适用场景

### Documentation

- 更新 README，补充推荐下载包、安装目录要求、`D:` 盘示例和 Python 依赖说明
- 更新团队安装说明，明确安装脚本执行位置与常见 PowerShell 错误
- 更新同事使用说明，补充安装阶段与运行阶段的依赖区别
- 补充 `-ExecutionPolicy` 常见误用的排查说明
- 新增 `v1.1.0` 发布说明与 GitHub Release 正文模板

### Packaging

- 生成新版正式安装包：`business-trip-expense-v1.1.0.zip`

## v1.0.0 - 2026-03-30

### Added

- 新增 WorkBuddy Skill：`business-trip-expense`
- 新增斜杠命令：`/出差报销`
- 新增用户级安装脚本：`scripts/install-user.ps1`
- 新增公开版 `README.md`
- 新增发布说明与 GitHub Release 正文模板
- 新增团队内部安装说明文档

### Integrated

- 接入远程报销 API：
  - `POST http://47.111.23.9/expense/process`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa001`
  - `GET http://47.111.23.9/expense/download/{session_id}/hoa002`

### Packaging

- 提供面向最终用户的正式安装包：`business-trip-expense-v1.0.0.zip`
- 提供面向团队分发的 marketplace 包：`workbuddy-business-trip-expense-marketplace.zip`

### Notes

- 默认不下载 zip 打包文件
- 输出目录默认创建在传入文件夹下，命名为 `expense-output-<session_id>`
- 结果生成依赖远程 API 服务可用性

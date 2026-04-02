---
name: business-trip-expense
description: 处理出差费用报销文件夹。接收一个本地文件夹路径，递归收集审批 PDF 与发票/行程单 PDF 或图片，按文件名或直接父文件夹名中的“商旅”或“出差”识别审批单，其余作为发票上传到 http://47.111.23.9/expense/process，读取 session_id，并下载 HOA-001 和 HOA-002 Excel 结果。Use when the user asks to process a reimbursement folder, approval PDFs, invoice PDFs, ride itineraries, or taxi receipt images.
allowed-tools: Read, Bash
---

# 出差费用报销

用这个技能处理一个包含出差审批单 PDF，以及发票、行程单 PDF 或图片的本地文件夹。

## 输入

用户会提供一个本地文件夹路径，或通过斜杠命令把路径传进来。

## 工作流

1. 确认用户提供了文件夹路径。
2. 调用技能目录下的脚本处理该文件夹。脚本会：
   - 递归收集 `.pdf`、`.jpg`、`.jpeg`、`.png`、`.bmp`、`.tiff`、`.tif`、`.webp`
   - 仅把审批单按 PDF 识别
   - 按文件名或直接父文件夹名中的 `商旅`、`出差` 识别审批单
   - 其余文件统一作为发票或行程单上传

3. 调用命令：

```powershell
python "{baseDirectory}\scripts\process_expense_folder.py" "<folder-path>"
```

4. 从脚本输出中提取：
   - `session_id`
   - `Preview` 摘要
   - `preview.json`
   - `HOA-001出差费用报销汇总表.xls`
   - `HOA-002交通费明细单.xlsx`
5. 用简洁中文向用户汇报结果。

## 输出要求

- 说明成功或失败。
- 成功时报告 `session_id`。
- 成功时总结行程、交通明细和未匹配项。
- 成功时明确给出生成文件路径。
- 失败时明确是路径错误、审批单缺失、审批单命名不符合规则，还是 API 连接失败。
- 除非用户明确要求，否则不要下载 zip 包。

## Bundled Resources

- `scripts/process_expense_folder.py`：完成分类、上传、下载。
- `references/api.md`：记录 API 端点和字段规则。

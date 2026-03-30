---
name: business-trip-expense
description: 处理出差费用报销文件夹。接收一个本地文件夹路径，递归收集 PDF，按文件名或父文件夹名中的“商旅”或“出差”识别审批单，其余视为发票或行程单，调用 http://47.111.23.9/expense/process 上传文件，读取 session_id，并下载 HOA-001 和 HOA-002 Excel 结果。Use when the user asks to process a reimbursement folder, approval PDFs, invoice PDFs, or travel itinerary PDFs.
allowed-tools: Read, Bash
---

# 出差费用报销

用这个技能处理一个包含出差审批单和发票或行程单 PDF 的本地文件夹。

## 输入

用户会提供一个本地文件夹路径，或通过斜杠命令把路径传进来。

## 工作流

1. 确认用户提供了文件夹路径。
2. 调用技能目录下的脚本处理该文件夹：

```powershell
python "{baseDirectory}\scripts\process_expense_folder.py" "<folder-path>"
```

3. 从脚本输出中提取：
   - `session_id`
   - `Preview` 摘要
   - `preview.json`
   - `HOA-001出差费用报销汇总表.xls`
   - `HOA-002交通费明细单.xlsx`
4. 用简洁中文向用户汇报结果。

## 输出要求

- 说明成功或失败。
- 成功时报告 `session_id`。
- 成功时总结行程、交通明细和未匹配项。
- 成功时明确给出生成文件路径。
- 失败时明确是路径错误、审批单缺失，还是 API 连接失败。
- 除非用户明确要求，否则不要下载 zip 包。

## Bundled Resources

- `scripts/process_expense_folder.py`：完成分类、上传、下载。
- `references/api.md`：记录 API 端点和字段规则。

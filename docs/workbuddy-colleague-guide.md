# WorkBuddy 同事使用说明

这份说明面向“最终使用者”，也就是只想在 WorkBuddy 里完成出差报销处理的同事。

如果你只是想安装后直接用，请优先选择：

`business-trip-expense-v1.0.0.zip`

不建议普通同事使用：

`workbuddy-business-trip-expense-marketplace.zip`

它更适合管理员、统一分发人员或高级用户。

## 一、先选哪个安装包

### 1. 普通同事

下载：

`business-trip-expense-v1.0.0.zip`

原因：

- 这是正式安装包
- 内容最精简
- 安装步骤最少
- 更适合个人直接使用

### 2. 管理员或高级用户

下载：

`workbuddy-business-trip-expense-marketplace.zip`

适合场景：

- 团队统一分发
- 需要按 marketplace 或 plugin 结构管理
- 需要做二次封装

如果你只是正常报销使用，直接忽略这个包。

## 二、使用前准备

开始前请先确认：

- 电脑已安装 WorkBuddy
- 电脑已安装 Python，并且 `python` 命令可用
- 电脑可以访问 `http://47.111.23.9`
- 你已经准备好一个本地文件夹，里面放着这次报销需要的 PDF 文件

## 三、文件夹应该怎么准备

把这次报销相关文件放到一个文件夹里，例如：

```text
C:\Users\你的用户名\Desktop\报销材料\test01
```

这个文件夹里通常会包含：

- 出差审批 PDF
- 打车电子发票 PDF
- 打车电子行程单 PDF
- 火车票或机票发票 PDF
- 酒店发票 PDF

### 审批单识别规则

系统会把“文件名”或“父文件夹名”中包含以下关键词的 PDF 识别为审批单：

- `商旅`
- `出差`

其余 PDF 会被当作发票或行程单处理。

所以最稳妥的做法是：

- 审批单文件名里直接带 `商旅` 或 `出差`
- 或者把审批单放到名字带 `商旅` / `出差` 的文件夹里

## 四、下载安装包

打开 GitHub Release 页面，下载正式安装包：

`business-trip-expense-v1.0.0.zip`

下载后，把它解压到一个你容易找到的位置，例如：

```text
C:\Users\你的用户名\Downloads\business-trip-expense-v1.0.0
```

## 五、安装到 WorkBuddy

### 第一步：打开 PowerShell

进入刚才解压后的目录，例如：

```powershell
cd "C:\Users\你的用户名\Downloads\business-trip-expense-v1.0.0"
```

### 第二步：执行安装脚本

运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

安装成功后，它会把以下内容复制到你的用户目录：

- `~/.codebuddy/skills/business-trip-expense/`
- `~/.codebuddy/commands/出差报销.md`

### 第三步：刷新 WorkBuddy

安装完成后：

- 重启 WorkBuddy

或

- 在 WorkBuddy 里执行 `/skills`

这样可以让新命令和新技能生效。

## 六、在 WorkBuddy 中怎么用

安装完成后，在 WorkBuddy 中直接输入：

```text
/出差报销 "C:\你的报销文件夹路径"
```

例如：

```text
/出差报销 "C:\Users\你的用户名\Desktop\报销材料\test01"
```

## 七、执行后会发生什么

WorkBuddy 会自动完成这些步骤：

1. 扫描你给的文件夹里的 PDF
2. 自动区分审批单和发票或行程单
3. 调用远程报销 API 上传文件
4. 获取 `session_id`
5. 下载生成的报销结果文件

## 八、最终会得到什么文件

处理成功后，通常会在你传入的原始文件夹下生成一个新目录：

```text
expense-output-<session_id>
```

里面通常会有：

- `preview.json`
- `HOA-001出差费用报销汇总表.xls`
- `HOA-002交通费明细单.xlsx`

其中：

- `preview.json` 是解析预览结果
- `HOA-001出差费用报销汇总表.xls` 是报销汇总表
- `HOA-002交通费明细单.xlsx` 是交通费明细单

## 九、推荐的实际使用流程

给同事的最简单流程就是：

1. 从 GitHub Release 下载 `business-trip-expense-v1.0.0.zip`
2. 解压
3. 运行安装脚本
4. 重启 WorkBuddy
5. 准备一个放满报销 PDF 的文件夹
6. 在 WorkBuddy 里执行：

```text
/出差报销 "C:\你的文件夹路径"
```

7. 等待处理完成
8. 打开生成的 `expense-output-<session_id>` 目录查看 Excel 文件

## 十、常见问题

### 1. WorkBuddy 里找不到 `/出差报销`

处理方法：

- 重启 WorkBuddy
- 或执行 `/skills`
- 检查这两个路径是否存在：
  - `~/.codebuddy/commands/出差报销.md`
  - `~/.codebuddy/skills/business-trip-expense/`

### 2. 运行时报 `python` 找不到

说明：

- 本机没有安装 Python
- 或 Python 没有加入环境变量

处理方法：

- 安装 Python
- 确保在 PowerShell 中输入 `python --version` 能成功

### 3. 提示 API 连接失败

可能原因：

- 本机网络异常
- 无法访问 `http://47.111.23.9`
- 公司网络策略拦截了请求

### 4. 没识别到审批单

处理方法：

- 确认审批 PDF 文件名中带 `商旅` 或 `出差`
- 或确认审批单所在父文件夹名中带 `商旅` 或 `出差`

### 5. 下载哪个包最合适

普通同事：

- 下载 `business-trip-expense-v1.0.0.zip`

管理员或高级用户：

- 下载 `workbuddy-business-trip-expense-marketplace.zip`

## 十一、一句话版发给同事

你可以直接把下面这段话发给同事：

```text
请到 GitHub Release 页面下载 business-trip-expense-v1.0.0.zip，解压后在 PowerShell 里执行 scripts/install-user.ps1，然后重启 WorkBuddy。之后在 WorkBuddy 里输入：
/出差报销 "你的报销文件夹路径"
处理完成后，到原文件夹下的 expense-output-<session_id> 目录里查看 preview.json、HOA-001 和 HOA-002。
```

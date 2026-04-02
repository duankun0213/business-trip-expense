# WorkBuddy 同事使用说明

这份说明面向“最终使用者”，也就是只想在 WorkBuddy 里完成出差报销处理的同事。

## 一、先下载哪个包

### 1. 普通同事

默认下载：

`business-trip-expense-v1.1.0.zip`

它是当前推荐的正式安装包，已经对齐最新发布说明。

### 2. 想跟上最新云端能力的人

如果你要尽快用到当前云端服务的新能力，比如更多票据类型或图片票据支持，优先让管理员给你仓库 `main` 分支安装版，或者等下一版安装包。

### 3. 管理员或高级用户

下载：

`workbuddy-business-trip-expense-marketplace.zip`

它更适合团队统一分发、marketplace 管理或二次封装，不是给普通同事直接安装的首选。

## 二、使用前准备

开始前请先确认：

- 电脑已安装 WorkBuddy
- 电脑可以访问 `http://47.111.23.9`
- 真正处理报销时，电脑里有可用的 `python`

补充说明：

- 安装脚本本身不依赖 Python
- Python 只在真正执行 `/出差报销` 时需要

## 三、现在支持哪些报销材料

审批材料：

- 出差审批 PDF

票据材料：

- 火车票 PDF
- 机票 PDF
- 保险发票 PDF
- 酒店发票 PDF
- 地铁票 PDF
- 打车电子发票 PDF
- 打车电子行程单 PDF
- 出租车小票照片

票据支持格式：

- `.pdf`
- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.tiff`
- `.tif`
- `.webp`

## 四、审批单识别规则

系统会把审批 PDF 识别为审批单的条件是：

- 文件名中包含 `商旅` 或 `出差`
- 或它的直接父文件夹名中包含 `商旅` 或 `出差`

注意：

- 这里只看审批 PDF 本身和它的直接父文件夹
- 不要只依赖更上层目录名
- 其他支持文件会被当作发票、行程单或票据上传

## 五、文件夹应该怎么准备

把这次报销相关文件放到一个文件夹里，例如：

```text
C:\Users\你的用户名\Desktop\报销材料\test01
```

这个文件夹里通常会包含：

- 出差审批 PDF
- 火车票 PDF
- 机票或保险发票 PDF
- 酒店发票 PDF
- 打车电子发票 PDF
- 打车电子行程单 PDF
- 出租车纸质小票拍照图片

## 六、下载安装包

打开 GitHub Release 页面，下载：

`business-trip-expense-v1.1.0.zip`

下载后，把它解压到一个你容易找到的位置，例如：

```text
C:\Users\你的用户名\Downloads\business-trip-expense-v1.1.0
```

## 七、安装到 WorkBuddy

### 第一步：打开 PowerShell

进入刚才解压后的目录，例如：

```powershell
cd "C:\Users\你的用户名\Downloads\business-trip-expense-v1.1.0"
```

### 第二步：执行安装脚本

运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

安装成功后，它会把以下内容复制到你的用户目录：

- `~/.codebuddy/skills/business-trip-expense/`
- `~/.codebuddy/commands/出差报销.md`

注意：

- 这条命令必须在当前目录能看到 `.codebuddy` 和 `scripts` 时执行
- 如果你解压在 `D:` 盘，例如 `D:\business-trip-expense-v1.1.0`，可以这样执行：

```powershell
cd "D:\business-trip-expense-v1.1.0"
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

### 第三步：刷新 WorkBuddy

安装完成后：

- 重启 WorkBuddy

或

- 在 WorkBuddy 里执行 `/skills`

## 八、在 WorkBuddy 中怎么用

安装完成后，在 WorkBuddy 中直接输入：

```text
/出差报销 "C:\你的报销文件夹路径"
```

例如：

```text
/出差报销 "C:\Users\你的用户名\Desktop\报销材料\test01"
```

## 九、执行后会发生什么

WorkBuddy 会自动完成这些步骤：

1. 递归扫描你给的文件夹里的 PDF 和支持的图片文件
2. 自动区分审批单和发票或行程单
3. 调用远程报销 API 上传文件
4. 获取 `session_id`
5. 下载生成的报销结果文件

## 十、最终会得到什么文件

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

补充说明：

- 服务器还支持打包下载 `expense-files.zip`
- 当前 WorkBuddy 斜杠命令默认只下载 `preview.json`、`HOA-001` 和 `HOA-002`

## 十一、推荐的实际使用流程

给同事的最简单流程就是：

1. 从 GitHub Release 下载 `business-trip-expense-v1.1.0.zip`
2. 解压
3. 运行安装脚本
4. 重启 WorkBuddy
5. 准备一个放好审批 PDF、票据 PDF 和票据图片的文件夹
6. 在 WorkBuddy 里执行：

```text
/出差报销 "C:\你的文件夹路径"
```

7. 等待处理完成
8. 打开生成的 `expense-output-<session_id>` 目录查看结果

## 十二、常见问题

### 1. WorkBuddy 里找不到 `/出差报销`

处理方法：

- 重启 WorkBuddy
- 或执行 `/skills`
- 检查这两个路径是否存在：
  - `~/.codebuddy/commands/出差报销.md`
  - `~/.codebuddy/skills/business-trip-expense/`

### 2. 运行时报 `python` 找不到

说明：

- 这通常发生在真正执行 `/出差报销` 的时候，不是安装阶段
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
- 或确认审批单的直接父文件夹名中带 `商旅` 或 `出差`
- 不要只依赖更上层目录名

### 5. 下载哪个包最合适

普通同事：

- 下载 `business-trip-expense-v1.1.0.zip`

管理员或高级用户：

- 下载 `workbuddy-business-trip-expense-marketplace.zip`

### 6. 提示 `-ExecutionPolicy` 无法识别

这通常是因为命令前面少写了 `powershell`。

正确写法：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

错误写法：

```powershell
-ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

### 7. 我需要图片票据支持，应该怎么办

如果你需要尽快使用图片票据等较新的输入能力：

- 优先安装仓库 `main` 分支里的最新版本
- 或联系管理员获取下一版打包安装包

## 十三、一句话版发给同事

你可以直接把下面这段话发给同事：

```text
请到 GitHub Release 页面下载 business-trip-expense-v1.1.0.zip，解压后在 PowerShell 里执行：
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
然后重启 WorkBuddy。之后在 WorkBuddy 里输入：
/出差报销 "你的报销文件夹路径"
处理完成后，到原文件夹下的 expense-output-<session_id> 目录里查看 preview.json、HOA-001 和 HOA-002。
```

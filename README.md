# WorkBuddy Business Trip Expense

用于 WorkBuddy 的出差费用报销仓库模板。

## 仓库结构

```text
.codebuddy/
  commands/
    出差报销.md
  skills/
    business-trip-expense/
      SKILL.md
      scripts/
      references/
scripts/
  install-user.ps1
```

## 用法

### 方式 1：作为项目仓库使用

1. 克隆这个仓库
2. 用 WorkBuddy 打开仓库根目录
3. 执行：

```text
/出差报销 "C:\你的文件夹路径"
```

### 方式 2：安装到用户目录，全局使用

在仓库根目录执行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-user.ps1
```

安装后把下面两个文件复制到用户目录：

- `~/.codebuddy/skills/business-trip-expense/`
- `~/.codebuddy/commands/出差报销.md`

然后重启 WorkBuddy，或执行 `/skills` 刷新。

## 要求

- 本机可用 `python`
- 可以访问 `http://47.111.23.9`

## 说明

- `SKILL.md` 负责技能逻辑
- `/出差报销` 斜杠命令负责把文件夹路径交给技能处理
- 生成文件默认下载到传入文件夹下的 `expense-output-<session_id>` 目录

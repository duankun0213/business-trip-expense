[CmdletBinding()]
param(
    [string]$TargetHome = $HOME
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceSkill = Join-Path $repoRoot ".codebuddy\skills\business-trip-expense"
$sourceCommands = Join-Path $repoRoot ".codebuddy\commands"

$targetCodeBuddy = Join-Path $TargetHome ".codebuddy"
$targetSkill = Join-Path $targetCodeBuddy "skills\business-trip-expense"
$targetCommands = Join-Path $targetCodeBuddy "commands"

New-Item -ItemType Directory -Force -Path $targetSkill | Out-Null
New-Item -ItemType Directory -Force -Path $targetCommands | Out-Null

Copy-Item -Recurse -Force (Join-Path $sourceSkill "*") $targetSkill

$commandFiles = Get-ChildItem -LiteralPath $sourceCommands -File -Filter *.md
if (-not $commandFiles) {
    throw "No command markdown files found under: $sourceCommands"
}

foreach ($commandFile in $commandFiles) {
    $targetCommand = Join-Path $targetCommands $commandFile.Name
    Copy-Item -LiteralPath $commandFile.FullName -Destination $targetCommand -Force
    Write-Output "Installed command to: $targetCommand"
}

Write-Output "Installed skill to: $targetSkill"
Write-Output "Restart WorkBuddy or run /skills to refresh commands and skills."

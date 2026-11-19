# Compacts Docker Desktop's WSL2 data disk so freed space returns to Windows. Quit Docker Desktop first.
param(
    [string]$VhdxPath = "$env:LOCALAPPDATA\Docker\wsl\disk\docker_data.vhdx"
)

if (-not (Test-Path $VhdxPath)) {
    Write-Host "VHDX not found at $VhdxPath. Pass the real path with -VhdxPath." -ForegroundColor Red
    return
}

function Get-VhdxSizeGb { [math]::Round((Get-Item $VhdxPath).Length / 1GB, 2) }

if (Get-Process -Name 'Docker Desktop' -ErrorAction SilentlyContinue) {
    Write-Host 'Docker Desktop is still running. Quit it from the tray icon, then run again.' -ForegroundColor Yellow
    return
}

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    $sizeBeforeGb = Get-VhdxSizeGb
    Start-Process powershell -Verb RunAs -Wait -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" -VhdxPath `"$VhdxPath`""
    Write-Host "VHDX: $sizeBeforeGb GB -> $(Get-VhdxSizeGb) GB" -ForegroundColor Green
    return
}

wsl --shutdown
Start-Service vds -ErrorAction SilentlyContinue

$diskpartScriptPath = Join-Path $env:TEMP 'docker_reclaim_diskpart.txt'
@"
select vdisk file="$VhdxPath"
attach vdisk readonly
compact vdisk
detach vdisk
exit
"@ | Set-Content -Path $diskpartScriptPath -Encoding ascii

diskpart /s $diskpartScriptPath

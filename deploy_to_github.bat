@echo off
REM 🚀 AI Chef Assistant - GitHub 快速部屬腳本
REM 使用方法: 雙擊此文件運行

echo.
echo ======================================
echo 🚀 AI Chef Assistant - GitHub 部屬
echo ======================================
echo.

REM 檢查 Git 安裝
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git 未安裝！
    echo 請訪問: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git 已安裝

REM 檢查是否在項目目錄
if not exist "smart_chef_advisor_v2.py" (
    echo ❌ 請在項目根目錄運行此腳本
    pause
    exit /b 1
)

echo ✅ 項目目錄正確

REM 檢查是否已初始化
if not exist ".git" (
    echo 初始化 Git 倉库...
    git init
    echo ✅ Git 倉库已初始化
) else (
    echo ✅ Git 倉库已存在
)

REM 配置 Git 用戶（如果需要）
echo.
echo 配置 Git 用戶信息...
set /p username="輸入 GitHub 用戶名 (或按 Enter 跳過): "
if not "%username%"=="" (
    git config user.name "%username%"
)

set /p email="輸入郵箱地址 (或按 Enter 跳過): "
if not "%email%"=="" (
    git config user.email "%email%"
)

REM 添加所有文件
echo.
echo 添加所有文件...
git add .
echo ✅ 文件已添加

REM 顯示待提交的文件
echo.
echo 📋 待提交的文件:
git status --short
echo.

REM 創建提交
set /p message="輸入提交信息 (默認: Initial commit): "
if "%message%"=="" (
    set message=Initial commit: AI Chef Assistant
)

git commit -m "%message%"
echo ✅ 提交已創建

REM 提示下一步
echo.
echo ======================================
echo ✅ 本地部分完成！
echo ======================================
echo.
echo 🔗 下一步:
echo 1. 在 GitHub 創建新倉库: https://github.com/new
echo 2. 複製倉库 URL (HTTPS 或 SSH)
echo 3. 運行以下命令:
echo.
echo    git remote add origin 你的_倉库_URL
echo    git branch -M main
echo    git push -u origin main
echo.
echo ======================================
echo.
pause

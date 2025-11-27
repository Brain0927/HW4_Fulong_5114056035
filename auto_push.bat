@echo off
REM 🚀 AI Chef Assistant - 完整推送腳本
REM 自動安裝 Git 並推送到 GitHub

chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ════════════════════════════════════════════════════════
echo 🚀 自動推送到 GitHub - AI Chef Assistant
echo ════════════════════════════════════════════════════════
echo.

REM 檢查是否在項目目錄
if not exist "smart_chef_advisor_v2.py" (
    echo ❌ 錯誤: 請在項目根目錄運行此腳本
    pause
    exit /b 1
)

REM 檢查 Git
git --version >nul 2>&1
if errorlevel 1 (
    echo ⏳ 正在安裝 Git...
    echo.
    echo 方法 1: 嘗試使用 winget
    winget install Git.Git --accept-source-agreements --accept-package-agreements
    
    REM 重新檢查
    git --version >nul 2>&1
    if errorlevel 1 (
        echo.
        echo ❌ Git 安裝失敗或未完成
        echo 請訪問: https://git-scm.com/download/win
        echo 手動下載並安裝 Git
        pause
        exit /b 1
    )
)

echo ✅ Git 已安裝

REM 進入項目目錄
cd /d "D:\00_student\02_AIOT\Homework_4"

REM 初始化 Git（如果需要）
if not exist ".git" (
    echo.
    echo 初始化 Git 倉庫...
    git init
    git config user.name "Brain0927"
    git config user.email "student@example.com"
    echo ✅ Git 倉庫已初始化
) else (
    echo ✅ Git 倉庫已存在
)

REM 檢查遠程倉庫
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo.
    echo 添加遠程倉庫...
    git remote add origin https://github.com/Brain0927/HW4_Fulong_5114056035.git
)

REM 添加文件
echo.
echo 添加所有文件...
git add .
echo ✅ 文件已添加

REM 檢查是否有待提交的文件
git status --short | findstr . >nul
if errorlevel 1 (
    echo ⚠️ 沒有待提交的文件
) else (
    echo.
    echo 待提交的文件:
    git status --short
    
    REM 創建提交
    echo.
    echo 創建提交...
    git commit -m "🎉 Initial commit: AI Chef Assistant v1.0

- Streamlit-based cooking assistant
- Features: AI chat, recipe generation
- Support for Google Gemini and OpenAI APIs
- Responsive UI with Chinese/English interface"
)

REM 設置分支並推送
echo.
echo ════════════════════════════════════════════════════════
echo 準備推送到 GitHub...
echo 倉庫: https://github.com/Brain0927/HW4_Fulong_5114056035
echo ════════════════════════════════════════════════════════
echo.

git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ 推送失敗
    echo.
    echo 可能原因:
    echo 1. 網絡連接問題
    echo 2. 認證失敗 - 需要輸入認證信息
    echo 3. 倉庫不存在或沒有推送權限
    echo.
    echo 解決方案:
    echo 1. 檢查網絡連接
    echo 2. 使用 Personal Access Token (推薦)
    echo    https://github.com/settings/tokens
    echo 3. 確認倉庫存在: https://github.com/Brain0927/HW4_Fulong_5114056035
    echo.
    echo 重試命令:
    echo   git push -u origin main
) else (
    echo.
    echo ════════════════════════════════════════════════════════
    echo ✅ 推送成功！
    echo ════════════════════════════════════════════════════════
    echo.
    echo 查看你的倉庫:
    echo https://github.com/Brain0927/HW4_Fulong_5114056035
    echo.
    echo 已上傳的文件:
    echo   ✅ smart_chef_advisor_v2.py
    echo   ✅ ai_chef_functions.py
    echo   ✅ README.md
    echo   ✅ 所有文檔和配置
)

echo.
pause

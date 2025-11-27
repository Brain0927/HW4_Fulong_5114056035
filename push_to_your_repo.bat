@echo off
REM 🚀 推送到 GitHub 倉庫
REM 倉庫: https://github.com/Brain0927/HW4_Fulong_5114056035.git

chcp 65001 >nul
echo.
echo ════════════════════════════════════════════════════════
echo 🚀 推送 AI Chef Assistant 到你的 GitHub 倉庫
echo ════════════════════════════════════════════════════════
echo.

REM 檢查 Git
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git 未安裝
    echo 請訪問: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo ✅ Git 已安裝

REM 進入項目目錄
if not exist "smart_chef_advisor_v2.py" (
    echo ❌ 請在項目根目錄運行此腳本
    pause
    exit /b 1
)
echo ✅ 項目目錄正確

REM 初始化 Git（如果需要）
if not exist ".git" (
    echo.
    echo 初始化 Git 倉庫...
    git init
    git config user.name "Brain0927"
    git config user.email "student@example.com"
    echo ✅ Git 倉庫已初始化
)

REM 添加文件
echo.
echo 添加所有文件...
git add .
echo ✅ 文件已添加

REM 創建提交
echo.
echo 創建提交...
git commit -m "🎉 Initial commit: AI Chef Assistant v1.0

- Streamlit-based cooking assistant
- Features: AI chat, recipe generation
- Support for Google Gemini and OpenAI APIs
- Responsive UI with Chinese/English interface"

REM 設置遠程倉庫
echo.
echo 設置遠程倉庫...
git remote remove origin 2>nul
git remote add origin https://github.com/Brain0927/HW4_Fulong_5114056035.git
echo ✅ 遠程倉庫已設置

REM 推送
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
    echo 可能原因:
    echo 1. 網絡連接問題
    echo 2. 認證失敗 - 使用 Personal Access Token
    echo 3. 倉庫不存在或沒有推送權限
    echo.
    echo Personal Access Token 生成:
    echo https://github.com/settings/tokens
) else (
    echo.
    echo ════════════════════════════════════════════════════════
    echo ✅ 推送成功！
    echo ════════════════════════════════════════════════════════
    echo.
    echo 查看倉庫:
    echo https://github.com/Brain0927/HW4_Fulong_5114056035
)

pause

# 🚀 推送到你的 GitHub 倉庫

## 你的倉庫信息
- **倉庫 URL**: https://github.com/Brain0927/HW4_Fulong_5114056035.git
- **項目**: AI Chef Assistant
- **用戶**: Brain0927

---

## ⚡ 快速推送指南

### 步驟 1: 安裝 Git（必須）
1. 訪問: https://git-scm.com/download/win
2. 下載並安裝（一直點 Next）
3. 驗證安裝: `git --version`

### 步驟 2: 配置 Git 用戶
```bash
git config --global user.name "Brain0927"
git config --global user.email "your_email@example.com"
```

### 步驟 3: 初始化並推送

在項目目錄運行:
```bash
cd D:\00_student\02_AIOT\Homework_4

# 初始化 Git
git init

# 添加所有文件
git add .

# 創建首次提交
git commit -m "🎉 Initial commit: AI Chef Assistant v1.0

- Streamlit-based cooking assistant
- Features: AI chat, recipe generation
- Support for Google Gemini and OpenAI APIs"

# 添加遠程倉庫（替換為你的倉庫）
git remote add origin https://github.com/Brain0927/HW4_Fulong_5114056035.git

# 設置主分支並推送
git branch -M main
git push -u origin main
```

### 步驟 4: 輸入憑證
- **用戶名**: Brain0927
- **密碼**: 輸入你的 GitHub Personal Access Token
  或直接使用 GitHub 密碼（推薦使用 Personal Access Token）

---

## 生成 Personal Access Token（推薦）

1. 訪問: https://github.com/settings/tokens
2. 點擊 "Generate new token"
3. 選擇 "repo" 和 "workflow" 權限
4. 複製生成的 token
5. 在推送時粘貼該 token（作為密碼）

---

## 推送後驗證

訪問你的倉庫驗證:
```
https://github.com/Brain0927/HW4_Fulong_5114056035
```

你應該看到:
- ✅ README.md
- ✅ smart_chef_advisor_v2.py
- ✅ ai_chef_functions.py
- ✅ 其他所有文件

---

## 常用命令

```bash
# 查看狀態
git status

# 查看遠程配置
git remote -v

# 查看提交歷史
git log --oneline

# 推送更新
git add .
git commit -m "Your message"
git push
```

---

## 🆘 常見問題

### Git 不被識別
- 重啟 PowerShell 或 CMD
- 確認已安裝 Git 並重啟系統

### 認證失敗
- 使用 Personal Access Token（推薦）
- 檢查用戶名是否正確: `Brain0927`
- 確認網絡連接

### 倉庫已存在
```bash
git remote remove origin
git remote add origin https://github.com/Brain0927/HW4_Fulong_5114056035.git
git push -u origin main
```

---

## 📝 完整命令一次性複製

```bash
cd D:\00_student\02_AIOT\Homework_4
git init
git config user.name "Brain0927"
git config user.email "your_email@example.com"
git add .
git commit -m "🎉 Initial commit: AI Chef Assistant v1.0"
git remote add origin https://github.com/Brain0927/HW4_Fulong_5114056035.git
git branch -M main
git push -u origin main
```

---

**準備好了嗎？安裝 Git 後執行上面的命令就能推送了！** 🚀

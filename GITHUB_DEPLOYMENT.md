# 🚀 GitHub 部屬指南 - AI Chef Assistant

本指南將幫助你將 **AI Chef Assistant** 項目部屬到 GitHub。

---

## 📋 前置準備

### 1. 安裝必需工具

**Git 安裝**
- Windows: 下載並安裝 [Git for Windows](https://git-scm.com/download/win)
- macOS: `brew install git`
- Linux: `sudo apt-get install git`

**驗證安裝**
```bash
git --version
```

### 2. 創建 GitHub 賬戶
如果還沒有 GitHub 賬戶：
1. 訪問 https://github.com
2. 點擊「Sign up」
3. 完成註冊流程

### 3. 生成 SSH 金鑰（推薦）
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
按 Enter 接受所有默認選項，然後在 GitHub 設置中添加公鑰。

---

## 🔧 部屬步驟

### 步驟 1: 初始化 Git 仓库

在項目目錄運行：
```bash
cd D:\00_student\02_AIOT\Homework_4
git init
```

### 步驟 2: 配置 Git 用戶信息

```bash
git config user.name "Your Name"
git config user.email "your_email@example.com"
```

### 步驟 3: 添加所有文件到暫存區

```bash
git add .
```

驗證添加的文件：
```bash
git status
```

你應該看到：
```
Changes to be committed:
  new file:   README.md
  new file:   SUMMARY.md
  new file:   smart_chef_advisor_v2.py
  new file:   ai_chef_functions.py
  new file:   requirements.txt
  new file:   .gitignore
  new file:   .env
```

### 步驟 4: 創建初始提交

```bash
git commit -m "🎉 Initial commit: AI Chef Assistant application"
```

### 步驟 5: 在 GitHub 創建新倉库

1. 訪問 https://github.com/new
2. 填寫倉库信息：
   - **Repository name**: `AI-Chef-Assistant` 或 `ai-chef-assistant`
   - **Description**: `🤖 A Streamlit-based AI cooking assistant with chat and recipe generation`
   - **Visibility**: Public（公開）或 Private（私有）
3. 點擊「Create repository」

### 步驟 6: 添加遠程倉库

將本地倉库連接到 GitHub：

```bash
git remote add origin https://github.com/YOUR_USERNAME/AI-Chef-Assistant.git
```

或使用 SSH（如果配置了 SSH 金鑰）：
```bash
git remote add origin git@github.com:YOUR_USERNAME/AI-Chef-Assistant.git
```

### 步驟 7: 推送到 GitHub

```bash
git branch -M main
git push -u origin main
```

首次推送時可能需要輸入 GitHub 密碼或使用 Personal Access Token。

---

## ✅ 驗證部屬成功

1. 訪問你的 GitHub 倉库：`https://github.com/YOUR_USERNAME/AI-Chef-Assistant`
2. 確認所有文件都已上傳
3. README.md 應該在主頁顯示

---

## 📝 重要注意事項

### .env 文件安全

⚠️ **重要**: `.env` 文件包含 API Key，不應公開！

檢查你的 `.gitignore` 文件是否包含：
```
.env
.env.local
*.env
```

如果 `.env` 已經被上傳，立即執行：
```bash
git rm --cached .env
git commit -m "Remove .env from tracking"
git push
```

### 創建 .env.example 文件

為了幫助其他開發者，創建一個 `.env.example` 文件：

```bash
# .env.example
GEMINI_API_KEY=your_api_key_here
OPENAI_API_KEY=your_api_key_here
```

這樣新用戶可以複製這個文件作為模板。

---

## 🔄 日常使用命令

### 提交更改

```bash
# 查看改動
git status

# 添加文件
git add .

# 提交
git commit -m "Your commit message"

# 推送到 GitHub
git push
```

### 拉取更改

```bash
git pull
```

### 查看提交歷史

```bash
git log --oneline
```

---

## 🎯 建議的第一次提交信息

```bash
git commit -m "🎉 Initial commit: AI Chef Assistant v1.0

- Streamlit-based cooking assistant application
- Features: AI chat, recipe generation
- Support for Google Gemini and OpenAI APIs
- Responsive UI with mixed Chinese/English interface
- Complete documentation (README.md, SUMMARY.md)"
```

---

## 📚 後續操作

### 1. 添加協作者

1. 進入倉库 Settings
2. 點擊 Collaborators
3. 添加團隊成員的 GitHub 用戶名

### 2. 設置 Branch Protection

1. 進入 Settings → Branches
2. 添加保護規則以防止意外刪除

### 3. 設置 GitHub Actions（CI/CD）

創建 `.github/workflows/test.yml` 進行自動化測試：

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - run: pip install -r requirements.txt
      - run: python -m streamlit run smart_chef_advisor_v2.py --logger.level=debug
```

---

## 🆘 常見問題

### Q: 如何更新我的倉库？
**A**: 
```bash
git add .
git commit -m "Update: description"
git push
```

### Q: 如何撤銷最後一次提交？
**A**: 
```bash
git reset --soft HEAD~1
```

### Q: 如何克隆我的倉库到另一台電腦？
**A**: 
```bash
git clone https://github.com/YOUR_USERNAME/AI-Chef-Assistant.git
cd AI-Chef-Assistant
```

### Q: 我不小心上傳了 .env，怎麼辦？
**A**: 
```bash
git rm --cached .env
git commit -m "Remove .env from version control"
git push
```

然後立即更新你的 API Key！

---

## 📌 倉库結構示例

你的 GitHub 倉库應該看起來像這樣：

```
AI-Chef-Assistant/
├── README.md                    # 使用指南
├── SUMMARY.md                   # 技術總結
├── smart_chef_advisor_v2.py     # 主應用
├── ai_chef_functions.py         # AI 模塊
├── requirements.txt             # 依賴
├── .env                         # 環境變數（不應公開）
├── .gitignore                   # Git 忽略規則
├── .github/
│   └── workflows/
│       └── test.yml             # CI/CD 配置（可選）
└── docs/                        # 額外文檔（可選）
```

---

## 🎨 README 徽章（可選）

在 README.md 頂部添加徽章以展示項目狀態：

```markdown
# AI Chef Assistant

[![GitHub](https://img.shields.io/badge/GitHub-AI--Chef--Assistant-blue?logo=github)](https://github.com/YOUR_USERNAME/AI-Chef-Assistant)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
```

---

## 📞 需要幫助？

- GitHub 官方文檔: https://docs.github.com
- Git 官方文檔: https://git-scm.com/doc
- Streamlit 部屬指南: https://docs.streamlit.io/deploy

---

**祝你部屬順利！🚀**

最後更新: 2025 年 11 月 27 日

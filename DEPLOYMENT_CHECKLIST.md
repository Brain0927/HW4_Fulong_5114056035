# ✅ GitHub 部屬清單

## 📋 部屬前的準備

- [ ] 已安裝 Git：`git --version`
- [ ] 已創建 GitHub 賬戶
- [ ] 已生成 SSH 金鑰（可選但推薦）
- [ ] `.env` 文件已配置 API Key
- [ ] `.gitignore` 包含 `.env`（已配置 ✅）

## 🚀 部屬步驟（選擇一種方式）

### 方式 A: 使用快速部屬腳本（推薦）

#### Windows
```
1. 打開文件管理器
2. 導航到: D:\00_student\02_AIOT\Homework_4
3. 雙擊 deploy_to_github.bat
4. 按照提示完成
```

### 方式 B: 手動部屬

#### 第一次部屬

```bash
# 1. 進入項目目錄
cd D:\00_student\02_AIOT\Homework_4

# 2. 初始化 Git（如果還沒初始化）
git init

# 3. 配置用戶信息
git config user.name "Your Name"
git config user.email "your_email@example.com"

# 4. 添加所有文件
git add .

# 5. 創建初始提交
git commit -m "🎉 Initial commit: AI Chef Assistant v1.0"

# 6. 添加遠程倉库（替換 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/AI-Chef-Assistant.git

# 7. 推送到 GitHub
git branch -M main
git push -u origin main
```

#### 後續更新

```bash
# 每次修改後執行以下命令
git add .
git commit -m "Your commit message"
git push
```

## 🔗 GitHub 倉库設置

### 創建新倉库
1. 訪問：https://github.com/new
2. 填寫信息：
   - Name: `AI-Chef-Assistant`
   - Description: `🤖 A Streamlit-based AI cooking assistant`
   - Visibility: `Public` 或 `Private`
3. 點擊 "Create repository"
4. 複製倉库 URL

## ✨ 完成後

- [ ] 所有文件已上傳到 GitHub
- [ ] 倉库 URL：`https://github.com/YOUR_USERNAME/AI-Chef-Assistant`
- [ ] README.md 在主頁顯示
- [ ] 可以邀請協作者
- [ ] 可以設置 GitHub Pages（可選）

## 📚 文檔參考

| 文件 | 說明 |
|------|------|
| `README.md` | 項目使用指南 |
| `SUMMARY.md` | 技術總結 |
| `GITHUB_DEPLOYMENT.md` | GitHub 部屬完整指南 |
| `deploy_to_github.bat` | Windows 快速部屬腳本 |

## 🆘 遇到問題？

### Git 命令常用

```bash
# 查看狀態
git status

# 查看提交歷史
git log --oneline

# 撤銷最後一次提交
git reset --soft HEAD~1

# 刪除未追蹤的文件
git clean -fd

# 克隆倉库到本地
git clone https://github.com/YOUR_USERNAME/AI-Chef-Assistant.git
```

### 常見問題

**Q: 我的 Git 不能連接到 GitHub**
A: 
- 檢查網絡連接
- 確認 SSH/HTTPS 配置正確
- 檢查防火牆設置

**Q: 我不小心提交了 .env**
A:
```bash
git rm --cached .env
git commit -m "Remove .env"
git push
# 然後立即重置 API Key
```

**Q: 我想更改倉库名稱**
A: 在 GitHub Settings 中修改，然後更新本地：
```bash
git remote set-url origin 新URL
```

## 📞 更多幫助

- GitHub 文檔：https://docs.github.com
- Git 教程：https://git-scm.com/book
- Streamlit 部屬：https://docs.streamlit.io/deploy

---

✅ **準備好了嗎？開始部屬吧！**

建議: 部屬前先備份你的 API Key！

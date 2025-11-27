# 🤖 AI Chef Assistant

一個由 Streamlit 驅動的智能廚師助手應用，集成 AI 對話和食譜生成功能。

## ✨ 功能特性

### 1. 💬 AI Chef Assistant（AI 廚師助手）
- **智能對話**: 與 AI 廚師實時對話，解答任何烹飪相關問題
- **快速提示**: 預設三個常見問題按鈕，一鍵獲取回答
  - 🍳 How to make tomato and egg stir-fry?
  - 🔥 Cooking Heat Techniques
  - 🥗 Nutrition Pairing Tips
- **對話歷史**: 完整保存對話記錄，隨時查看
- **清空功能**: 一鍵清空對話歷史，開始新對話

### 2. ✨ Recipe Generator（食譜生成）
- **智能生成**: 輸入菜名自動生成完整食譜
- **參數自定義**:
  - 難度等級（簡單/中等/困難）
  - 烹飪時間（5-180 分鐘）
  - 份量（1-10 人份）
  - 可用食材（自由組合）
- **詳細信息**: 顯示材料、步驟、烹飪技巧
- **JSON 導出**: 支持查看完整 JSON 格式的食譜

## 🛠️ 技術棧

- **前端框架**: Streamlit 1.35.0
- **AI 服務**:
  - Google Gemini API（推薦，免費額度充足）
  - OpenAI API（可選）
- **環境管理**: python-dotenv 1.0.0
- **Python 版本**: 3.8+

## 📋 前置要求

### 必需的依賴
```bash
pip install streamlit==1.35.0
pip install google-generativeai==0.3.0
pip install python-dotenv==1.0.0
pip install openai==1.6.1  # 可選
```

### API Key 配置
在項目根目錄創建 `.env` 文件：

**選項 1: 使用 Google Gemini API（推薦）**
```
GEMINI_API_KEY=你的_Gemini_API_Key
```

**選項 2: 使用 OpenAI API**
```
OPENAI_API_KEY=你的_OpenAI_API_Key
```

> 獲取 Gemini API Key: https://makersuite.google.com/app/apikey
> 
> 獲取 OpenAI API Key: https://platform.openai.com/api-keys

## 🚀 快速開始

### 1. 克隆或下載項目
```bash
cd Homework_4
```

### 2. 安裝依賴
```bash
pip install -r requirements.txt
```

### 3. 配置 API Key
編輯 `.env` 文件，添加你的 API Key

### 4. 運行應用
```bash
streamlit run smart_chef_advisor_v2.py
```

應用將在默認瀏覽器中打開：http://localhost:8501

## 🌐 GitHub 部屬

### 快速部屬（Windows）
1. 雙擊 `deploy_to_github.bat` 文件
2. 按照提示完成部屬

### 完整部屬指南
詳見 [`GITHUB_DEPLOYMENT.md`](GITHUB_DEPLOYMENT.md) 文件，包含：
- ✅ 詳細的分步指南
- ✅ Git 命令詳解
- ✅ 常見問題解答
- ✅ 安全建議

## 📁 項目結構

```
Homework_4/
├── smart_chef_advisor_v2.py    # 主應用文件
├── ai_chef_functions.py         # AI 功能模塊
├── requirements.txt             # 依賴列表
├── .env                         # 環境變數配置（需自行創建）
├── README.md                    # 項目文檔
└── SUMMARY.md                   # 項目總結
```

## 🎯 使用指南

### AI 廚師助手
1. 在左側輸入框輸入烹飪問題
2. 點擊「📤 發送」按鈕
3. 查看 AI 的回答
4. 使用「🗑️ 清空」按鈕清除對話歷史

**快速提示使用**:
直接點擊預設按鈕，快速提交常見問題

### 食譜生成器
1. 輸入菜名（例如：番茄湯）
2. 調整難度、時間、份量
3. （可選）輸入可用食材
4. 點擊「🚀 生成食譜」
5. 查看完整的食譜信息

## 🔧 自定義配置

### 修改快速提示按鈕
編輯 `smart_chef_advisor_v2.py` 中的第 160-200 行，修改按鈕文本和提示內容。

### 調整 UI 樣式
修改 CSS 部分（第 30-50 行）來改變顏色、大小等視覺效果。

### 修改 Tab 標籤大小
在 CSS 中調整：
```css
button[data-baseweb="tab"] {
    font-size: 18px !important;
    font-weight: bold !important;
    padding: 15px 30px !important;
}
```

## 💡 常見問題

### Q: 應用顯示 "AI 功能未啟用"
**A**: 確保 `.env` 文件正確配置了 API Key，然後重啟應用。

### Q: AI 回答很慢
**A**: 這是正常的。首次調用可能需要 5-10 秒，後續會加快。

### Q: 如何切換 AI 服務？
**A**: 修改 `.env` 文件中的 API Key，應用會自動檢測可用的服務。

### Q: 對話框為空怎麼辦？
**A**: 檢查 API Key 是否有效，或查看控制台是否有錯誤信息。

## 🎨 特色功能

### 智能加載動畫
- 顯示 "💬 AI Chef Assistant 🤖🤖🤖 Thinking..."
- 用戶能清楚看到應用正在處理

### 錯誤處理
- 所有 API 調用都有 try-except 保護
- 錯誤信息直接顯示在聊天窗口

### 響應式設計
- 寬度自適應
- 支持所有屏幕尺寸

## 📊 應用信息

- **版本**: 1.0 (AI Chef Assistant + Recipe Generator)
- **開發框架**: Streamlit
- **AI 服務**: Google Gemini / OpenAI
- **語言**: 混合中英文（導航中文，提示英文）

## ⚙️ 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| GEMINI_API_KEY | Google Gemini API 密鑰 | 二選一 |
| OPENAI_API_KEY | OpenAI API 密鑰 | 二選一 |

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📝 許可證

本項目採用 MIT 許可證。

## 👨‍💻 開發者

由 AI 驅動的廚師助手應用 • 2025

---

**提示**: 首次使用前，請確保已配置 API Key 並安裝所有依賴！

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速測試 Gemini API 連接
"""

import os
from dotenv import load_dotenv

# 強制加載 .env
load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

print("=" * 60)
print("🔍 Gemini API 快速測試")
print("=" * 60)

if not api_key:
    print("❌ API Key 未設置！")
    print("請在 .env 文件中設置 GEMINI_API_KEY")
    exit(1)

print(f"\n✅ API Key 已讀取 (首 15 字: {api_key[:15]}...)")

# 測試連接
try:
    print("\n⏳ 測試 Gemini 連接...")
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    
    # 使用最新的 Gemini 2.5 Flash 模型
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Say 你好 in one word")
    
    print(f"✅ 連接成功！")
    print(f"📝 回應: {response.text}")
    print("\n✅ Gemini API 工作正常，應用應該可以運行了！")
    
except Exception as e:
    print(f"❌ 連接失敗: {str(e)}")
    print("\n💡 解決方案：")
    print("1. 檢查 API Key 是否正確")
    print("2. 檢查網路連接")
    print("3. 訪問 https://ai.google.dev 檢查服務狀態")
    exit(1)

print("\n" + "=" * 60)

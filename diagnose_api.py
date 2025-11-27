#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Chef Assistant - API 診斷工具
用於檢測 Gemini 和 OpenAI API 的連接狀態
"""

import os
import sys
from dotenv import load_dotenv

# 加載環境變量
load_dotenv()

print("=" * 60)
print("🔍 AI Chef Assistant - API 診斷工具")
print("=" * 60)

# 1. 檢查 API Keys
print("\n📋 Step 1: 檢查 API Keys 配置")
print("-" * 60)

openai_key = os.getenv("OPENAI_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

if openai_key:
    print(f"✅ OpenAI API Key: 已設置 (首 10 字: {openai_key[:10]}...)")
else:
    print("❌ OpenAI API Key: 未設置")

if gemini_key:
    print(f"✅ Gemini API Key: 已設置 (首 10 字: {gemini_key[:10]}...)")
else:
    print("❌ Gemini API Key: 未設置")

# 2. 檢查 Python 包
print("\n📦 Step 2: 檢查必要的 Python 包")
print("-" * 60)

packages_to_check = {
    'google.generativeai': 'Google Generative AI',
    'openai': 'OpenAI',
    'streamlit': 'Streamlit',
    'dotenv': 'python-dotenv'
}

for package, display_name in packages_to_check.items():
    try:
        __import__(package)
        print(f"✅ {display_name}: 已安裝")
    except ImportError:
        print(f"❌ {display_name}: 未安裝 (運行: pip install {package})")

# 3. 測試 Gemini 連接
print("\n🤖 Step 3: 測試 Gemini API 連接")
print("-" * 60)

if gemini_key:
    try:
        import google.generativeai as genai
        
        genai.configure(api_key=gemini_key)
        
        print("⏳ 測試連接中...")
        
        # 列出可用模型
        models = genai.list_models()
        available_models = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
        
        if available_models:
            print(f"✅ Gemini API 連接成功！")
            print(f"\n可用的生成模型:")
            for model in available_models:
                print(f"  - {model}")
            
            # 嘗試簡單的生成測試
            print("\n⏳ 嘗試簡單的文本生成...")
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content("Say hello in Traditional Chinese")
                print(f"✅ 生成測試成功！")
                print(f"   回應: {response.text[:100]}")
            except Exception as e:
                print(f"⚠️  生成測試失敗: {str(e)}")
        else:
            print("❌ 沒有找到可用的 Gemini 模型")
            
    except Exception as e:
        print(f"❌ Gemini API 連接失敗: {str(e)}")
else:
    print("⚠️  Gemini API Key 未設置，跳過測試")

# 4. 測試 OpenAI 連接
print("\n🤖 Step 4: 測試 OpenAI API 連接")
print("-" * 60)

if openai_key:
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=openai_key)
        
        print("⏳ 測試連接中...")
        
        # 嘗試簡單的對話
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": "Say hello in Traditional Chinese"}
                ],
                max_tokens=50
            )
            print(f"✅ OpenAI API 連接成功！")
            print(f"   回應: {response.choices[0].message.content[:100]}")
        except Exception as e:
            print(f"❌ OpenAI API 呼叫失敗: {str(e)}")
            
    except Exception as e:
        print(f"❌ OpenAI API 連接失敗: {str(e)}")
else:
    print("⚠️  OpenAI API Key 未設置，跳過測試")

# 5. 推薦操作
print("\n" + "=" * 60)
print("💡 推薦操作")
print("=" * 60)

if not gemini_key and not openai_key:
    print("\n❌ 兩個 API Key 都未設置！")
    print("\n請選擇以下方式之一：")
    print("\n方式 1: 使用 Google Gemini API (免費)")
    print("  1. 訪問 https://ai.google.dev/")
    print("  2. 點擊 'Get API Key' 按鈕")
    print("  3. 複製 API Key")
    print("  4. 在 .env 文件中添加: GEMINI_API_KEY=your_key_here")
    print("\n方式 2: 使用 OpenAI API (付費)")
    print("  1. 訪問 https://platform.openai.com/api-keys")
    print("  2. 複製 API Key")
    print("  3. 在 .env 文件中添加: OPENAI_API_KEY=your_key_here")
elif gemini_key and not openai_key:
    print("\n✅ Gemini API Key 已設置")
    print("\n若 Gemini 仍然無法連接：")
    print("  1. 驗證 API Key 是否正確複製")
    print("  2. 檢查網路連接")
    print("  3. 訪問 https://ai.google.dev/ 檢查 API 狀態")
    print("  4. 嘗試添加 OpenAI API Key 作為備選")
else:
    print("\n✅ API Key 已配置")
    print("應用應該可以正常工作")

print("\n" + "=" * 60)
print("診斷完成！")
print("=" * 60)

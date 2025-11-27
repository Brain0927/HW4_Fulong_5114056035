#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
直接測試提供的 Gemini API Key
"""

api_key = "AIzaSyD7iPPJfbZ3dkw9_rO-WfQW6jt3qLh9_CE"

print("=" * 60)
print("🔍 測試 Gemini API Key")
print("=" * 60)
print(f"\n✅ API Key: {api_key[:15]}...{api_key[-5:]}")

try:
    import google.generativeai as genai
    
    print("\n⏳ 配置 Gemini...")
    genai.configure(api_key=api_key)
    
    # 列出可用模型
    print("⏳ 列出可用模型...")
    models = genai.list_models()
    available_models = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
    
    print(f"\n✅ 找到 {len(available_models)} 個可用模型")
    print("\n前 10 個可用模型:")
    for i, model in enumerate(available_models[:10], 1):
        print(f"  {i}. {model}")
    
    # 測試最新的模型
    print("\n⏳ 測試 gemini-2.5-flash 模型...")
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content("Say '你好' (Hello in Traditional Chinese)")
    
    print(f"✅ API 連接成功！")
    print(f"\n📝 測試回應:")
    print(f"   {response.text}")
    
    print("\n" + "=" * 60)
    print("✅ API Key 有效！應用應該可以正常運行")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ 錯誤: {str(e)}")
    print("\n" + "=" * 60)
    print("💡 故障排查:")
    print("1. 檢查 API Key 是否正確複製")
    print("2. 檢查網路連接")
    print("3. 訪問 https://ai.google.dev 檢查 API 狀態")
    print("=" * 60)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Streamlit 應用啟動腳本（帶緩存清理）
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

print("=" * 60)
print("🚀 AI Chef Assistant - 應用啟動")
print("=" * 60)

# 獲取腳本所在目錄
app_dir = Path(__file__).parent
streamlit_cache = app_dir / ".streamlit" / "cache"

# 清理 Streamlit 緩存
print("\n🧹 清理 Streamlit 緩存...")
if streamlit_cache.exists():
    try:
        shutil.rmtree(streamlit_cache)
        print(f"✅ 已清理: {streamlit_cache}")
    except Exception as e:
        print(f"⚠️  無法完全清理: {e}")
else:
    print("✅ 無需清理")

# 檢查 .env 文件
env_file = app_dir / ".env"
if not env_file.exists():
    print("⚠️  警告: .env 文件不存在")
else:
    print(f"✅ .env 文件: {env_file}")

# 檢查必要的文件
print("\n📂 檢查必要文件...")
required_files = ["app.py", "ai_chef_functions.py", ".env"]
for filename in required_files:
    filepath = app_dir / filename
    if filepath.exists():
        print(f"✅ {filename}")
    else:
        print(f"❌ {filename} - 缺失")

# 啟動 Streamlit
print("\n" + "=" * 60)
print("🎬 正在啟動 Streamlit 應用...")
print("=" * 60)
print("\n💡 應用將在您的瀏覽器中打開")
print("   如果沒有自動打開，訪問: http://localhost:8501\n")

os.chdir(app_dir)
subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py", "--logger.level=debug"])

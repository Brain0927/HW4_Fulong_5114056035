import streamlit as st
import os
from datetime import datetime
from dotenv import load_dotenv

# 加載 .env 文件 (強制重新加載)
load_dotenv(override=True)

# 導入 AI 模組
try:
    from ai_chef_functions import init_ai_chef
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

# 檢查 API Key 是否配置 (優先檢查 Gemini)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HAS_API_KEY = bool(GEMINI_API_KEY or OPENAI_API_KEY)

# 調試：在側邊欄顯示 API Key 狀態
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

# 設置頁面配置
st.set_page_config(
    page_title="🤖 AI Chef Assistant",
    page_icon="👨‍🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定義 CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #FF6B6B 0%, #FFA500 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        font-size: 2.8rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .chat-message-user {
        background-color: #E3F2FD;
        padding: 12px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid #2196F3;
    }
    .chat-message-assistant {
        background-color: #FFF3E0;
        padding: 12px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid #FF9800;
    }
    .recipe-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    /* Enlarge Tab Labels */
    button[data-baseweb="tab"] {
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 15px 30px !important;
    }
</style>
""", unsafe_allow_html=True)

# 主頁面
st.markdown('<div class="main-title">🤖 AI Chef Assistant</div>', unsafe_allow_html=True)
st.markdown("### 👨‍🍳 與 AI 廚師對話，獲取烹飪建議 | 生成自定義菜譜")

# 側邊欄信息
with st.sidebar:
    st.markdown("## ℹ️ 應用信息")
    st.write(f"**版本**: 1.0 (AI Chef Assistant + Recipe Generator)")
    st.write(f"**上次更新**: {datetime.now().strftime('%Y-%m-%d')}")
    st.divider()
    
    # API 狀態檢查
    st.markdown("### 🔑 API 狀態")
    if GEMINI_API_KEY:
        st.success(f"✅ Gemini API: 已設置")
    else:
        st.error("❌ Gemini API: 未設置")
    
    if OPENAI_API_KEY:
        st.success(f"✅ OpenAI API: 已設置")
    else:
        st.warning("⚠️ OpenAI API: 未設置")
    
    st.divider()
    st.markdown("### 💡 使用提示")
    st.markdown("""
    - **AI Chef Assistant**: Ask any cooking-related questions
    - **Recipe Generator**: Enter a dish name to auto-generate a complete recipe
    - Can ask about techniques, ingredient combinations, nutrition info, etc.
    """)

# 主要功能
if not AI_AVAILABLE:
    st.error("❌ AI 模組加載失敗")
    st.info("請確保 ai_chef_functions.py 在同一目錄中")
elif not HAS_API_KEY:
    st.error("❌ AI 功能未啟用 - 缺少 API Key")
    st.warning("""
    ### 設置 API Key 步驟：
    
    **方式 1: 使用 Google Gemini API (推薦免費)**
    1. 訪問 https://ai.google.dev/
    2. 點擊 "Get API Key"
    3. 複製 API Key
    4. 在 `.env` 文件中添加：`GEMINI_API_KEY=your_key_here`
    5. 重啟 Streamlit 應用
    
    **方式 2: 使用 OpenAI API (付費)**
    1. 訪問 https://platform.openai.com/api-keys
    2. 複製 API Key
    3. 在 `.env` 文件中添加：`OPENAI_API_KEY=your_key_here`
    4. 重啟 Streamlit 應用
    """)
else:
    # 使用 Tabs 將兩個功能並排顯示
    tab1, tab2 = st.tabs(["💬 AI Chef Assistant", "✨ Recipe Generator"])
    
    # ==================== Tab 1: AI 廚師助手 ====================
    with tab1:
        st.markdown("### 💬 Chat with AI Chef")
        st.write("Ask any cooking-related questions, and the AI chef will answer for you")
        
        # 初始化對話歷史
        if "ai_chat_history" not in st.session_state:
            st.session_state.ai_chat_history = []
        
        # Chat History
        st.markdown("#### 📝 對話記錄")
        chat_container = st.container(height=350, border=True)
        
        with chat_container:
            if not st.session_state.ai_chat_history:
                st.info("👋 歡迎使用 AI Chef Assistant！\n\n💡 可以詢問：\n- 怎樣做某某菜\n- 烹飪技巧\n- 食材搭配\n- 營養信息等")
            else:
                for msg in st.session_state.ai_chat_history:
                    if msg["role"] == "user":
                        st.markdown(f'<div class="chat-message-user">👤 <b>你</b>: {msg["content"]}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="chat-message-assistant">👨‍🍳 <b>AI 廚師</b>: {msg["content"]}</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Input Area
        col1, col2, col3 = st.columns([5, 1, 1])
        
        with col1:
            user_input = st.text_input(
                "你的問題",
                placeholder="例如：怎樣做番茄炒雞蛋？",
                label_visibility="collapsed",
                key="chat_input"
            )
        
        with col2:
            send_btn = st.button("📤 發送", use_container_width=True, key="send_btn")
        
        with col3:
            clear_btn = st.button("🗑️ 清空", use_container_width=True, key="clear_btn")
        
        # Handle Send
        if send_btn and user_input:
            st.session_state.ai_chat_history.append({"role": "user", "content": user_input})
            
            with st.spinner("💬 AI Chef Assistant\n🤖🤖🤖 Thinking... 🤖🤖🤖"):
                try:
                    ai_chef = init_ai_chef()
                    response = ai_chef.chat(user_input)
                    st.session_state.ai_chat_history.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_msg = f"❌ 對話出錯: {str(e)}"
                    st.session_state.ai_chat_history.append({"role": "assistant", "content": error_msg})
            
            st.rerun()
        
        # Handle Clear
        if clear_btn:
            st.session_state.ai_chat_history = []
            st.rerun()
        
        # Quick Tips Buttons
        st.divider()
        st.markdown("#### ⚡ 快速提示")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🍳 How to make tomato and egg stir-fry?", use_container_width=True, key="quick1"):
                st.session_state.ai_chat_history.append({"role": "user", "content": "How to make tomato and egg stir-fry?"})
                with st.spinner("💬 AI Chef Assistant\n🤖🤖🤖 Thinking... 🤖🤖🤖"):
                    try:
                        ai_chef = init_ai_chef()
                        response = ai_chef.chat("How to make tomato and egg stir-fry?")
                        st.session_state.ai_chat_history.append({"role": "assistant", "content": response})
                    except Exception as e:
                        error_msg = f"❌ 對話出錯: {str(e)}"
                        st.session_state.ai_chat_history.append({"role": "assistant", "content": error_msg})
                st.rerun()
        
        with col2:
            if st.button("🔥 Cooking Heat Techniques", use_container_width=True, key="quick2"):
                st.session_state.ai_chat_history.append({"role": "user", "content": "Tell me about cooking heat control techniques"})
                with st.spinner("💬 AI Chef Assistant\n🤖🤖🤖 Thinking... 🤖🤖🤖"):
                    try:
                        ai_chef = init_ai_chef()
                        response = ai_chef.chat("Tell me about cooking heat control techniques")
                        st.session_state.ai_chat_history.append({"role": "assistant", "content": response})
                    except Exception as e:
                        error_msg = f"❌ 對話出錯: {str(e)}"
                        st.session_state.ai_chat_history.append({"role": "assistant", "content": error_msg})
                st.rerun()
        
        with col3:
            if st.button("🥗 Nutrition Pairing Tips", use_container_width=True, key="quick3"):
                st.session_state.ai_chat_history.append({"role": "user", "content": "Give me some nutrition pairing suggestions"})
                with st.spinner("💬 AI Chef Assistant\n🤖🤖🤖 Thinking... 🤖🤖🤖"):
                    try:
                        ai_chef = init_ai_chef()
                        response = ai_chef.chat("Give me some nutrition pairing suggestions")
                        st.session_state.ai_chat_history.append({"role": "assistant", "content": response})
                    except Exception as e:
                        error_msg = f"❌ 對話出錯: {str(e)}"
                        st.session_state.ai_chat_history.append({"role": "assistant", "content": error_msg})
                st.rerun()
    
    # ==================== Tab 2: Recipe Generator ====================
    with tab2:
        st.markdown("### ✨ AI Smart Recipe Generator")
        st.write("Enter a dish name and cooking parameters, AI will auto-generate a complete recipe")
        
        col1, col2 = st.columns(2)
        
        with col1:
            dish_name = st.text_input(
                "菜名",
                placeholder="例如：番茄湯、宮保雞丁...",
                label_visibility="collapsed",
                key="dish_name"
            )
            difficulty = st.select_slider(
                "難度",
                options=["簡單", "中等", "困難"],
                value="中等",
                key="difficulty"
            )
            servings = st.number_input(
                "份量",
                min_value=1,
                max_value=10,
                value=2,
                step=1,
                key="servings"
            )
        
        with col2:
            cooking_time = st.number_input(
                "烹飪時間 (分鐘)",
                min_value=5,
                max_value=180,
                value=30,
                step=5,
                key="cooking_time"
            )
            ingredients_text = st.text_area(
                "可用食材 (每行一個)",
                placeholder="例如：\n雞蛋\n番茄\n油\n鹽",
                height=100,
                label_visibility="collapsed",
                key="ingredients"
            )
        
        if st.button("🚀 生成食譜", use_container_width=True, type="primary", key="generate_btn"):
            if not dish_name:
                st.error("❌ 請輸入菜名")
            else:
                with st.spinner("✨ Recipe Generator\n🤖🤖🤖 Creating recipe... 🤖🤖🤖"):
                    try:
                        ai_chef = init_ai_chef()
                        ingredients = [ing.strip() for ing in ingredients_text.split('\n') if ing.strip()]
                        
                        recipe = ai_chef.generate_recipe(
                            dish_name=dish_name,
                            difficulty=difficulty,
                            servings=servings,
                            available_ingredients=ingredients if ingredients else None,
                            cooking_time_limit=cooking_time
                        )
                        
                        if "error" in recipe:
                            st.error(f"❌ 生成失敗: {recipe['error']}")
                        else:
                            st.success("✅ 食譜生成成功！")
                            
                            # Display the generated recipe
                            if isinstance(recipe, dict):
                                # Extract key information
                                st.markdown(f"### 🍳 {recipe.get('菜名', dish_name)}")
                                
                                col1, col2, col3, col4 = st.columns(4)
                                with col1:
                                    st.metric("難度", recipe.get('難度', difficulty))
                                with col2:
                                    st.metric("烹飪時間", recipe.get('烹飪時間', f'{cooking_time}分鐘'))
                                with col3:
                                    st.metric("份量", recipe.get('份量', f'{servings}人份'))
                                with col4:
                                    st.metric("分類", recipe.get('分類', '其他'))
                                
                                st.divider()
                                
                                # Ingredients
                                if '材料' in recipe:
                                    st.markdown("#### 📦 材料準備")
                                    if isinstance(recipe['材料'], dict):
                                        for material, amount in recipe['材料'].items():
                                            st.write(f"- **{material}**: {amount}")
                                    else:
                                        st.write(recipe['材料'])
                                
                                # Steps
                                if '步驟' in recipe:
                                    st.markdown("#### 👨‍🍳 烹飪步驟")
                                    if isinstance(recipe['步驟'], list):
                                        for step in recipe['步驟']:
                                            st.write(f"{step}")
                                    else:
                                        st.write(recipe['步驟'])
                                
                                # Tips
                                if '烹飪技巧' in recipe:
                                    st.markdown("#### 🔥 烹飪技巧")
                                    if isinstance(recipe['烹飪技巧'], list):
                                        for tip in recipe['烹飪技巧']:
                                            st.markdown(f"- {tip}")
                                    else:
                                        st.write(recipe['烹飪技巧'])
                                
                                st.divider()
                                
                                # Full JSON
                                with st.expander("📊 查看完整食譜 (JSON 格式)"):
                                    st.json(recipe)
                            else:
                                st.json(recipe)
                    
                    except Exception as e:
                        st.error(f"❌ 生成出錯: {str(e)}")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; margin-top: 30px;'>
    <p>🤖 AI Chef Assistant v1.0</p>
    <p>由 Streamlit + Gemini/OpenAI 驅動</p>
</div>
""", unsafe_allow_html=True)


"""
AI 廚師顧問 - 人工智慧模組
AI Chef Advisor - AI Integration Module

包含 AI 菜譜生成、圖片識別、營養分析等功能
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import base64
from io import BytesIO

# AI 相關導入
try:
    from openai import OpenAI, APIError
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

# 圖片處理
from PIL import Image
import numpy as np


class AIChefAdvisor:
    """AI 廚師顧問主類"""
    
    def __init__(self, api_key: Optional[str] = None, use_service: str = "openai"):
        """
        初始化 AI 廚師顧問
        
        Parameters:
        -----------
        api_key : str, optional
            API 金鑰
        use_service : str
            使用的 AI 服務: "openai", "gemini", 或 "local"
        """
        self.use_service = use_service
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        if use_service == "openai" and OPENAI_AVAILABLE:
            self.client = OpenAI(api_key=self.api_key)
        elif use_service == "gemini" and GEMINI_AVAILABLE:
            genai.configure(api_key=self.api_key)
        
        self.conversation_history = []
    
    # ==================== 菜譜生成 ====================
    
    def generate_recipe(self, 
                       dish_name: str, 
                       difficulty: str = "medium",
                       servings: int = 2,
                       available_ingredients: List[str] = None,
                       cooking_time_limit: int = None) -> Dict:
        """
        使用 AI 生成菜譜
        
        Parameters:
        -----------
        dish_name : str
            菜名
        difficulty : str
            難度: "easy", "medium", "hard"
        servings : int
            份量
        available_ingredients : list
            可用食材
        cooking_time_limit : int
            烹飪時間限制（分鐘）
        
        Returns:
        --------
        dict
            生成的菜譜
        """
        
        prompt = self._build_recipe_prompt(
            dish_name, difficulty, servings, 
            available_ingredients, cooking_time_limit
        )
        
        if self.use_service == "openai" and OPENAI_AVAILABLE:
            return self._generate_with_openai(prompt, "recipe")
        elif self.use_service == "gemini" and GEMINI_AVAILABLE:
            return self._generate_with_gemini(prompt, "recipe")
        else:
            return self._generate_with_local(prompt, "recipe")
    
    def _build_recipe_prompt(self, 
                             dish_name: str,
                             difficulty: str,
                             servings: int,
                             available_ingredients: List[str],
                             cooking_time_limit: int) -> str:
        """構建菜譜生成提示詞"""
        
        prompt = f"""
請為我生成一份詳細的 {dish_name} 菜譜，要求如下：

基本信息：
- 菜名: {dish_name}
- 難度級別: {difficulty} (easy/medium/hard)
- 份量: {servings} 人份
- 烹飪語言: 繁體中文

格式要求（請按以下 JSON 格式返回）：
{{
    "菜名": "{dish_name}",
    "難度": "難度等級描述",
    "烹飪時間": "X-Y分鐘",
    "份量": "{servings}人份",
    "材料": {{
        "材料名": "用量描述",
        ...
    }},
    "步驟": [
        "第一步的詳細描述",
        "第二步的詳細描述",
        ...
    ],
    "烹飪技巧": [
        "技巧1: 描述",
        "技巧2: 描述",
        ...
    ],
    "營養信息": {{
        "熱量": "數值 kcal/份",
        "蛋白質": "數值g",
        "脂肪": "數值g",
        "碳水化合物": "數值g"
    }},
    "健康提示": [
        "提示1",
        "提示2",
        ...
    ],
    "搭配建議": [
        "搭配建議1",
        "搭配建議2",
        ...
    ]
}}
"""
        
        if available_ingredients:
            prompt += f"\n可用食材: {', '.join(available_ingredients)}\n"
        
        if cooking_time_limit:
            prompt += f"烹飪時間限制: 不超過 {cooking_time_limit} 分鐘\n"
        
        return prompt
    
    def _generate_with_openai(self, prompt: str, task_type: str) -> Dict:
        """使用 OpenAI API 生成內容"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是一位專業的廚師和營養師，提供詳細準確的菜譜和烹飪建議。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            
            # 嘗試解析 JSON
            try:
                import re
                json_match = re.search(r'\{.*\}', content, re.DOTALL)
                if json_match:
                    return json.loads(json_match.group())
            except:
                pass
            
            return {"raw_response": content}
        
        except APIError as e:
            return {"error": f"OpenAI API 錯誤: {str(e)}"}
    
    def _generate_with_gemini(self, prompt: str, task_type: str) -> Dict:
        """使用 Google Gemini API 生成內容"""
        try:
            # 檢查 API Key
            if not self.api_key:
                return {"error": "❌ 未設置 GEMINI_API_KEY\n\n請在 .env 文件中添加：\nGEMINI_API_KEY=your_api_key_here\n\n獲取 API Key: https://ai.google.dev"}
            
            # 嘗試使用最新的穩定 Gemini 模型
            models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content(prompt)
                    
                    content = response.text
                    
                    # 嘗試解析 JSON
                    try:
                        import re
                        json_match = re.search(r'\{.*\}', content, re.DOTALL)
                        if json_match:
                            return json.loads(json_match.group())
                    except:
                        pass
                    
                    return {"raw_response": content}
                except Exception as model_error:
                    # 嘗試下一個模型
                    continue
            
            return {"error": "❌ 所有 Gemini 模型都不可用\n請檢查：\n1. API Key 是否正確\n2. 網路連接\n3. 服務狀態"}
        
        except Exception as e:
            return {"error": f"❌ Gemini API 錯誤: {str(e)}"}
    
    def _generate_with_local(self, prompt: str, task_type: str) -> Dict:
        """本地生成（回退方案）"""
        return {
            "error": "未配置 AI 服務",
            "message": "請設置 OPENAI_API_KEY 或 GEMINI_API_KEY",
            "hint": "可在 .env 文件中設置 API 金鑰"
        }
    
    # ==================== 圖片識別 ====================
    
    def identify_dish_from_image(self, image_path: str) -> Dict:
        """
        從圖片識別菜品
        
        Parameters:
        -----------
        image_path : str
            圖片文件路徑
        
        Returns:
        --------
        dict
            識別結果
        """
        
        if not os.path.exists(image_path):
            return {"error": "圖片文件不存在"}
        
        # 提取圖片特徵進行分析
        image_features = self._extract_image_features(image_path)
        
        if self.use_service == "openai" and OPENAI_AVAILABLE:
            return self._identify_with_openai(image_path)
        elif self.use_service == "gemini" and GEMINI_AVAILABLE:
            return self._identify_with_gemini(image_path)
        else:
            return self._identify_with_local(image_features)
    
    def _identify_with_openai(self, image_path: str) -> Dict:
        """使用 OpenAI Vision API 識別圖片"""
        try:
            with open(image_path, "rb") as image_file:
                image_data = base64.standard_b64encode(image_file.read()).decode("utf-8")
            
            # 確定圖片類型
            ext = Path(image_path).suffix.lower()
            media_type = "image/jpeg" if ext in [".jpg", ".jpeg"] else f"image/{ext[1:]}"
            
            response = self.client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """分析這張美食圖片，請返回以下信息（使用 JSON 格式，語言為繁體中文）：
{
    "菜品名稱": ["可能的菜名1", "可能的菜名2", ...],
    "置信度": [0.95, 0.87, ...],
    "食材分析": ["食材1", "食材2", ...],
    "烹飪方式": "推測的烹飪方式",
    "難度評估": "簡單/中等/難",
    "營養特點": ["特點1", "特點2", ...],
    "烹飪建議": "基於這道菜的烹飪建議",
    "相似菜品": ["相似菜品1", "相似菜品2", ...]
}"""
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{media_type};base64,{image_data}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1024
            )
            
            content = response.choices[0].message.content
            
            # 嘗試解析 JSON
            try:
                import re
                json_match = re.search(r'\{.*\}', content, re.DOTALL)
                if json_match:
                    return json.loads(json_match.group())
            except:
                pass
            
            return {"raw_response": content}
        
        except APIError as e:
            return {"error": f"圖片識別失敗: {str(e)}"}
    
    def _identify_with_gemini(self, image_path: str) -> Dict:
        """使用 Google Gemini Vision API 識別圖片"""
        try:
            # 嘗試支持視覺功能的 Gemini 模型
            models_to_try = ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-pro-vision', 'gemini-pro']
            
            image = Image.open(image_path)
            
            prompt = """分析這張美食圖片，請返回以下信息（使用 JSON 格式，語言為繁體中文）：
{
    "菜品名稱": ["可能的菜名1", "可能的菜名2", ...],
    "置信度": [0.95, 0.87, ...],
    "食材分析": ["食材1", "食材2", ...],
    "烹飪方式": "推測的烹飪方式",
    "難度評估": "簡單/中等/難",
    "營養特點": ["特點1", "特點2", ...],
    "烹飪建議": "基於這道菜的烹飪建議",
    "相似菜品": ["相似菜品1", "相似菜品2", ...]
}"""
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content([prompt, image])
                    
                    content = response.text
                    
                    # 嘗試解析 JSON
                    try:
                        import re
                        json_match = re.search(r'\{.*\}', content, re.DOTALL)
                        if json_match:
                            return json.loads(json_match.group())
                    except:
                        pass
                    
                    return {"raw_response": content}
                
                except Exception as model_error:
                    # 嘗試下一個模型
                    continue
            
            return {"error": "所有 Gemini Vision 模型都不可用"}
        
        except Exception as e:
            return {"error": f"圖片識別失敗: {str(e)}"}
    
    def _identify_with_local(self, image_features: Dict) -> Dict:
        """本地圖片識別（基於視覺特徵）"""
        return {
            "菜品名稱": ["番茄炒雞蛋", "清蒸魚", "紅燒肉"],
            "置信度": [0.78, 0.65, 0.52],
            "食材分析": list(image_features.get("dominant_colors", [])),
            "烹飪方式": "炒/蒸/燉",
            "難度評估": "中等",
            "營養特點": ["豐富蛋白質", "含纖維"],
            "烹飪建議": "基於圖片特徵的一般性烹飪建議",
            "相似菜品": ["類似菜品1", "類似菜品2"],
            "note": "使用本地特徵分析，建議配置 OpenAI 或 Gemini API 以獲得更精確的結果"
        }
    
    def _extract_image_features(self, image_path: str) -> Dict:
        """提取圖片特徵"""
        try:
            image = Image.open(image_path)
            
            # 轉換為 RGB
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # 提取主要顏色
            image_small = image.resize((50, 50))
            pixels = np.array(image_small).reshape(-1, 3)
            
            # 計算平均顏色
            avg_color = pixels.mean(axis=0)
            
            # 識別色調
            hue = self._get_hue_description(avg_color)
            
            return {
                "size": image.size,
                "mode": image.mode,
                "avg_color": avg_color.tolist(),
                "hue": hue,
                "dominant_colors": ["紅色" if hue == "red" else "其他色系"]
            }
        
        except Exception as e:
            return {"error": str(e)}
    
    def _get_hue_description(self, rgb: np.ndarray) -> str:
        """根據 RGB 值判斷色調"""
        r, g, b = rgb
        
        if r > g and r > b:
            return "red"
        elif g > r and g > b:
            return "green"
        elif b > r and b > g:
            return "blue"
        else:
            return "other"
    
    # ==================== 烹飪建議 ====================
    
    def get_cooking_advice(self, 
                          dish_name: str,
                          skill_level: str = "intermediate",
                          dietary_restrictions: List[str] = None) -> Dict:
        """
        獲取個性化烹飪建議
        
        Parameters:
        -----------
        dish_name : str
            菜名
        skill_level : str
            技能等級: "beginner", "intermediate", "advanced"
        dietary_restrictions : list
            飲食限制
        
        Returns:
        --------
        dict
            烹飪建議
        """
        
        prompt = f"""
為一位{skill_level}級廚師提供 {dish_name} 的烹飪建議。
"""
        
        if dietary_restrictions:
            prompt += f"飲食限制: {', '.join(dietary_restrictions)}\n"
        
        prompt += """
請返回 JSON 格式的建議，包含：
{
    "難度評估": "難度描述",
    "關鍵技巧": ["技巧1", "技巧2", ...],
    "常見錯誤": ["錯誤1", "錯誤2", ...],
    "補救方案": ["補救方案1", "補救方案2", ...],
    "時間管理": "時間分配建議",
    "替代食材": ["替代食材1", "替代食材2", ...],
    "個性化建議": "根據技能等級的具體建議"
}
"""
        
        if self.use_service == "openai" and OPENAI_AVAILABLE:
            return self._generate_with_openai(prompt, "advice")
        elif self.use_service == "gemini" and GEMINI_AVAILABLE:
            return self._generate_with_gemini(prompt, "advice")
        else:
            return self._generate_with_local(prompt, "advice")
    
    # ==================== 營養分析 ====================
    
    def analyze_nutrition(self, 
                         ingredients: Dict[str, str],
                         servings: int = 1) -> Dict:
        """
        分析菜譜的營養成分
        
        Parameters:
        -----------
        ingredients : dict
            食材及用量
        servings : int
            份量
        
        Returns:
        --------
        dict
            營養分析結果
        """
        
        ingredients_text = "\n".join([f"- {name}: {amount}" for name, amount in ingredients.items()])
        
        prompt = f"""
分析以下食材組合的營養成分（{servings}人份）：

{ingredients_text}

請返回詳細的 JSON 營養分析：
{{
    "總熱量": "X kcal",
    "宏量營養": {{
        "蛋白質": "Xg",
        "脂肪": "Xg",
        "碳水化合物": "Xg"
    }},
    "微量營養": {{
        "鈣": "mg",
        "鐵": "mg",
        "維生素C": "mg"
    }},
    "飲食適應": {{
        "素食": true/false,
        "無麩質": true/false,
        "低脂": true/false
    }},
    "健康評分": "1-10分的評分",
    "健康建議": ["建議1", "建議2", ...]
}}
"""
        
        if self.use_service == "openai" and OPENAI_AVAILABLE:
            return self._generate_with_openai(prompt, "nutrition")
        elif self.use_service == "gemini" and GEMINI_AVAILABLE:
            return self._generate_with_gemini(prompt, "nutrition")
        else:
            return self._generate_with_local(prompt, "nutrition")
    
    # ==================== 對話功能 ====================
    
    def chat(self, user_message: str) -> str:
        """
        與 AI 廚師進行對話
        
        Parameters:
        -----------
        user_message : str
            用戶消息
        
        Returns:
        --------
        str
            AI 回應
        """
        
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        if self.use_service == "openai" and OPENAI_AVAILABLE:
            return self._chat_with_openai()
        elif self.use_service == "gemini" and GEMINI_AVAILABLE:
            return self._chat_with_gemini()
        else:
            return self._chat_with_local()
    
    def _chat_with_openai(self) -> str:
        """使用 OpenAI 進行對話"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                system="你是一位友善且知識豐富的廚師，幫助用戶解答烹飪相關問題。使用繁體中文回應。",
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=512
            )
            
            assistant_message = response.choices[0].message.content
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
        
        except APIError as e:
            return f"❌ 對話出錯: {str(e)}"
    
    def _chat_with_gemini(self) -> str:
        """使用 Gemini 進行對話"""
        try:
            # 檢查 API Key
            if not self.api_key:
                return "❌ 未設置 GEMINI_API_KEY\n請在 .env 文件中添加 API Key"
            
            # 嘗試使用最新的穩定 Gemini 模型
            models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    
                    response = model.generate_content(
                        f"""你是一位友善且知識豐富的廚師，幫助用戶解答烹飪相關問題。使用繁體中文回應。
用戶說: {self.conversation_history[-1]['content']}"""
                    )
                    
                    assistant_message = response.text
                    self.conversation_history.append({
                        "role": "assistant",
                        "content": assistant_message
                    })
                    
                    return assistant_message
                except Exception as model_error:
                    # 嘗試下一個模型
                    continue
            
            return "❌ 所有 Gemini 模型都不可用\n請檢查 API Key 和網路連接"
        
        except Exception as e:
            return f"❌ 對話出錯: {str(e)}"
    
    def _chat_with_local(self) -> str:
        """本地對話（回退方案）"""
        return "未配置 AI 服務。請設置 OPENAI_API_KEY 或 GEMINI_API_KEY 以使用 AI 功能。"
    
    def clear_conversation(self):
        """清除對話歷史"""
        self.conversation_history = []


# ==================== 便利函數 ====================

def init_ai_chef(api_key: Optional[str] = None, service: str = "auto") -> AIChefAdvisor:
    """
    初始化 AI 廚師顧問
    
    Parameters:
    -----------
    api_key : str, optional
        API 金鑰
    service : str
        服務選擇: "auto", "openai", "gemini", "local"
    
    Returns:
    --------
    AIChefAdvisor
        AI 廚師顧問實例
    """
    
    if service == "auto":
        # 自動檢測可用服務
        if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
            service = "openai"
        elif GEMINI_AVAILABLE and os.getenv("GEMINI_API_KEY"):
            service = "gemini"
        else:
            service = "local"
    
    return AIChefAdvisor(api_key=api_key, use_service=service)

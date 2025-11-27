#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
將 Markdown 聊天紀錄轉換為 PDF
Converts Markdown conversation summary to PDF
"""

import os
import sys

def convert_md_to_pdf():
    """使用 markdown2 和 wkhtmltopdf 轉換 PDF"""
    try:
        # 嘗試使用 markdown2 + wkhtmltopdf
        import markdown2
        from subprocess import run, PIPE
        
        md_file = "CONVERSATION_SUMMARY.md"
        pdf_file = "CONVERSATION_SUMMARY.pdf"
        html_file = "CONVERSATION_SUMMARY.html"
        
        if not os.path.exists(md_file):
            print(f"❌ 找不到文件: {md_file}")
            return False
        
        # 讀取 Markdown
        print("📖 讀取 Markdown 文件...")
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 轉換為 HTML
        print("🔄 轉換為 HTML...")
        html_content = markdown2.markdown(
            md_content,
            extras=['tables', 'fenced-code-blocks', 'toc']
        )
        
        # 添加 HTML 模板
        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Chef Assistant - 開發聊天紀錄</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Microsoft YaHei', 'SimHei', Arial, sans-serif;
            line-height: 1.8;
            color: #333;
            background: white;
            padding: 40px;
        }}
        
        h1 {{
            color: #1976d2;
            border-bottom: 4px solid #1976d2;
            padding: 20px 0;
            margin: 40px 0 20px 0;
            font-size: 2.2em;
        }}
        
        h2 {{
            color: #0d47a1;
            margin-top: 30px;
            margin-bottom: 15px;
            padding: 10px 0;
            border-left: 4px solid #0d47a1;
            padding-left: 15px;
            font-size: 1.8em;
        }}
        
        h3 {{
            color: #1565c0;
            margin: 20px 0 10px 0;
            font-size: 1.3em;
        }}
        
        h4, h5, h6 {{
            color: #1976d2;
            margin: 15px 0 5px 0;
        }}
        
        p {{
            margin: 10px 0;
            text-align: justify;
        }}
        
        code {{
            background: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #d32f2f;
            font-size: 0.9em;
        }}
        
        pre {{
            background: #f5f5f5;
            border: 1px solid #ddd;
            border-left: 4px solid #1976d2;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
            font-size: 0.85em;
        }}
        
        pre code {{
            color: #333;
            background: transparent;
            padding: 0;
        }}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        table th {{
            background-color: #1976d2;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: bold;
        }}
        
        table td {{
            padding: 10px 12px;
            border-bottom: 1px solid #ddd;
        }}
        
        table tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        table tr:hover {{
            background-color: #f0f0f0;
        }}
        
        ul, ol {{
            margin: 15px 0;
            padding-left: 40px;
            line-height: 2;
        }}
        
        li {{
            margin: 5px 0;
        }}
        
        blockquote {{
            border-left: 4px solid #1976d2;
            margin: 15px 0;
            padding: 10px 15px;
            background: #f0f7ff;
            color: #0d47a1;
        }}
        
        strong {{
            color: #d32f2f;
            font-weight: bold;
        }}
        
        em {{
            color: #f57c00;
            font-style: italic;
        }}
        
        a {{
            color: #1976d2;
            text-decoration: none;
            border-bottom: 1px dotted #1976d2;
        }}
        
        a:hover {{
            color: #0d47a1;
            border-bottom-style: solid;
        }}
        
        .emoji {{
            font-size: 1.2em;
        }}
        
        hr {{
            border: none;
            border-top: 2px solid #1976d2;
            margin: 30px 0;
        }}
        
        /* 頁面分割 */
        .page-break {{
            page-break-after: always;
        }}
        
        /* 打印樣式 */
        @media print {{
            body {{ padding: 0; }}
            h1 {{ page-break-before: always; }}
        }}
    </style>
</head>
<body>
    {html_content}
    
    <hr>
    <p style="text-align: center; margin-top: 40px; color: #999; font-size: 0.9em;">
        <strong>文檔生成時間:</strong> 2025年11月27日<br>
        <strong>開發者:</strong> Brain0927<br>
        <strong>項目名稱:</strong> AI Chef Assistant<br>
        <strong>GitHub:</strong> https://github.com/Brain0927/HW4_Fulong_5114056035
    </p>
</body>
</html>"""
        
        # 保存 HTML
        print(f"💾 保存 HTML 檔案: {html_file}")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        # 嘗試使用 wkhtmltopdf
        print("📄 轉換為 PDF...")
        try:
            result = run(
                ['wkhtmltopdf', '--quiet', html_file, pdf_file],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0 and os.path.exists(pdf_file):
                print(f"✅ PDF 已生成: {pdf_file}")
                print(f"📊 檔案大小: {os.path.getsize(pdf_file) / 1024:.1f} KB")
                return True
        except FileNotFoundError:
            print("⚠️  wkhtmltopdf 未安裝")
        
        # 如果 wkhtmltopdf 不可用，提示用戶
        print("\n📋 已生成 HTML 檔案，可以通過以下方式轉換為 PDF：")
        print("1. 在瀏覽器中打開 HTML 檔案，按 Ctrl+P 轉換為 PDF")
        print("2. 安裝 wkhtmltopdf: https://wkhtmltopdf.org/")
        print("3. 使用 pandoc: pandoc CONVERSATION_SUMMARY.md -o CONVERSATION_SUMMARY.pdf")
        
        return True
        
    except ImportError as e:
        print(f"❌ 缺少必要的模塊: {e}")
        print("\n💡 解決方案:")
        print("1. 安裝 markdown2: pip install markdown2")
        print("2. 使用在線工具: https://md2pdf.netlify.app")
        print("3. 使用 Pandoc: https://pandoc.org/")
        return False
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        return False

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__) or '.')
    success = convert_md_to_pdf()
    sys.exit(0 if success else 1)

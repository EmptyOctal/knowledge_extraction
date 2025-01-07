import re

def clean_text(text):
    """清理文本，去除标点、特殊字符等"""
    text = re.sub(r'\s+', ' ', text)  # 去除多余空格
    text = re.sub(r'[^\w\s]', '', text)  # 去除标点符号
    return text.strip()

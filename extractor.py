from preprocessor import clean_text
from segmenter import segment_and_tag
from rules.base_rules import apply_rules

def extract_knowledge(text):
    """
    知识抽取主逻辑
    :param text: 输入文本
    :return: 知识三元组列表 [(主语, 谓语, 宾语)]
    """
    # 1. 文本预处理
    cleaned_text = clean_text(text)
    
    # 2. 分词与词性标注
    words = segment_and_tag(cleaned_text)
    
    # 3. 应用规则提取三元组
    knowledge = apply_rules(words)
    return knowledge

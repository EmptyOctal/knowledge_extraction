import re

def rule_is_relation(words):
    """
    规则1：提取 "A 是 B" 的句式
    :param words: 分词与词性标注结果 [(word, pos)]
    :return: 知识三元组列表 [(主语, 谓语, 宾语)]
    """
    pattern = re.compile(r'(\w+)/n 是/v (\w+)/n')  # 匹配 “名词 是 名词”
    sentence = " ".join([f"{w}/{p}" for w, p in words])  # 转换成标注格式
    matches = pattern.findall(sentence)
    return [(match[0], "是", match[1]) for match in matches]


def rule_own_relation(words):
    """
    规则2：提取 "X 拥有 Y" 的句式
    :param words: 分词与词性标注结果 [(word, pos)]
    :return: 知识三元组列表 [(主语, 谓语, 宾语)]
    """
    pattern = re.compile(r'(\w+)/n 拥有/v (\w+)/n')  # 匹配 “名词 拥有 名词”
    sentence = " ".join([f"{w}/{p}" for w, p in words])
    matches = pattern.findall(sentence)
    return [(match[0], "拥有", match[1]) for match in matches]


def apply_rules(words):
    """应用所有规则，返回所有三元组"""
    results = []
    results.extend(rule_is_relation(words))
    results.extend(rule_own_relation(words))
    return results

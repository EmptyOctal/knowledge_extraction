import re

def to_sentence(words):
    """
    将分词与词性标注结果转换为字符串模式。
    示例：
    输入: [('张三', 'nr'), ('是', 'v'), ('学生', 'n')]
    输出: '张三/nr 是/v 学生/n'
    """
    return ' '.join(f"{word}/{tag}" for word, tag in words)


# 定义名词词性集合
NOUN_TAGS = {'n', 'nr', 'ns', 'nt', 'nz', 'ng'}

def rule_verb_object_relation(sentence):
    """
    规则1：提取一般动宾结构 "A 动作 B"
    """
    triples = []
    # (\S+)/(nt|ns|n|ng|nr|nz) (\S+)/v (\S+)/(nt|ns|n|ng|nr|nz)
    pattern = r'(\S+)/({}) (\S+)/v (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        triples.append((match.group(1), match.group(3), match.group(4)))
    return triples


def apply_rules(words):
    """
    应用所有规则
    :param words: 分词与词性标注结果
    :return: 知识三元组列表
    """
    sentence = to_sentence(words)
    # print('sentence:',sentence)
    results = []
    results.extend(rule_verb_object_relation(sentence))
    return results
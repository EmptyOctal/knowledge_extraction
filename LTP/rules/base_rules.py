import re

def to_sentence(words):
    """
    将分词与词性标注结果转换为字符串模式。
    """
    return ' '.join(f"{word}/{tag}" for word, tag in words)

NOUN_TAGS = {'n', 'nh', 'nl', 'ns', 'ni', 'nz'}  # 名词集合
ADJ_TAG = 'a'  # 形容词
VERB_TAG = 'v'  # 动词
TIME_TAG = 'nt'  # 时间名词
LOC_TAG = 'ns'  # 地点名词

def rule_verb_object_relation(sentence):
    """规则1：提取一般动宾结构"""
    triples = set()
    pattern = r'(\S+)/({}) (\S+)/v (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = match.group(3)
        obj = match.group(4)
        triples.add((subject, verb, obj))
    return triples

def rule_is_relation(sentence):
    """规则2：提取"A 是 B"的描述性关系"""
    triples = set()
    pattern = r'(\S+)/({}) 是/v (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = "是"
        obj = match.group(3)
        triples.add((subject, verb, obj))
    return triples

def rule_adj_noun_relation(sentence):
    """规则3：提取形容词修饰名词的属性关系"""
    triples = set()
    pattern = r'(\S+)/a 的/u (\S+)/({})'.format('|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        adj = match.group(1)
        noun = match.group(2)
        triples.add((adj, '修饰', noun))
    return triples

def rule_time_loc_relation(sentence):
    """规则4：提取时间或地点的修饰关系"""
    triples = set()
    pattern = r'(\S+)/({}|{}) (\S+)/v (\S+)/({})'.format(TIME_TAG, LOC_TAG, '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        modifier = match.group(1)
        verb = match.group(3)
        obj = match.group(4)
        triples.add((modifier, verb, obj))
    return triples

def rule_verb_loc_relation(sentence):
    """规则5：提取动词+地点的关系"""
    triples = set()
    pattern = r'(\S+)/({}) (\S+)/v (\S+)/({})'.format('|'.join(NOUN_TAGS), LOC_TAG)
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = match.group(3)
        loc = match.group(4)
        triples.add((subject, verb, loc))
    return triples

def rule_verb_time_relation(sentence):
    """规则6：提取动词+时间的关系"""
    triples = set()
    pattern = r'(\S+)/({}) (\S+)/v (\S+)/({})'.format('|'.join(NOUN_TAGS), TIME_TAG)
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = match.group(3)
        time = match.group(4)
        triples.add((subject, verb, time))
    return triples

def rule_has_relation(sentence):
    """规则7：提取“具有”关系"""
    triples = set()
    pattern = r'(\S+)/({}) 具有/v .*? (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = "具有"
        obj = match.group(3)
        triples.add((subject, verb, obj))
    return triples

def rule_include_relation(sentence):
    """规则8：提取“包括”关系。"""
    triples = set()
    pattern = r'(\S+)/({}) (包括|包含|含有)/v .*? (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = "包括"
        obj = match.group(4)
        triples.add((subject, verb, obj))
    return triples

def rule_own_relation(sentence):
    """规则9：提取“拥有”关系。"""
    triples = set()
    pattern = r'(\S+)/({}) (拥有|坐拥|持有|获得)/v .*? (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = "拥有"
        obj = match.group(4)
        triples.add((subject, verb, obj))
    return triples

def rule_need_relation(sentence):
    """规则10：提取“需要”关系。"""
    triples = set()
    pattern = r'(\S+)/({}) (需要|急需)/v .*? (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        verb = "需要"
        obj = match.group(4)
        triples.add((subject, verb, obj))
    return triples

def rule_cause_relation(sentence):
    """规则11：提取“因果”关系"""
    triples = set()
    pattern = r'(\S+)/({}) (使得|导致)/v (\S+)/({})'.format('|'.join(['n', 'nz', 'nl', 'ns']), '|'.join(['n', 'nz', 'nl', 'ns']))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        cause = match.group(1)
        effect = match.group(4)
        triples.add((cause, "导致", effect))
    return triples


def rule_modify_relation(sentence):
    """规则12：提取“修饰”关系"""
    triples = set()
    pattern = r'(\S+)/({}) (\S+)/a'.format('|'.join(['n', 'nz', 'nl', 'ns']))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        adj = match.group(3)
        noun = match.group(1)
        triples.add((adj, "修饰", noun))
    return triples

def rule_person_location_label(sentence):
    """
    规则13：提取 A/nh 为 'A 是 人物'，提取 A/ns 或 A/nl 为 'A 是 地点'
    """
    triples = set()
    # 提取人物
    person_pattern = r'(\S+)/nh'
    person_matches = re.finditer(person_pattern, sentence)
    for match in person_matches:
        entity = match.group(1)
        triples.add((entity, "是", "人物"))

    # 提取地点
    location_pattern = r'(\S+)/({}|{})'.format(LOC_TAG, 'nl')
    location_matches = re.finditer(location_pattern, sentence)
    for match in location_matches:
        entity = match.group(1)
        triples.add((entity, "是", "地点"))

    return triples

def rule_food_relation(sentence):
    """规则14：提取 动词'吃'/'喝' 或形容词'美味的' 后面名词'A'，标记为 A 是 食物"""
    triples = set()
    # 修改匹配模式，支持“吃/v”、“喝/v”、“美味/a 的/u” 后接 名词/n
    pattern = r'(吃/v|喝/v|美味/a 的/u) .*? (\S+)/({})'.format('|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        action = match.group(1)  # 动作或形容词短语
        food = match.group(2)  # 名词
        triples.add((food, "是", "食物"))
    return triples


def rule_like_relation(sentence):
    """规则15：提取 名词/人物 + 喜欢 + 动词短语 或 动宾结构"""
    triples = set()
    # 匹配“喜欢 + 动词短语”，确保动词后面不是名词
    pattern_phrase = r'(\S+)/(n|nh) 喜欢/v (\S+)/v(?! \S+/n)'
    # 匹配“喜欢 + 动宾结构”
    pattern_verb_object = r'(\S+)/(n|nh) 喜欢/v (\S+)/v (\S+)/({})'.format('|'.join(NOUN_TAGS))

    # 匹配“喜欢 + 动词短语”
    matches_phrase = re.finditer(pattern_phrase, sentence)
    for match in matches_phrase:
        subject = match.group(1)  # 主体：名词或人物
        verb = "喜欢"
        action = match.group(3)  # 动词短语
        triples.add((subject, verb, action))

    # 匹配“喜欢 + 动宾结构”
    matches_verb_object = re.finditer(pattern_verb_object, sentence)
    for match in matches_verb_object:
        subject = match.group(1)  # 主体：名词或人物
        verb = "喜欢"
        object_verb = match.group(3)  # 动宾中的动词
        object_noun = match.group(4)  # 动宾中的名词
        triples.add((subject, verb, f"{object_verb}{object_noun}"))

    return triples

def rule_is_possessive_relation(sentence):
    """规则16：提取 A 是 B 的 C"""
    triples = set()
    pattern = r'(\S+)/({}) 是/v (\S+)/({}) 的/u (\S+)/({})'.format('|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS), '|'.join(NOUN_TAGS))
    matches = re.finditer(pattern, sentence)
    for match in matches:
        subject = match.group(1)
        possessive = f"{match.group(3)}的{match.group(6)}"
        triples.add((subject, "是", possessive))
    return triples



def apply_rules(words):
    """应用所有规则"""
    sentence = to_sentence(words)
    # print('sentence:', sentence)
    results = set()
    results.update(rule_verb_object_relation(sentence))  # 规则1
    results.update(rule_is_relation(sentence))  # 规则2
    results.update(rule_adj_noun_relation(sentence))  # 规则3
    results.update(rule_time_loc_relation(sentence))  # 规则4
    results.update(rule_verb_loc_relation(sentence))  # 规则5
    results.update(rule_verb_time_relation(sentence))  # 规则6
    results.update(rule_has_relation(sentence))  # 规则7
    results.update(rule_include_relation(sentence))  # 规则8
    results.update(rule_own_relation(sentence))  # 规则9
    results.update(rule_need_relation(sentence))  # 规则10
    results.update(rule_cause_relation(sentence))  # 规则11
    results.update(rule_modify_relation(sentence))  # 规则12
    results.update(rule_person_location_label(sentence))  # 规则13
    results.update(rule_food_relation(sentence))  # 规则14
    results.update(rule_like_relation(sentence))  # 规则15
    results.update(rule_is_possessive_relation(sentence))  # 规则16
    return results

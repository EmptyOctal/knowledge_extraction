import jieba.posseg as pseg

def segment_and_tag(text):
    """对文本进行分词和词性标注"""
    words = pseg.cut(text)
    return [(word, flag) for word, flag in words]
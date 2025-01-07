import jieba
import jieba.posseg as pseg

def segment_and_tag(text):
    """对文本进行分词和词性标注"""
    words = pseg.cut(text)  # 分词并标注词性
    return [(word, flag) for word, flag in words]

import pandas as pd
from extractor import extract_knowledge
from storage import save_to_neo4j, save_to_file

def read_text_from_csv(file_path, text_column):
    """
    从 CSV 文件的指定列逐行读取内容。
    :param file_path: CSV 文件路径
    :param text_column: 包含正文内容的列名
    :return: 正文内容列表
    """
    df = pd.read_csv(file_path, encoding='gbk') # encoding为文件编码格式
    return df[text_column].dropna().astype(str).tolist()

def read_text_from_dir(dir_path):
    """
    从指定目录下的所有文件读取文本内容。
    :param dir_path: 目录路径
    :return: 正文内容列表
    """
    pass


if __name__ == '__main__':
    csv_file = 'D:/CodeField/knowledge_extraction/demo_data.csv'
    text_column = '正文'
    texts = read_text_from_csv(csv_file, text_column)
    result = []
    tot = 0
    for text in texts:
        tot += 1
        if tot >= 10:
            break
        knowledge = extract_knowledge(text)
        result.extend(knowledge)
        print(f"处理正文：{text}")
        for triple in knowledge:
            print(triple)
    
    # 保存结果到 Neo4j 数据库
    save_to_neo4j(result, uri="bolt://localhost:7687", user="neo4j", password="passw0rd", database="neo4j")
    # 保存结果到文件
    save_to_file(result, 'knowledge.json')
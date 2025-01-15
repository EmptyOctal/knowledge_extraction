import json

def save_to_file(triples, filename='knowledge.json'):
    """保存三元组到文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(triples, f, ensure_ascii=False, indent=4)

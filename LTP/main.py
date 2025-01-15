import os
from extractor import extract_knowledge
from storage import save_to_file

def read_all_md_files(directory):
    """
    从指定目录读取所有.md文件的内容。
    """
    text = ""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text += f.read() + '\n'  # 将文件内容累加
    return text

if __name__ == '__main__':
    # 指定目录路径
    directory = 'F:/浏览器下载/rmrb-master/rmrb-master/7z/1989年09月'

    # 读取所有.md文件内容
    text = read_all_md_files(directory)

    # 知识抽取
    knowledge = extract_knowledge(text)
    # print("提取的知识：")
    # for triple in knowledge:
    #     print(triple)

    # 保存结果
    # save_to_file(list(knowledge))

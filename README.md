# knowledge_extraction

jieba版项目结构
```bash
jieba/
├── main.py             # 主程序入口
├── preprocessor.py     # 文本预处理模块
├── segmenter.py        # 分词与词性标注模块
├── rules/              # 规则集
│   ├── base_rules.py   # 基础规则实现
│   ├── additional_rules.py  # 可扩展规则
├── extractor.py        # 知识抽取逻辑
├── storage.py          # 知识存储模块
└── data.txt       # 测试文本
```
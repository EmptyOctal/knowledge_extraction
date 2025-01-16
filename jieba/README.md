因jieba的词性标注效果欠佳，本版块暂未启用，等待后续更新维护。
将需要测试的文本data.txt放在本目录下，随后运行main.py即可使用。

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
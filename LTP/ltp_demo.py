import torch
from ltp import LTP
from segmenter import segment_and_tag
# ltp = LTP("D:/LTP/legacy")
# with open('data.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# result = ltp.pipeline(["我喜欢吃fish"], tasks = ["cws", "pos"])
# print(result.cws)
# print(result.pos)

segment_and_tag("我喜欢吃KFC")
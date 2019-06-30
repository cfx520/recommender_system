#coding:utf-8
from collections import defaultdict
import jieba.posseg
"""sentence='我喜欢深圳世界之窗'
w1=jieba.cut(sentence,cut_all=False)
for i in w1:
    print i"""
sentence='我喜欢深圳世界之窗'
d=defaultdict(int)
for k in sentence:
    d[k]+=1
print list(d.items())
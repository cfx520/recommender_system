#encoding:utf-8

#author cfx
"""
计算相似度
"""

items_tags={'python':{'basic language':2,'very good':3,'基础':3},'java入门':{'基础':3,'入门':5,'编程':1}
    ,'python_data':{'数据':2,'学习下python数据处理':3},'bigdata':{'很棒，些许了':4,'很不错':5}}
import math
def ConsineSim(item_tages,i,j):
    ret=0
    for b,wib in item_tages[i].items():
        if b in item_tages[j]:
            ret+=wib*item_tages[j][b]
    ni,nj=0,0
    for b,w in item_tages[i].items():
        ni+=w*w
    for b,w in item_tages[j].items():
        nj+=w*w
    if ret==0:
        return 0
    return ret/math.sqrt(ni*nj)
print ConsineSim(items_tags,'python','java入门')

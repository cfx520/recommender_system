#coding:utf-8
#author cfx
"""import jieba
from wordcloud import wordcloud
import matplotlib.pyplot as plt
jieba.load_userdict("news.txt")
word='美媒称，鉴于全球石油市场过度供给的情况，中国原油需求下滑是其首要担忧之一。过量生产拉低了石油价格，但是中国过去一年左右的疲弱需求引发了缓慢的回弹。'
cons=jieba.cut(word)
cons2=jieba.cut(word)
text=''.join(cons)
text_count={}
for i in cons2:
    if i in text_count:
        text_count[i]+=1
    else:
        text_count[i]=1
wordclouds=wordcloud(font_path="simhei.ttf",background_color="black").generate(text)
plt.imshow(wordclouds)
plt.axis('off')
plt.show()"""
def a(num):
    strs='first'
    for i in range(num):
        strs+=str(i)
    return strs
print a(4)

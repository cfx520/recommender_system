#coding:utf-8
#author :cfx
import random,math
##切割数据
def split_file(file):
    fin=open(file)
    train=open('E:\\tableau\\ml-1m\\train_10.txt','ab')
    test=open('E:\\tableau\\ml-1m\\test_10.txt','ab')
    while True:
        line=fin.readline()
        if line!='':
            li=random.randint(1,100)
            if li<=10:
                train.write(line)
            else:
                test.write(line)
        else:
            break
    train.close()
    test.close()

"""
获得训练数据
"""
def getTraindata():
    return open('E:\\tableau\\ml-1m\\train_1.txt')
##jaccard 相似度算法
##交集除以并集
def simJaccard(itemsA,itemsB):
    setA=set(itemsA)
    setB=set(itemsB)
    ##交集
    common=setA.intersection(setB)
    if common.__len__()==0:
        return 0.0
    ##并集
    all=setA.union(setB)
    ##相似度
    sim=float(common.__len__())/all.__len__()
    return sim

###余弦相似度
##交集/sqrt(集合的乘积)
def simCos(itemsA,itemsB):
    setA=set(itemsA)
    setB=set(itemsB)
    common=setA.intersection(setB)
    if common.__len__()==0:
        return 0.0
    bot=math.sqrt(setA.__len__()*setB.__len__())
    sim=float(common.__len__())/bot
    return sim

"""
john 相似度算法
对商品的流行度进行惩罚
"""
###得到用户和商品的映射
def getUserToItems():
    file=getTraindata()
    UserToItem={}
    while True:
        line=file.readline()
        if line!="":
            s=line.split('::')
            #print s[1]
            uid=s[0]
            vid=s[1]
            if uid in UserToItem:
                UserToItem[uid].append(vid)
            else:
                UserToItem[uid]=[vid]
        else:
            break
    return UserToItem
###计算用户相似度矩阵
def SimMatrix():
    ##得到用户和商品之间的映射
    userToItems=getUserToItems()
    M={}
    for u,itemsU in userToItems.items():
        for v,itemsV in userToItems.items():
            if u<v:
                if u not in M.keys():
                    M[u] = {}
                if v not in M.keys():
                    M[v]={}
                rat=simCos(itemsU,itemsV)
                M[u][v]=rat
                M[v][u]=rat
    M2={}
    for k,v in M.items():
        M2[k]=sorted(v.items(),key=lambda e:e[1],reverse=True)
    return M2
"""#得到商品和用户之间的映射
def getItems():
    fin=open('')
    Items={}
    while True:
        line=fin.readline()
        if line!="":
            r=line.split('::')
            a=r[0]
            b=[1]
            if a in Items:
                Items[a].append(b)
            else:
                Items[a]=[b]
        else:
            break
    return Items
###计算用户相似度矩阵
##{1:{2:0.3,3:0.4}}
def simItemMatrix():
    Matrix={}
    Items=getItems()
    for u,itemsu in Items.items():
        for v,itemsv in Items.items():
            if u<v:
                if u not in Matrix.keys():
                    Matrix[u]={}
                if v not in Matrix.keys():
                    Matrix[v]={}
                ratio=simCos(itemsu,itemsv)
                Matrix[u][v]=ratio
                Matrix[v][u]=ratio
    return Matrix
"""
"""
计算用户对物品的偏好
1.计算与用户最相似的K个用户
2.在这K个用户找出与物品i交互过的用户
3.相似用户的相似度加和
"""
def preUserItems(u,i,k):
    pref=0.0
    #k个相似用户数
    Kusers=SimMatrix()[u][:k]
    print Kusers
    #用户和物品映射集合
    userItems=getUserToItems()
    print userItems
    for t in Kusers:
        if i in userItems[t[0]]:
            pref+=t[1]
    return pref
"""
基于用户的协同过滤推荐算法
"""
def recommentUserCF(u,k):
    recommentDict={}
    #拿到最相似的K个用户
    Kusers=SimMatrix()[u][:k]
    #拿到用户对应的商品列表
    items=getUserToItems()
    for v,simv in Kusers:
        for vi in items[v]:
            if vi not in items[u]:
                if vi not in recommentDict.keys():
                    recommentDict[vi]=0.0
                recommentDict[vi]=recommentDict[vi]+simv
    return sorted(recommentDict.items(),key=lambda e:e[1],reverse=True)

if __name__ == '__main__':
    #file='E:\\tableau\\ml-1m\\ratings.dat'
    #split_file(file)
    #print [1,2,3]&[2,3,5]
    #print SimMatrix()
    """a={
        1:{2:0.2,3:0.3,4:0.1},
        2:{1:0.2,3:0.1,4:0.2},
        3:{1:0.3,2:0.1,4:0.13},
        4:{1:0.1,2:0.2,3:0.13}
    }
    r=sorted(a[3].items(),key=lambda e:e[1],reverse=True)
    print r"""
    print recommentUserCF('5',2)


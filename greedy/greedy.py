#!/usr/bin/python
#coding=utf-8

# 0 - 1 package problem 
# 每个物品只能选一次
# 背包最多承受的重量是max_package_size
# 要求背包最大价值化
# greedy algorithm

import math

class tagObject:
    weight = 0
    price = 0
    priority = 0.0
    status = 0  #0 未选中  1 已选中 2 已经不可选

max_package_size = 150

w = [35, 30, 60, 50, 40, 10, 25] # w 代表第i个包裹重量
p = [10, 40, 30, 50, 35, 40, 30] # p 代表第i个包裹价值
count = len(w)
# [] 这种数据结构是list ， 相对应的还有另一种数据结构array， array的性能和存储量更好，array支持array/n
# list更常用。

def runAlgorithm():
    tagObjectList = []
    for i in range(0, count):
        obj = tagObject()
        obj.weight = w[i]
        obj.price = p[i]
        obj.priority = (obj.price * 1.0) / obj.weight
        print("weight = " + str(obj.weight) + " price = " + str(obj.price), "priority = " + str(obj.priority))
        tagObjectList.append(obj)

    greedyAlgo(tagObjectList)


def tagListCompare(x, y):
    compare = (y.priority - x.priority)
    intCompare = 0
    if compare > 0:
        # > 0则向上取整
        intCompare = (int)(math.ceil(compare))
    else:
        # < 0则向下取整
        intCompare = (int)(math.floor(compare))
    
    return intCompare

# 贪心算法策略，按 价格/重量 算出权重，按照权重排序，即可以算出最优解
def greedyAlgo(tagObjectList):
    # tagObjectList 排序算法
    sortedTagObjectList = sorted(tagObjectList, cmp=tagListCompare)

    totalWeight = 0
    totalPrice = 0
    index = 0
    for i in range(0, count):
        tempWeight = sortedTagObjectList[i].weight + totalWeight

        if tempWeight > max_package_size:
            # print("over max weigth")
            continue

        index = i
        # 计算目前的总重量
        totalWeight = tempWeight
        # 标记状态
        sortedTagObjectList[i].status = 1
        # 计算总价值
        totalPrice += sortedTagObjectList[i].price
    
        print(sortedTagObjectList[i].weight, sortedTagObjectList[i].price,  sortedTagObjectList[i].priority, "index = " + str(i))
    

    # print result
    print("total weight =" + str(totalWeight),  "total price = " + str(totalPrice))

runAlgorithm()


# result
# (10, 40, 4.0, 'index = 0')
# (30, 40, 1.3333333333333333, 'index = 1')
# (25, 30, 1.2, 'index = 2')
# (50, 50, 1.0, 'index = 3')
# (35, 10, 0.2857142857142857, 'index = 6')
# ('total weight =150', 'total price = 170')
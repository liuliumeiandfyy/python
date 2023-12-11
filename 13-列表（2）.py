'''
lst = [2, 5, 6, 7, 8, 9, 9]
请写程序完成下列操作
    1、在列表的末尾增加元素 15
    2、在列表的中间位置插入元素20
    3、将列表[2, 5, 6]合并到lst中
    4、移除列表中索引为3 的元素
    5、翻转列表里的所有元素
    6、对列表的元素进行排列，从小到大一次，从大到小一次
'''
lst = [2, 5, 6, 7, 8, 9, 9]
# 在列表的末尾增加元素 15
lst.append(15)
print('1、', lst, end='\n')
# 在列表的中间位置插入元素20
lst.insert(len(lst)//2, 20)
print('2、', lst, end='\n')
# 将列表[2, 5, 6]合并到lst中
lst.extend([2, 5, 6])
print('3、', lst, end='\n')
# 移除列表中索引为3 的元素
lst.pop(3)
print('4、', lst, end='\n')
'''
lst = [2, 5, 6, 7, 20, 8, 9, 9, 15, 2, 5, 6]
del lst[3]
print('4、', lst, end='\n')
'''
# 翻转列表里的所有元素
lst.reverse()
print('5、', lst, end='\n')
# 对列表的元素进行排列，从小到大一次，从大到小一次
# .sort()
lst.sort()
print('6、', lst, end='\n')
# .reverse()
lst.reverse()
print('6、', lst, end='\n')
# 内置 sorted()  False:升序  True:降序
print('6、', sorted(lst, reverse=False), end='\n')
print('6、', sorted(lst, reverse=True), end='\n')

'''
dict = {'语文': 95, '数学': 99, '英语': 100}，用程序解答下面题目
    1、字典的长度是多少
    2、请修改‘数学’这个 key 对应的 value 值为98
    3、删除英语这个 key
    4、增加一个 key-value 对，key 值为物理，value 值是90
    5、获取所有的 key 值，存储在列表里
    6、判断 python 这个 key 是否在字典中
    7、获得字典里所有 value 的和
    8、获取字典里最大的 value
    9、获取字典里最小的 value
'''
dict = {'语文': 95, '数学': 99, '英语': 100}
# 字典的长度是多少
print('1、该字典的长度是：', len(dict), end='\n')
# 请修改‘数学’这个 key 对应的 value 值为98
dict['数学'] = 98
print('2、', dict, end='\n')
# 删除英语这个 key

# del dict['英语']
dict.pop('英语')
print('3、删除英语 key 后：', dict, end='\n')

# 增加一个 key-value 对，key 值为物理，value 值是90
dict['物理'] = 90
print('4、增加新键-值：', dict, end='\n')

# 获取所有的 key 值，存储在列表里
print('5、获取值后，储存在列表里：', list(dict.keys()), end='\n')

# 获取所有的 value 值，存储在列表里
print('5、获取值后，储存在列表里：', list(dict.values()), end='\n')

# 判断 python 这个 key 是否在字典中  用 in
if 'pyhon' in dict:
    print('6、', True)
else:
    print('6、',False)

# 获取字典里最大的 value
print('7、', max(dict.values()))

# 获取字典里最小的 value
print('8、', min(dict.values()))
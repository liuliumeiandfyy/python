# 有以下列表： li = [' ','你','好','\n','hello','world',' '],处理成以下结果
# 1、把列表里面的内容拼接成一个字符串
# 2、把字符串前后的空格去掉

li = [' ', '你', '好', '\n', 'hello', 'world', ' ']
# 输出结果的类型--str

# （1）使用“+”拼接内容
print(li[1]+li[2]+li[3]+li[4]+li[5])    # 列表当中的取值+字符串的拼接

# （2）使用 ''.join() 进行拼接
print(''.join(li).strip())
# 定义两个变量如下：
s1 = "hello"
s2 = "world"

# (1)
# 一个print输出s1，s2占2行, 使用格式化输出变量之间添加“\n”
print(f'{s1}\n{s2}')

# （2）
# 一个print输出s1，s2占2行，使用sep=参数
print(s1, s2, sep="\n")


# 两个print输出“s1********s2”
print(s1, end='***************')
print(s2)




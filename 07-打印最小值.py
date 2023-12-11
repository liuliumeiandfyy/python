# input输入的为字符串，需要使用int转换为整形
a = int(input("请输入数字1："))
b = int(input("请输入数字2："))
c = int(input("请输入数字3："))

# （1）
# 将输入的内容存入一个列表之内
num = [a, b, c]

# min()函数找出列表内的最小值
print(min(num))

# （2）
# 不用列表，直接使用min()函数输出
print(min(a, b, c))

# （3）
# input输入使用float，将字符串转换为浮点数
a = (input("请输入数字1："))
b = (input("请输入数字2："))
c = (input("请输入数字3："))
print(min(float(a), float(b), float(c)))

# （4）
# 在输出中
a = (input("请输入数字1："))
b = (input("请输入数字2："))
c = (input("请输入数字3："))
print(min(int(a), int(b), int(c)))


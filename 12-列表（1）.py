'''
输入个人信息，有以下要求
    1、用户输入个人信息
    2、将这些个人信息存放在列表当中
    3、将家庭地址改为广东
    4、采用切片方式同时输出姓名、年龄
'''
name = input('请输出姓名：')
sex = input('请输入性别：')
age = input('请输入年龄：')
ha = input('请输入家庭住址：')
li = [name, sex, age, ha]      #不能将这一整段代码放入print中，报错
                               # print(li = [name, sex, age, ha])TypeError: 'li' is an invalid keyword argument for print()
                               # print(li[name, sex, age, ha])TypeError: list indices must be integers or slices, not tuple

print(li)
# 将家庭地址改为广东
li[3] = '广东'
print(li)
# 采用切片方式同时输出姓名
print(li[0:3:2])
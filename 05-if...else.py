# 输入一个成绩，进行判断
# （1）if...else判断
# 要输入的成绩是整形，而input是字符串，需要用int将输入的内容转换成整形
ach = int(input('请输入你的成绩：'))
if ach >= 60:
    print("恭喜你，成绩及格")
else:
    print("成绩不及格，下次努力哦")

# （2）三目运算
ach = int(input('请输入你的成绩：'))
ach = print('恭喜你，成绩及格') if ach >= 60 else print('成绩不合格，再次努力哦')

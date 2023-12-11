name = input("请输入姓名：")
list_num = input("请输入身份证号码：")

# 对于身份证取值使用倒序-1，从后往前数
print(name, list_num[-1])

# 身份证正序取值
print(name, list_num[len(list_num)-1])
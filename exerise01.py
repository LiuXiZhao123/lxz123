# #1.创建空元祖
# t01=()
# t01=tuple
# #2.创建具有默认值的元组
# t01=(1,2,3)
# t01=1,2,3
# t01=tuple("abc")
#
# t01=(1,2,[3,4])
# print(t01)
#
# #3.元组元素不能修改
# #t01[0]＝１　错误
# #修改的数列表元素
# t01[2][0]="a"
# print(t01)
# t01=(1,3,5,7,8,10,12)
# t02=(4,6,9,11)
# sum=0
# #计算某月某日数这一年的第几天
# month=int(input("请输入月份"))
# day=int(input("请输入日期"))
# for num in range(1,month):
#     if num in t01:
#         sum+=31
#     if num in t02:
#         sum+=30
#     if num==2:
#         sum+=28
# result=sum+day
# print(result)

day=(31,28,31,30,31,30,31,31,30,31,30,31)
i =int(input("请输入月份："))
result=day[i-1]
print(result)
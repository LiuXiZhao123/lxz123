# 作业1
# season={"春":"1月2月3月","夏":"4月5月6月","秋":"7月8月9月","冬":"10月11月12月"}
# answer=input("请输入季节")
# print(season[answer])


#作业２在控制台中获取一段文字，
#打印这个文字中出现的字符以及次数。
# result=[]
# item=str(input("请输入一段字符"))
# #打印这个文字中出现的字符以及次数。
# for i in item:
#     num=item.count(i)
#     print(i,num)


# 游戏：      石头    剪刀   布
# 在控制台中获取：0    1    2，代表石头剪刀布。
# 根据游戏规则，显示：平局、胜利、失败。
# import random
# i=random.randint(0,2)
# item=("石头","剪刀","布")
#
# win=(("石头","剪刀"),("布","石头"),("剪刀","布"))
# while True:
#     player=int(input("请输入0，1，2代表石头剪刀布"))
#     player1=item[player]
#     i1=item[i]
#     i = random.randint(0, 2)
#     list=(player1,i1)
#     if i1==player1:
#         print(i1,"平局")
#     elif list in win:
#         print(i1,"赢了")
#     else:
#         print(i1,"输了")

# d01={}
# for item in range(1,6):
#     d01[item]=item**2
# d01={item:item**2 for item in range(1,6)}
# print(d01)
#
# list01=["zs","wlw","tarena"]
# d01={key:len(key)for key in list01}
# # print(d01)
# list01=[101,102,103]
# list02=["zs","ls","ww"]
# d02={list01[i]:list02[i] for i in range(3)}
# print(d02)






# list=set()
# count=0
# while True:
#     str_q = str(input("请输入内容，如果输入为空字符，则退出"))
#     if str_q=="":
#         break
#     count += 1
#     list.add(str_q)
#     print(count,list)
#
# manger={"曹操","刘备","孙权"}
# technologist={"曹操","刘备","张飞","关羽"}
#
# print("既是经理夜色技术员：",manger & technologist)
#
#
# print("是经理但不是计算员",manger - technologist)
#
# print("数技术员但不是经理",technologist - manger)
#
# print("张飞是经理吗",("张飞"in manger))
#
# print("身兼一职的有",manger ^ technologist)
#
# print("经理和及技术共有多少人",len(manger | technologist))

#
# for l in range(5):
#     for r in range(4):
#         if l%2==0:
#          print("*",end="")
#         else:
#          print("#",end="")
#     print()

# list=[range(4)]
# for b in range(4):
#     for i in range(4,0,-1):
#         print("*",end="")
#     print()





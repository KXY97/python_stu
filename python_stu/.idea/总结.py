# 质数之和
# a = 0
# for i in range(2,101):
#     for j in range(2,i+1):
#         if i % j == 0:
#             break
#     if i == j:
#         a += i
# print(a)



# 因数之和等于本身
# for i in range(2,1001):
#     a = 0
#     for j in range(1,i):
#         if i % j == 0:
#             a+=j
#     if i == a:
#         print(a) 、


# 阶乘之和
# a = int(input('>>>'))
# sum = 0
# b = 1
# for i in range(1,a+1):
#     b *= i
#     sum += b
# print(sum)


# 打印第一和第二大的数
# a = input('>')
# a = a.split(',')
# b = a.copy()
# b = list(set(b))
# b.sort()
# c = a.count(b[-1])
# q = a.count(b[-2])
# print('{}'.format(b[-1])*c)
# print('{}'.format(b[-2])*q)


# 去重排序
# a = input('>>>')
# a = a.split(',')
# b = []
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# b.sort()
# print(b)


# 字符串不用int变整数
# a = input('>>>')
# a = a[::-1]
# sum = 0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j) == a[i]:
#             sum += j*10**i
# print(type(sum))


# 十进制转十六进制
# a = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# b = input('>>>')
# b = int(b)
# s = []
# while True:
#     x = b%16
#     b = b//16
#     s.append(a[x])
#     if b == 0:
#         break
# s.reverse()
# m = s[0]
# for i in range(1,len(s)):
#     m += s[i]
# print(m)


# 九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()


# 一加到一百
# sum = 0
# a=1
# while a < 101:
#     sum += a
#     a+=1
# print(sum)=


# 判断回文
# a = input('>>>')
# for i in range(len(a)):
#     if a[i] != a[-i-1]:
#         print('不是回文')
#         break
#     else:
#         print('是回文')
#         break


# TXT到Excel
# import xlwt
# import xlrd
# f = xlwt.Workbook('aaa.xls')
# sheet = f.add_sheet('9')
# s = open('a.txt','r',encoding='utf-8')
# a = s.readlines()
# print(a)
# for i,j in enumerate(a):
#     j = j.replace('\n','').split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
# f.save('aaa.xls')


#Excel到TXT
# import xlwt
# import xlrd
# f = xlrd.open_workbook('aaa.xls')
# k = open('a.txt','w',encoding='utf-8')
# sheet = f.sheets()[0]
# for i in range(sheet.nrows):
#     a = (sheet.row_values(i))
#     a = ''.join(a)
#     k.write('{}\n'.format(a))

















# import xlrd
# import pymysql
# con = pymysql.connect(host = '192.168.0.60',
#                       port = 3306,
#                       user 'root',
#                       password = '123456',
#                       charset = 'utf8')
# a = con.cursor()
# f = xlrd.open_workbook('douban.xls')
# c = f.sheet()[0]
# for i in range(c.nrows):
#
#     if i == 0:
#         n = c.row_values(i)
#         a.execute('use python_k;')
#         a.execute('create table dushu({} char(255),{} char(255),{} char(255),{} char(255))'.format(n[0],n[1],n[2],n[3]))
#     else:
#         n = c.row_values(i)
#         a.execute('insert into dushu values("{}","{}","{}","{}");'.format(n[0],n[1],n[2],n[3]))
#         a.execute('select * from dushu;')
#         print(a.fetchall())
#         con.close()
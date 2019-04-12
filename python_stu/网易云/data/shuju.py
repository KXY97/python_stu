import xlrd

def duqu_shuju_shouye(self):
    shuju = []
    f = xlrd.open_workbook('D:\python文件\网易云\data\shu.xlsx')
    sheet = f.sheets()[0]
    num = sheet.nrows

    for i in range(num):
        if i == 0:
            continue
        else:
            shuju.append(sheet.row_values(i))

    return shuju
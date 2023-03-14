# ------------------------------------
# -*- coding = utf-8 -*-
# @Time : 2021/6/22 12:44
# @Author ：chc_stars
# @File : data_class_handle.py
# @Software : PyCharm 

# --------------------------------------
import xlrd

# def data_transfor():
bok= xlrd.open_workbook('data\\测试-初赛.xlsx') #打开Excel

# lists = ['财经','房产','教育','科技','军事','汽车','体育','游戏','娱乐']
textt = ""
textt += 'label'
textt += '\t'
textt += 'content'
textt += '\n'


sht= bok.sheet_by_name('类别')

print(sht.nrows)
print(sht.ncols)

for i in range(1,sht.nrows):


    cell_title = sht.cell(i,2).value
    cell_content = sht.cell(i,3).value
    titles = cell_title.replace('\n', '').replace('\r', '')
    contents = cell_content.replace('\n', '').replace('\r', '').replace(' ','').replace('\t','')

    # textt += cell_num
    # textt += '\t'
    textt += titles
    textt += ':'
    textt += contents
    textt += '\n'

f = open('data/测试-初赛.txt', 'w', encoding='utf-8')
f.write(textt)
f.close()













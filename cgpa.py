import xlrd  #Extracts data from Excel spreadsheets
import xlwt  #generates spreadsheet files
from openpyxl import Workbook   #to open xl files
from openpyxl import load_workbook

#convert() will convert the grades to points & return respective points
def convert(value):
    if value == 'O' :
        return 10
    elif value == 'S':
        return 9
    elif value == 'A':
        return 8
    elif value == 'B':
        return 7
    elif value == 'C':
        return 6
    elif value == 'D' :
        return 5
    elif value == 'F' or value == 'ABSENT' :
        return 0

#calculate() is to choose respective results document  and calculate GPA
def calculate(rollno,sem1):
    if sem1 =='1-1':
        books = [xlrd.open_workbook("1_1.xlsx")]
    elif sem1 == '1-2':
        books = [xlrd.open_workbook("1_2.xlsx")]
    elif sem1 == '2-1':
        books = [xlrd.open_workbook("2_1.xlsx")]
    elif sem1 == '2-2':
        books = [xlrd.open_workbook("2_2.xlsx")]
    elif sem1 == '3-1':
        books = [xlrd.open_workbook("3_1.xlsx")]
    flag=0
    book = books[0]
    sheet = book.sheet_by_index(0) 
    sum=0
    ret = []
    for row in range(sheet.nrows):
        if sheet.cell_value(row,0) == rollno :    
            ret.append([sheet.cell_value(row,2),sheet.cell_value(row,3)])
            grade = convert(sheet.cell_value(row,3))
            credit = sheet.cell_value(row,4)
            sum += grade*credit
            flag = 1
            
    if flag == 1:
        res = sum/21
        ret.append(res)
        return ret   
    else:
        return -1

import openpyxl

path="E:\\pythonProject\\pawanOnlineSeleniumPython\\xlData1.xlsx"

workbook=openpyxl.load_workbook(path)
Sheet2 = workbook.get_sheet_by_name('Sheet2')

for r in range(1,6):
    for c in range(1,4):
        Sheet2.cell(row=r,column=c).value="welcome2"

workbook.save(path)

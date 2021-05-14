import openpyxl as xl
wb = xl.load_workbook('testXML.xlsx') # loads the xml
sheet = wb['Sheet1'] #accesses the sheet
cell = sheet['a1']
cell = sheet.cell(1,1)

for row in range(2, sheet.max_row + 1):
   cell = sheet.cell(row, 3)
   corrected_price = cell.value * 0.9
   corrected_price_cell = sheet.cell(row, 4)
   corrected_price_cell.value = corrected_price

wb.save('test2XML.xlsx')


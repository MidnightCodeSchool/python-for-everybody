import gspread

gc = gspread.service_account('/Users/m/Projects/python-for-everybody/class-05/test-sloth-7c698a48adde.json')

sh = gc.open("MyNewSheet")

sh.sheet1.get('A1')
sh.sheet1.update('A1', [[1234]])
sh.sheet1.append_row([1, 2, 3, 4])
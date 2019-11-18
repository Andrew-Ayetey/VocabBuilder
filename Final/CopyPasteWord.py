import websterApi
from openpyxl import load_workbook
wb2 = load_workbook('test.xlsx')


ws1 = wb2['New Title']

columns = ws1.columns


testWord = ws1['A2']

wordColumn = ws1['A']

for x in wordColumn:
    if x.value == "Word":
        pass
    else:
        print(x)
        print(x.value)
#         definition_locaiton = "B" + str(x.row)
#         ws1[definition_locaiton] = x.value
#         print(ws1[definition_locaiton].value)

# wb2.save('test.xlsx')

def define_word(cell):
    word = cell.value
    return word

def paste_defintion(cell):
    word = define_word(cell)
    definitionLocation = "B" + str(cell.row)
    ws1[definitionLocation] = define_word(word)
    wb2.save('test.xlsx')
    pass

paste_defintion(testWord)
print(ws1['B2'].value)








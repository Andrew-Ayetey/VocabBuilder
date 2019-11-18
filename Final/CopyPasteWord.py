import websterApi
from openpyxl import load_workbook
wb2 = load_workbook('test.xlsx')
ws1 = wb2['New Title']
columns = ws1.columns
testWord = ws1['A2']
wordColumn = ws1['A']

# for x in wordColumn:
#     if x.value == "Word":
#         pass
#     else:

#         print(x)
#         print(x.value)
#         definition_locaiton = "B" + str(x.row)
#         ws1[definition_locaiton] = x.value
#         print(ws1[definition_locaiton].value)

# wb2.save('test.xlsx')

def define_word(word):
    definedWord = websterApi.WebsterWord(word)
    return definedWord

def paste_defintion(cell):
    word = cell.value
    defined = define_word(word)
    definitionLocation = "B" + str(cell.row)
    ws1[definitionLocation] = defined.shortdef[0]
    wb2.save('test.xlsx')
    pass

# newTest = websterApi.WebsterWord('Colonnades')

# print(newTest.wordList)
# print(define_word(testWord.value))
# paste_defintion(testWord)
# print(ws1['B2'].value)
# print(testWord.value)
# print(define_word(testWord))

def addDefinition():
    for x in wordColumn:
        definitionLocation = "B" + str(x.row)
        if x.value == "Word":
            pass
        elif ws1[definitionLocation].value != None:
            print("Definition Present")
        else:
            paste_defintion(x)


addDefinition()








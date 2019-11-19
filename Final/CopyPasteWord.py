import websterApi
import time
from openpyxl import load_workbook
start_time = time.time()
wb2 = load_workbook('test.xlsx')
ws1 = wb2['New Title']
columns = ws1.columns
testWord = ws1['A2']
wordColumn = ws1['A']


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

def paste_pronunciation(cell):
    word = cell.value
    prs = define_word(word)
    prsLocation = "C" + str(cell.row)
    ws1[prsLocation] = prs.prsMw
    wb2.save('test.xlsx')
    pass


def addDefinition():
    for x in wordColumn:
        definitionLocation = "B" + str(x.row)
        if x.value == "Word":
            pass
        elif ws1[definitionLocation].value != None:
            print("Definition Present")
        else:
            print("Definition Updated")
            paste_defintion(x)

def addPronunciation():
    for x in wordColumn:
        prsLocation = "C" + str(x.row)
        if x.value == "Pronunciation":
            pass
        elif ws1[prsLocation].value != None:
            print("Pronunciation Present")
        else:
            print("Pronunciation Updated")
            paste_pronunciation(x)

addDefinition()
addPronunciation()
elapsed_time= time.time() - start_time
print(elapsed_time)








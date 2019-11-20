import excelReader
import websterApi
import time
from openpyxl import Workbook
from openpyxl import load_workbook


vocabFile = input("Please enter vocab file: ")
workbook = load_workbook(vocabFile)
sheetName = input("Please enter sheet name: ")
vocabWorksheet = workbook[sheetName]
wordColumn = vocabWorksheet['A']

def define_word(word):
    definedWord = websterApi.WebsterWord(word)
    return definedWord

def paste_defintion(cell):
    word = cell.value
    defined = define_word(word)
    if defined.found == False:
        print("Word not found in Webster")
        pass
    else:
        definitionLocation = "B" + str(cell.row)
        vocabWorksheet[definitionLocation] = defined.shortdef[0]
        workbook.save('test.xlsx')
    pass

def paste_pronunciation(cell):
    word = cell.value
    prs = define_word(word)
    if prs.found == False:
        print("Pronunciation not found in Webster")
        pass
    else:
        prsLocation = "C" + str(cell.row)
        vocabWorksheet[prsLocation] = prs.prsMw
        workbook.save('test.xlsx')
    pass


def addDefinition():
    for x in wordColumn:
        definitionLocation = "B" + str(x.row)
        if x.value == "Word":
            pass
        elif vocabWorksheet[definitionLocation].value != None:
            print("Definition for " + x.value+ " Present")
        else:
            print("Definition for " + x.value+ " Updated")
            paste_defintion(x)

def addPronunciation():
    for x in wordColumn:
        prsLocation = "C" + str(x.row)
        if x.value == "Pronunciation":
            pass
        elif vocabWorksheet[prsLocation].value != None:
            print("Pronunciation for " +x.value +" Present")
        else:
            print("Pronunciation for " +x.value+ " Updated")
            paste_pronunciation(x)


start_time = time.time()
addDefinition()
addPronunciation()
elapsed_time= time.time() - start_time
print(elapsed_time)



# ws1 = wb2['New Title']
# columns = ws1.columns
# testWord = ws1['A2']
# wordColumn = ws1['A']
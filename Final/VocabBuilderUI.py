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
    try:
        websterApi.WebsterWord(word)
    except:
        KeyError
        print("Something wrong with Dictionary key/object")
        definedWord = websterApi.ProblemWord(word)
        return definedWord
    definedWord = websterApi.WebsterWord(word)
    return definedWord

def paste_defintion(cell):
    word = cell.value
    defined = define_word(word)
    if defined.found == False:
        print("" +word +" not found in Webster")
        pass
    else:
        definitionLocation = "B" + str(cell.row)
        vocabWorksheet[definitionLocation] = defined.shortdef[0]
        workbook.save('test.xlsx')
        print("Definition of "+ word +" updated")
    pass

def paste_defintion_long(cell):
    word = cell.value
    defined = define_word(word)
    if defined.found == False:
        print("" +word +" not found in Webster")
        pass
    else:
        definitionLocation = "D" + str(cell.row)
        vocabWorksheet[definitionLocation] = str(defined.wordDef)
        workbook.save('test.xlsx')
        print("Long Definition of "+ word +" updated")
    pass

def paste_pronunciation(cell):
    word = cell.value
    prs = define_word(word)
    if prs.found == False:
        print(""+ word +" not found in Webster")
        pass
    else:
        prsLocation = "C" + str(cell.row)
        vocabWorksheet[prsLocation] = prs.prsMw
        workbook.save('test.xlsx')
        print("Pronunciation of "+ word +" updated.")
    pass

def paste_quizlet(cell):
    word = cell.value
    quizlet = define_word(word)
    if quizlet.found == False:
        print(""+ word +" not found in Webster")
        pass
    else:
        quizletLocation = "E" + str(cell.row)
        vocabWorksheet[quizletLocation] = "{} ({})".format(quizlet.word, quizlet.prsMw)
        workbook.save('test.xlsx')
        print("Quizlet of "+ word +" updated.")
    pass


def addDefinition():
    for x in wordColumn:
        definitionLocation = "B" + str(x.row)
        if x.value == "Definition":
            pass
        elif vocabWorksheet[definitionLocation].value != None:
            print("Definition for " + x.value+ " Present")
        else:
            paste_defintion(x)

def addPronunciation():
    for x in wordColumn:
        prsLocation = "C" + str(x.row)
        if x.value == "Word":
            pass
        elif vocabWorksheet[prsLocation].value != None:
            print("Pronunciation for " +x.value +" Present")
        else:
            paste_pronunciation(x)

def addDefinitionLong():
    for x in wordColumn:
        definitionLocation = "D" + str(x.row)
        if x.value == "Word":
            pass
        elif vocabWorksheet[definitionLocation].value != None:
            print("Long Definition for " + x.value+ " Present")
        else:
            paste_defintion_long(x)

def quizletFlashCardWord():
    for x in wordColumn:
        wordLocation = "E" + str(x.row)
        if x.value == "Word":
            pass
        elif vocabWorksheet[wordLocation].value != None:
            print("Quizlet Format Found")
        else:
            paste_quizlet(x)


start_time = time.time()
addDefinition()
addPronunciation()
addDefinitionLong()
quizletFlashCardWord()
elapsed_time= time.time() - start_time
print(elapsed_time)



# ws1 = wb2['New Title']
# columns = ws1.columns
# testWord = ws1['A2']
# wordColumn = ws1['A']
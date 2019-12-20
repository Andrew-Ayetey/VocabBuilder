import json
import requests
from websterApi import *


# myWebId = '17e1bacd-ab8e-4924-8c57-5a32357d29d9'

def requestWebsterWord(word, id):
    return requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}'.format(word, id))

# def checkStems(word):
#     stem= 
#     return word + [0]['meta']['stems'][0]

testword = WebsterWord('quick')
print(type(myWebID))
word = 'indirection'
id = myWebID
# print('https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}'.format(word, id))
testWord2 = requestWebsterWord('indirection', myWebID)
print(type(testword.wordDef))
# print(testWord2.json())




import json
import requests


class WebsterWord:
        
    def __init__(self, word, id, response=None, json=None):
        self.word = word
        self.id = id
        self.response = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}'.format(word, id))
        self.json = (self.response).json()
        self.wordList = self.json[0]
        self.shortdef = self.wordList['shortdef']
  
        


# request = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key=17e1bacd-ab8e-4924-8c57-5a32357d29d9')

# wordList = request.json()
# wordDic = wordList[0]
# wordDef = wordDic['def']
# shortdef = wordDic['shortdef']
# hwi = wordDic['hwi']
# meta = wordDic['meta']
# fl = wordDic['fl']
# uros = wordDic['uros']
# et = wordDic['et']


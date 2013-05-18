# -*- coding: UTF-8 -*-
import string

def searchForRepeatedWords(text1, text2):    
    text1Words = ignorePunctuation(text1.split())    
    text2Words = ignorePunctuation(text2.split())    
    return obtainRepeatedWords(text1Words, text2Words)


def ignorePunctuation(text):
    return [''.join(word for word in par if word not in string.punctuation) for par in text]

def obtainRepeatedWords(text1Words, text2Words):
    repeatedWords = set()
    for word in text1Words:
        if word in text2Words:
            repeatedWords.add(word)
    return repeatedWords


text1 = "en un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo"
text2 = "ponte en mi lugar, no tengo mucho tiempo para acordarme de tu nombre"
print (searchForRepeatedWords(text1, text2))

# -*- coding: UTF-8 -*-
def Palindromes(number):
    return str(number) == str(number)[::-1]

print("¿Es palíndromo el número 1234321?: " +str(Palindromes(1234321)))
print("¿Es palíndromo el número 785?: " +str(Palindromes(785)))
print("¿Es palíndromo el número 9?: " +str(Palindromes(9)))
print("¿Es palíndromo el número 1210?: " +str(Palindromes(1210)))
#Numbers can't start with 0 in Python, Syntax error
#print("¿Es palíndromo el número 1234321?: " +str(Palindromes(01210)))
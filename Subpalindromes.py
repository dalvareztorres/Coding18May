# -*- coding: UTF-8 -*-

maxLen = 0

def getLargestSubpalindrome(number):
    stNumber = str(number)
    if len(stNumber) < 3:
        return 0
    if isPalindrome(stNumber):
        return int(stNumber)
    
    maxLen = 0
    largestSubpalindrome = 0;
    n = ""
    for i in range(len(stNumber)):
        for j in range (i, len(stNumber)):
            n = stNumber[i:j+1]
            if isPalindrome(n) and len(n) > maxLen:
                maxLen = len(n)
                largestSubpalindrome = n
                
    if len(str(largestSubpalindrome)) > 2:
        return largestSubpalindrome
    return 0

   
    
def isPalindrome(number):
    return number == number[::-1]

print (getLargestSubpalindrome(1234321))
print (getLargestSubpalindrome(31221790))
print (getLargestSubpalindrome(1232442909))
print (getLargestSubpalindrome(123244909))
print (getLargestSubpalindrome(12331233))
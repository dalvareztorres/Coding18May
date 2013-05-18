def palindromeBaseN(number, base):
    if base == 10:
        return isPalindrome(str(number))
    elif base == 2:
        return isPalindrome(str(bin(number))[2:])
    elif base == 16:
        return isPalindrome(str(hex(number))[2:])
    elif base == 8:
        return isPalindrome(str(oct(number))[2:])
    
    return "Not a valid base"

def isPalindrome(number):
    return number == number[::-1]

print (palindromeBaseN(1234321, 10))
print (palindromeBaseN(1234321, 16))
print (palindromeBaseN(289, 16))
print (palindromeBaseN(1234, 2))
print (palindromeBaseN(273, 2))
print (palindromeBaseN(273, 8))
print (palindromeBaseN(273, 16))


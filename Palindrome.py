def isPalindrome (x):
        if x < 0:
            return False
        numbStr = str(x)
        lists = tuple(int(digit) for digit in numbStr)
        inverted_lists = lists[::-1]
        print(inverted_lists)
        return lists == inverted_lists

x = int(input("Digite o número que você deseja conferir ser palíndromo ou não: "))
print(isPalindrome(x))



"""
Se for feito sem transformar o número em string
if x < 0:
    return False
        
original = x
reversed_num = 0
        
while x > 0:
    digit = x % 10
    reversed_num = reversed_num * 10 + digit
    x //= 10 
        
return original == reversed_num
"""
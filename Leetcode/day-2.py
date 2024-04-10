#greates common divisor of strings

from math import gcd

str1 = "ABCAB"
str2 = "ABC"

if str1+str2 != str2+str1:
    print("")

result = str1[:gcd(len(str1), len(str2))]
print(result)

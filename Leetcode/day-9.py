#  String Compression

# class Solution:
#   def compress(self, chars: List[str]) -> int:
#     ans = 0
#     i = 0

#     while i < len(chars):
#       letter = chars[i]
#       count = 0
#       while i < len(chars) and chars[i] == letter:
#         count += 1
#         i += 1
#       chars[ans] = letter
#       ans += 1
#       if count > 1:
#         for c in str(count):
#           chars[ans] = c
#           ans += 1

#     return ans


# this is my own solution
class Solution:
  def compress(self, chars: List[str]) -> int:
    nu_char = len(chars)

    if nu_char < 2:
        return nu_char
    i = index = 0
    while i < nu_char:
        count = 1
        #chk for dupli and count it
        while i < nu_char -1 and chars[i]==chars[i+1]:
            count += 1
            i += 1

        chars[index] = chars[i] #call for index if next value is !=
        index += 1

        #assign the values to main list not a seperate one
        if count > 1: #i still have a doubt here
            for val in str(count):
                chars[index] = val
                index += 1
        i += 1
    return index

# print(count)
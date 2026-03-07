'''
Valid Palindrome
Easy
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: After removing non-alphanumeric characters, it l
Input: s = "race a car"
Output: false
Explanation: After removing non-alphanumeric characters, it l


'''


s = "race a car"

def is_palindrome(input):
    l, r = 0, len(input)-1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True


print(is_palindrome(s))
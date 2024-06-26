#  Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count = 0
        vowels = ['a','e','i','o','u']
        m_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count+=1
                m_vowels = max(m_vowels,vowel_count)
        i=0
        for j in range(k,len(s)):
            if s[j] in vowels:
                vowel_count+=1
            if s[i] in vowels and k>1:
                vowel_count-=1
            i+=1
            m_vowels = max(m_vowels,vowel_count)
        return min(m_vowels,k)
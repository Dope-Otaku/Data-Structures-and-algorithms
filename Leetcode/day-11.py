# is subsequence

s = "axc"
t = "ahbgdc" 

s, t= list(s), list(t)
for sub in t:
    for io in s:
        if sub == io and sub in s:
            print(True)
        else:
            break

        # class Solution:
        #     def isSubsequence(self, s: str, t: str) -> bool:
        #         sp = tp = 0

        #         while sp < len(s) and tp < len(t):
        #             if s[sp] == t[tp]:
        #                 sp += 1
        #             tp += 1
                
        #         return sp == len(s)
    
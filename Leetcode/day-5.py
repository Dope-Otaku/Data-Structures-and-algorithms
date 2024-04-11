#reverse vowels of a string


#approach was two pointer
s = "hello"
o = list(s)
vowel = set('aeiouAEIOU')
start = 0
end = len(o)-1

while(start<end):
    while(start<end and o[start] not in vowel):
        start += 1

    while(start<end and o[end] not in vowel):
        end -= 1
    
    o[start], o[end] = o[end], o[start]
    start+=1
    end-=1
    print( "".join(o))
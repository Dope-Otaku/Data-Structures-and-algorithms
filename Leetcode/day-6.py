#reverse words in a string

# approach: was easy just split it reverse it and then join it with a space


s = "  hello world  "
r = s.split(" ")
nr = r[::-1]
rr = ' '.join(nr)
print(r)
print(nr)
print(rr)


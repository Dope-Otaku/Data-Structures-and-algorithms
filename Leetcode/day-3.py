# kids with the greatest number of candles

candies = [2,3,4,5,1]
extra_candies = 2
result = []
maximum = max(candies)

for i in range(len(candies)):
    temp = candies[i] + extra_candies
    result.append(temp >= maximum)

print(result)

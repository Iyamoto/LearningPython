import random

def randomList(n):
  s = [0] * n
  for i in range(n):
    s[i] = random.random()
  return s

t = randomList(10000)
#print(t)

numBuckets = 10
buckets = [0] * numBuckets
for i in t:
  index = int(i * numBuckets)
  #buckets[index] = buckets[index] + 1
  buckets[index] += 1

print(buckets)

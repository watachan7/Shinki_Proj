
texts="texts/testidiom.txt"

test_data = open(texts, "r")
lines = test_data.readlines()
arr = [[0 for i in range(3)] for j in range(sum(1 for line in open(texts)))]

num_lines = sum(1 for line in open(texts))
print(num_lines)

for line in lines:
  l = line.split(':')
  arr[0][0] = l[3]
  print(arr[0][0])
  #print(l[0])
  print(l)

test_data.close()

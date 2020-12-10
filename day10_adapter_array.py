def distribution(adapters):
  count = [0, 0, 0]
  count[adapters[0]-0-1] += 1
  for i in range(len(adapters)-1):
    count[adapters[i+1]-adapters[i]-1] += 1
  count[2] += 1
  return count

def countDistinctWays(adapters):
  adapters = [0] + adapters
  f = [0] * len(adapters)
  f[0] = 1
  for i in range(1, len(adapters)):
    for j in range(i-1, -1, -1):
      if adapters[j]+3 < adapters[i]:
        break
      f[i] += f[j]
  return f[-1]

if __name__=="__main__":
  f = open("day10_input1.txt")
  adapters = [int(line) for line in f]
  adapters.sort()
  dis = distribution(adapters)
  print(dis[0]*dis[2])
  print(countDistinctWays(adapters))
  f.close()

def getNthNumber(startings, nth):
  d = {}
  if nth <= len(startings):
    return startings[nth-1]

  for i in range(len(startings)):
    if startings[i] not in d:
      d[startings[i]] = [None, i+1]
    else:
      d[startings[i]] = [d[startings[i]][-1], i+1]
  
  cnt = len(startings)
  recent = startings[-1] 

  while cnt < nth:
    if d[recent][0] == None:
      recent = 0
    else:
      recent = d[recent][1] - d[recent][0]
    cnt += 1
    if recent not in d:
      d[recent] = [None, cnt]
    else:
      d[recent] = [d[recent][-1], cnt]
  return recent

if __name__=="__main__":
  f = open("day15_input1.txt")
  startings = [int(n) for n in f.readline().rstrip().split(",")]
  result1 = getNthNumber(startings, 2020)
  print(result1)
  result2 = getNthNumber(startings, 30000000)
  print(result2)
  f.close()

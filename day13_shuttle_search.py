import sys

"""
ex:
7,13,x,x,59,x,31,19

(7*(k + 0) + 1) % 13 == 0 -> k = 11
(7*(k*13 + 11) + 4) % 59 == 0 -> k = 3
...
(7*(k*13*59*31+10021) + 7) % 19 == 0 -> k = 6
 t  k     b             r  target
"""

def find_earliest_timestamp(tokens):
  t, b, target, r = None, 1, None, 0
  result = 0
  for i in range(len(tokens)):
    if tokens[i] == 'x':
      continue
    num = int(tokens[i])
    if t == None:
      t = num
      continue
    else:
      target = num
    k = 1
    while (t*(k*b+r)+i)%target != 0:
      k += 1
    result = t*(k*b+r)
    r += k*b
    b *= target
  return result

def find_earliest_bus(depart_time, buses):
  result = -1
  earliest_depart_time = sys.maxsize
  for t in buses:
    r = depart_time % t
    earliest = depart_time + t - r
    if earliest < earliest_depart_time:
      earliest_depart_time = earliest
      result = t * (t - r)
  return result

if __name__=="__main__":
  f = open("day13_input1.txt")
  depart_time = int(f.readline())
  tokens = f.readline().split(",")
  #print(tokens)
  buses = [int(n) for n in list(filter(lambda e: e != 'x', tokens))]
  #print(buses)
  result = find_earliest_bus(depart_time, buses)
  print(result)
  result2 = find_earliest_timestamp(tokens)
  print(result2)
  f.close()

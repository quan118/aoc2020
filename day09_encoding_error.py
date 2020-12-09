PREAMBLE_LENGTH = 25

def findOutlawNumber(numbers):
  for i in range(PREAMBLE_LENGTH, len(numbers)):
    n = numbers[i]
    s = set(numbers[i-PREAMBLE_LENGTH:i])
    previous = list(s)
    found = False
    for m in previous:
      s.remove(m)
      if n - m in s:
        s.add(m)
        found = True
        break
    if not found:
      return n
  return None

def findEncryptionWeakness(numbers, target):
  first, last = 0, 1
  while last < len(numbers):
    s = sum(numbers[first:last+1])
    if s < target:
      last += 1
    elif s > target:
      if first < last-1:
        first += 1
      else:
        first += 1
        last += 1
    else:
      return min(numbers[first:last+1]) + max(numbers[first:last+1])
  return None

if __name__=="__main__":
  f = open("day09_input1.txt")
  numbers = []
  for line in f:
    numbers.append(int(line))
  n1 = findOutlawNumber(numbers)
  print(n1)
  n2 = findEncryptionWeakness(numbers, n1)
  print(n2)
  f.close()

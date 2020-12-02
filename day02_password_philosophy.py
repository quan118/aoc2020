def isValid(line):
  policy, letter, password = line.split()
  l, h = [int (ch) for ch in policy.split("-")]
  cnt = password.count(letter[0])
  if cnt < l or cnt > h:
    return False
  return True

def isValid2(line):
  policy, letter, password = line.split()
  l, h = [int (ch) for ch in policy.split("-")]
  cnt = 0
  if password[l-1] == letter[0]:
    cnt += 1
  if password[h-1] == letter[0]:
    cnt += 1
  if cnt == 1:
    return True
  return False

if __name__=="__main__":
  f = open("day02_input1.txt")
  valid_counter = 0
  valid_counter2 = 0
  for line in f:
    if isValid(line):
      valid_counter += 1
    if isValid2(line):
      valid_counter2 += 1

  print(valid_counter)
  print(valid_counter2)
  f.close()

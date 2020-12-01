def find2Numbers(numbers, target):
  for key, value in numbers.items():
    if value <= 0:
      continue
    key2 = target-key
    numbers[key] -= 1
    if key2 in numbers and numbers[key2] > 0 :
      return key * key2
    numbers[key] += 1
  return None

def find3Numbers(numbers):
  for key, value in numbers.items():
    numbers[key] -= 1
    mul = find2Numbers(numbers, 2020-key)
    if mul != None:
      return key * mul
    numbers[key] += 1
  return None

if __name__=="__main__":
  f = open("day01_input1.txt")
  numbers = {}
  for line in f:
    expense = int(line)
    if expense in numbers:
        numbers[expense] += 1
    else:
        numbers[expense] = 1
  print(find2Numbers(numbers, 2020))
  print(find3Numbers(numbers))
  f.close()

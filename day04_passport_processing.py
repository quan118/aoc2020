from functools import reduce
import re
def isValid(passport):
  requiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
  return reduce(lambda a, b: a and b, [field in passport for field in requiredFields])

def intValidator(number):
  regex = re.compile('^[0-9]+$')
  return bool(regex.match(number))

def yearValidator(year, minValue, maxValue):
  if len(year) != 4 or not intValidator(year):
    return False

  number = int(year)
  if number < minValue or number > maxValue:
    return False
  return True

def hgtValidator(hgt):
  if len(hgt) < 4:
    return False
  unit = hgt[-2:]
  height = hgt[:-2]
  if not intValidator(height):
    return False
  number = int(height)
  if unit == 'cm':
    if number < 150 or number > 193:
      return False
    return True
  elif unit == 'in':
    if number < 59 or number > 76:
      return False
    return True
  return False

def hclValidator(hcl):
  regex = re.compile('^#[0-9a-f]{6}$')
  return bool(regex.match(hcl))

def eclValidator(ecl):
  return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pidValidator(pid):
  regex = re.compile('^[0-9]{9}$')
  return bool(regex.match(pid))

def isValid2(passport):
  if 'byr' not in passport or not yearValidator(passport['byr'], 1920, 2002):
    return False

  if 'iyr' not in passport or not yearValidator(passport['iyr'], 2010, 2020):
    return False

  if 'eyr' not in passport or not yearValidator(passport['eyr'], 2020, 2030):
    return False

  if 'hgt' not in passport or not hgtValidator(passport['hgt']):
    return False

  if 'hcl' not in passport or not hclValidator(passport['hcl']):
    return False

  if 'ecl' not in passport or not eclValidator(passport['ecl']):
    return False

  if 'pid' not in passport or not pidValidator(passport['pid']):
    return False

  return True

if __name__=="__main__":
  f = open("day04_input1.txt")
  passports = []
  passport = {}
  for line in f:
    strippedLine = line.rstrip()
    if len(strippedLine) == 0:
      passports.append(passport)
      passport = {}
      continue
    tokens = strippedLine.split()
    for token in tokens:
      k, v = token.split(":")
      passport[k] = v
  passports.append(passport)
  print([isValid(passport) for passport in passports].count(True))
  print([isValid2(passport) for passport in passports].count(True))

  f.close()

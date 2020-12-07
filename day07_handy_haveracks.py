import re

def updateRule(line, rules):
  tokens = re.split("bags?|contain|,", line)
  bag0 = tokens[0].strip()
  rules[bag0] = {}
  for token in tokens[1:]:
    strippedToken = token.strip()
    if len(strippedToken) < 2:
      continue
    matches = re.match("(\d+)\s(\D+)", strippedToken)
    if matches == None:
      continue
    groups = matches.groups()
    if len(groups) < 2:
      continue
    rules[bag0][groups[1]] = int(groups[0])
  return rules

def find(color, bags, rules):
  if bags == {}:
    return False
  if color in bags:
    return True
  for bag, _ in bags.items():
    if bag not in rules:
      continue
    if find(color, rules[bag], rules):
      return True
  return False

def count(color, rules):
  cnt = 0
  for bag, bagsList  in rules.items():
    if color in rules[bag]:
      cnt += 1
    elif find(color, rules[bag], rules):
      cnt += 1
  return cnt

def count2(color, rules):
  if color not in rules or rules[color] == {}:
    return 0
  cnt = 0
  for bagColor, number in rules[color].items():
    cnt += number + number * count2(bagColor, rules)
  return cnt

if __name__=="__main__":
  f = open("day07_input1.txt")
  rules = {}
  for line in f:
    rules = updateRule(line, rules)
  print(count("shiny gold", rules))
  print(count2("shiny gold", rules))
  f.close()

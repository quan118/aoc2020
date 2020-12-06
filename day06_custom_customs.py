from functools import reduce

def count(answers):
  answersSet = set() 
  for answer in answers:
    answersSet.update(answer)
  return len(answersSet)

def count2(answers):
  s = set([c for c in answers[0]])
  for answer in answers[1:]:
    s = s.intersection(answer)
  return len(s)

if __name__=="__main__":
  f = open("day06_input01.txt")
  groupAnswers = []
  answers = []
  for line in f:
    answer = line.rstrip()
    if len(answer) == 0:
      groupAnswers.append(answers)
      answers = []
      continue
    answers.append(answer)
  groupAnswers.append(answers)
  print(reduce(lambda a, b: a+b, [count(answers) for answers in groupAnswers]))
  print(reduce(lambda a, b: a+b, [count2(answers) for answers in groupAnswers]))
  #print(groupAnswers)

  f.close()

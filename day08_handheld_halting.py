def executeOneTime(program):
  acc = 0
  idx = 0
  visited = set()

  while idx not in visited:
    if idx >= len(program):
      return (acc, True)
    op, val = program[idx]
    if op == 'nop':
      visited.add(idx)
      idx += 1
    elif op == 'acc':
      acc += val
      visited.add(idx)
      idx += 1
    elif op == 'jmp':
      visited.add(idx)
      idx += val
  return (acc, False)

def fix(program):
  program2 = list(program)
  for idx in range(len(program)):
    op, val = program[idx]
    if op == 'nop':
      program2[idx] = ('jmp', val)
    elif op == 'jmp':
      program2[idx] = ('nop', val)
    else:
      continue
    state = executeOneTime(program2)
    if state[1] == True:
      return state
    program2[idx] = (op, val)
  return (-1, False)

if __name__=="__main__":
  f = open("day08_input1.txt")
  program = []
  for line in f:
    op, val = line.split()
    program.append((op, int(val)))
  state = executeOneTime(program)
  print(state)
  state2 = fix(program)
  print(state2)
  f.close()

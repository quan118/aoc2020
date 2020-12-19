import copy

def display(state):
  cycles = len(state)//2
  for z in range(len(state)):
    print("z=%d" % (z-cycles))
    for row in state[z]:
      print("".join(row))
  print()

def display_4d(state):
  cycles = len(state)//2
  for w in range(len(state)):
    for z in range(len(state[w])):
      print("z=%d, w=%d" % (z-cycles, w-cycles))
      for row in state[w][z]:
        print("".join(row))
  print()

def count_active_neighbors(x, y, z, state):
  cnt = 0
  for dz in range(-1,2):
    z1=z+dz
    if z1<0 or z1>=len(state):
      continue
    for dy in range(-1,2):
      y1=y+dy
      if y1<0 or y1>=len(state[0]):
        continue
      for dx in range(-1,2):
        x1=x+dx
        if x1<0 or x1>=len(state[0][0]):
          continue
        if dx == 0 and dy == 0 and dz == 0:
          continue
        if state[z1][y1][x1] == '#':
          cnt += 1
  return cnt

def count_active_neighbors_4d(x, y, z, w, state):
  cnt = 0
  for dw in range(-1,2):
    w1=w+dw
    if w1<0 or w1>=len(state):
      continue
    for dz in range(-1,2):
      z1=z+dz
      if z1<0 or z1>=len(state[0]):
        continue
      for dy in range(-1,2):
        y1=y+dy
        if y1<0 or y1>=len(state[0][0]):
          continue
        for dx in range(-1,2):
          x1=x+dx
          if x1<0 or x1>=len(state[0][0][0]):
            continue
          if dx == 0 and dy == 0 and dz == 0 and dw == 0:
            continue
          if state[w1][z1][y1][x1] == '#':
            cnt += 1
  return cnt

def count_active(state):
  cnt = 0;
  for plane in state:
    for row in plane:
      for item in row:
        if item == '#':
          cnt += 1
  return cnt

def count_active_4d(state):
  cnt = 0;
  for w in state:
    for z in w:
      for y in z:
        for x in y:
          if x == '#':
            cnt += 1
  return cnt

def get_full_state(cycles, initial_state):
  new_state = []
  width = len(initial_state[0]) + cycles*2
  height = len(initial_state) + cycles*2
  for z in range(-cycles, cycles+1):
    plane = [['.' for x in range(width)] for y in range(height)]
    new_state.append(plane)
  for h in range(len(initial_state)):
    for w in range(len(initial_state[0])):
      new_state[cycles][h+cycles][w+cycles] = initial_state[h][w]

  return new_state

def get_full_state_4d(cycles, initial_state):
  width = len(initial_state[0]) + cycles*2
  height = len(initial_state) + cycles*2
  new_state = [[[['.' for x in range(width)] for y in range(height)] for z in range(cycles*2+1)] for w in range(cycles*2+1)]
 
  for y in range(len(initial_state)):
    for x in range(len(initial_state[0])):
      new_state[cycles][cycles][y+cycles][x+cycles] = initial_state[y][x]

  return new_state

def advance(state, cycles):
  old = copy.deepcopy(state)
  new = copy.deepcopy(state)
  for i in range(cycles):
    for z in range(len(state)):
      for y in range(len(state[0])):
        for x in range(len(state[0][0])):
          active_neighbors = count_active_neighbors(x, y, z, old)
          if old[z][y][x] == '#'and active_neighbors not in [2, 3]:
            new[z][y][x] = '.'
          elif old[z][y][x] == '.' and active_neighbors == 3:
            new[z][y][x] = '#'
    old = copy.deepcopy(new)
  return old

def advance_4d(state, cycles):
  old = copy.deepcopy(state)
  new = copy.deepcopy(state)
  for i in range(cycles):
    for w in range(len(state)):
      for z in range(len(state[0])):
        for y in range(len(state[0][0])):
          for x in range(len(state[0][0][0])):
            active_neighbors = count_active_neighbors_4d(x, y, z, w, old)
            if old[w][z][y][x] == '#'and active_neighbors not in [2, 3]:
              new[w][z][y][x] = '.'
            elif old[w][z][y][x] == '.' and active_neighbors == 3:
              new[w][z][y][x] = '#'
    old = copy.deepcopy(new)
  return old

if __name__=="__main__":
  f = open("day17_input1.txt")
  initial_state = []
  cycles = 6
  for line in f:
    initial_state.append(list(line.rstrip()))
  full_state = get_full_state(cycles, initial_state)
  final_state = advance(full_state, cycles)
  result1 = count_active(final_state)
  print(result1)
  full_state_4d = get_full_state_4d(cycles, initial_state)
  final_state_4d = advance_4d(full_state_4d, cycles)
  result2 = count_active_4d(final_state_4d)
  print(result2)
  f.close()

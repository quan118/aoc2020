import copy

def countOccupied(seats):
  cnt = 0
  for row in seats:
    for seat in row:
      if seat == '#':
        cnt += 1
  return cnt

def countAdjOccupied(row, col, seats):
  cnt = 0
  dirs = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
  for d in dirs:
    r, c = row + d[0], col + d[1]
    if r >= 0 and c >= 0 and r < len(seats) and c < len(seats[r]) and seats[r][c] == '#':
      cnt += 1
  return cnt

def countOccupiedInDir(row, col, seats, d):
  cnt = 0
  r, c = row + d[0], col + d[1]
  while r >= 0 and r < len(seats) and c >= 0 and c < len(seats[0]):
    if seats[r][c] == '#':
      cnt += 1
      break
    elif seats[r][c] == 'L':
      break
    r += d[0]
    c += d[1]
  return cnt

def count8DirOccupied(row, col, seats):
  cnt = 0
  dirs = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
  for d in dirs:
    cnt += countOccupiedInDir(row, col, seats, d)
  return cnt

def applyRule(seats, maxOccupied, countFunc):
  changed = True
  while changed:
    changed = False
    seats2 = copy.deepcopy(seats)
    for row in range(len(seats2)):
      for col in range(len(seats2[row])):
        occupied = countFunc(row, col, seats2)
        seat = seats2[row][col]
        if seat == 'L' and occupied == 0:
          seats[row][col] = '#'
          changed = True
        elif seat == '#' and occupied >= maxOccupied:
          seats[row][col] = 'L'
          changed = True

  return seats

if __name__=="__main__":
  f = open("day11_input1.txt")
  seats = [list(line.rstrip()) for line in f]
  seats1 = copy.deepcopy(seats)
  seats1 = applyRule(seats1, 4, countAdjOccupied)
  occupied = countOccupied(seats1)
  print(occupied)

  seats2 = copy.deepcopy(seats)
  seats2 = applyRule(seats2, 5, count8DirOccupied)
  occupied = countOccupied(seats2)
  print(occupied)
  f.close()

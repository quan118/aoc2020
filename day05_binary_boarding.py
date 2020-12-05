def getSeatId(line):
  row, rowLo, rowHi = 0, 0, 127
  col, colLo, colHi = 0, 0, 7
  for c in line:
    if c == 'F':
      row = (rowLo + rowHi) // 2
      rowHi = row
    elif c == 'B':
      row = round((rowLo + rowHi + 0.1) / 2)
      rowLo = row
    elif c == 'R':
      col = round((colLo + colHi + 0.1)/2)
      colLo = col
    elif c == 'L':
      col = (colLo + colHi) // 2
      colHi = col
  return row*8+col

if __name__=="__main__":
  f = open("day06_input1.txt")

  maxId = -1
  seatIds = []
  for line in f:
    seatId = getSeatId(line)
    seatIds.append(seatId)
    maxId = max(maxId, seatId)
  print("maxId:%d" % maxId)
  seatIds.sort()
  for i in range(0, len(seatIds)-1):
    if seatIds[i] + 1 != seatIds[i+1]:
      print("my seat id: %d" % (seatIds[i]+1))
      break
  f.close()

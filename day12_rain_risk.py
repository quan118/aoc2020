import math

def doActions2(actions):
  x, y = 0, 0
  wpx, wpy = 10, 1
  for a, v in actions:
    if a == 'F':
      x += v * wpx
      y += v * wpy
    elif a == 'N':
      wpy += v
    elif a == 'S':
      wpy -= v
    elif a == 'E':
      wpx += v
    elif a == 'W':
      wpx -= v
    elif a == 'L' or a == 'R':
      radian = math.pi / 180.0 * v
      if a == 'R':
        radian = -radian
      tx = int(wpx*round(math.cos(radian)) - wpy*round(math.sin(radian)))
      ty = int(wpx*round(math.sin(radian)) + wpy*round(math.cos(radian)))
      wpx, wpy = tx, ty
  return (x, y)

def doActions(actions):
  x, y = 0, 0
  vx, vy = 1, 0
  for a, v in actions:
    if a == 'F':
      x += vx * v
      y += vy * v
    elif a == 'N':
      y += v
    elif a == 'S':
      y -= v
    elif a == 'E':
      x += v
    elif a == 'W':
      x -= v
    elif a == 'L' or a == 'R':
      radian = math.pi / 180.0 * v
      if a == 'R':
        radian = -radian
      tx = int(vx*round(math.cos(radian)) - vy*round(math.sin(radian)))
      ty = int(vx*round(math.sin(radian)) + vy*round(math.cos(radian)))
      vx, vy = tx, ty
  return (x, y)

if __name__=="__main__":
  f = open("day12_input1.txt")
  actions = [(line[0], int(line[1:])) for line in f]
  x, y = doActions(actions)
  print(abs(x) + abs(y))
  x2, y2 = doActions2(actions)
  print(abs(x2) + abs(y2))
  f.close()

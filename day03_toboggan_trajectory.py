def count_tree(map, slope):
  cnt, x, y = 0, 0, 0
  w = len(map[0])
  h = len(map)
  r, d = slope
  x += r
  y += d
  while y < h:
    if map[y][x % w] == '#':
      cnt += 1
    x += r
    y += d
  return cnt

if __name__=="__main__":
  f = open("day03_input1.txt")
  map = [line.rstrip() for line in f]
  slopes = [(1,1), (3,1), (5, 1), (7, 1), (1, 2)]
  result = 1
  for slope in slopes:
    result *= count_tree(map, slope)

  print(result)
  f.close()

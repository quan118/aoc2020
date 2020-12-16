def write(mem, addr, mask, value):
  bits = list(bin(value)[2:].zfill(36))
  for i in range(len(mask)):
    if mask[i] == '0' or mask[i] == '1':
      bits[i] = mask[i]
  mem[addr] = int(''.join(bits), 2)

def write2(mem, addr, mask, value):
  bits = list(bin(addr)[2:].zfill(36))
  xidx = []
  for i in range(len(mask)):
    if mask[i] == '1' or mask[i] == 'X':
      bits[i] = mask[i]
    if mask[i] == 'X':
      xidx.append(i)
  for i in range(pow(2, len(xidx))):
    binaries = bin(i)[2:].zfill(len(xidx))
    for j in range(len(binaries)):
      bits[xidx[j]] = binaries[j]
    addr2 = int(''.join(bits), 2)
    mem[addr2] = value

def execute(lines, writeFn):
  mem = {}
  mask = None
  for line in lines:
    if line.startswith('mask'):
      mask = line.split('=')[1].strip()
    elif line.startswith('mem'):
      left, right = line.split('=')
      addr = int(left.strip()[4:-1])
      value = int(right.strip())
      writeFn(mem, addr, mask, value)
  total = 0
  for _, value in mem.items():
    total += value
  return total

if __name__=="__main__":
  f = open("day14_input1.txt")
  lines = f.readlines()
  total = execute(lines, write)
  print(total)
  total2 = execute(lines, write2)
  print(total2)
  f.close()

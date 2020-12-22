import re

def make_tree(s):
  s = s.rstrip()

  bracket_counter = 0
  first_add_op_idx = -1
  first_mul_op_idx = -1
  for i in range(len(s)-1, -1, -1):
    if s[i] == ')':
      bracket_counter += 1
    elif s[i] == '(':
      bracket_counter -= 1
    elif s[i] == '+' and bracket_counter == 0 and first_add_op_idx == -1:
      first_add_op_idx = i
    elif s[i] == '*' and bracket_counter == 0:
      first_mul_op_idx = i
      break
  if first_add_op_idx == -1 and first_mul_op_idx == -1 and  s[0] == '(' and s[-1] == ')':
    return make_tree(s[1:-1])
  idx = first_mul_op_idx if first_mul_op_idx != -1 else first_add_op_idx
  left = s[0:idx]
  middle = s[idx]
  right = s[idx+1:]
  number_pattern = "^\d+$"
  if re.match(number_pattern, left) != None:
    left = int(left)
  else:
    left = make_tree(left)

  if re.match(number_pattern, right) != None:
    right = int(right)
  else:
    right = make_tree(right)  
  return (left, middle, right)

def cal_tree(root):
  left = 0
  right = 0
  if type(root[0]) == int:
    left = root[0]
  else:
    left = cal_tree(root[0])
  if type(root[2]) == int:
    right = root[2]
  else:
    right = cal_tree(root[2])
  if root[1] == '+':
    return left + right
  elif root[1] == '*':
    return left*right

def evaluate2(s):
  root = make_tree(s)
  return cal_tree(root)

def evaluate(s):
  i = 0
  left = ''
  right = ''
  op= ''
  exp = ''
  state = 'UNKNOWN'
  prev_state = 'UNKNOWN'
  bracket_counter = 0
  first_bracket_idx = -1
  last_closing_bracket_idx = -1
  while i < len(s):
    if state == 'UNKNOWN':
      if s[i] in '0123456789':
        if prev_state == 'OPERATOR':
          prev_state = state
          state = 'RIGHT_NUMBER'
          continue
        elif prev_state == 'UNKNOWN':
          prev_state = state
          state = 'LEFT_NUMBER'
          continue
      elif s[i] == '(':
        prev_state = state
        state = 'PARSE_('
        bracket_counter = 0
        first_bracket_idx = -1
        last_closing_bracket_idx = -1
        continue
      elif s[i] in '*+':
        if prev_state == 'RIGHT_NUMBER':
          tmp = eval(left+op+right)
          left = str(tmp)
          op = ''
          right = ''
        state = 'OPERATOR'
        continue
      elif s[i] == ')':
        if left and op:
          tmp = eval(left+op+str(exp))
          left = str(tmp)
          op = ''
        else:
          left = str(exp)
      elif s[i] == '\n':
        if left and op and right:
          tmp = eval(left+op+right)
          left = str(tmp)
    elif state == 'PARSE_(':
      if s[i] == '(':
        bracket_counter += 1
        if bracket_counter == 1:
          first_bracket_idx = i
      elif s[i] == ')':
        bracket_counter -= 1
        if bracket_counter == 0:
          last_closing_bracket_idx = i
      if bracket_counter == 0:
        exp = evaluate(s[first_bracket_idx+1:last_closing_bracket_idx] + "\n")
        prev_state = state
        state = 'UNKNOWN'
        continue
    elif state == 'LEFT_NUMBER':
      if s[i] in '0123456789':
        left += s[i]
      else:
        prev_state = state
        state = 'UNKNOWN'
        continue
    elif state == 'OPERATOR':
      if s[i] in '+*':
        op = s[i]
      else:
        prev_state = state
        state = 'UNKNOWN'
        continue
    elif state == 'RIGHT_NUMBER':
      if s[i] in '0123456789':
        right += s[i]
      else:
        prev_state = state
        state = 'UNKNOWN'
        continue
    i += 1

  return int(left)

if __name__=="__main__":
  f = open("day18_input1.txt")
  total = 0
  total2 = 0
  for line in f:
    exp = "".join(line.split()) + "\n"
    result = evaluate(exp)
    total += result
    result2 = evaluate2(exp)
    total2 += result2
  print(total)
  print(total2)
  f.close()

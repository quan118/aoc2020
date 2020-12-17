def merge_ranges(ranges):
  ranges.sort()
  merged_ranges = []
  head, tail = ranges[0]
  for r in ranges:
    h, t = r
    if h >= tail:
      merged_ranges.append((head, tail))
      head, tail = h, t
    elif t > tail:
      tail = t
  merged_ranges.append((head, tail))
  return merged_ranges

def is_valid_ticket(merged_ranges, ticket):
  rate = 0
  is_valid = True
  for num in ticket:
    found = False
    for r in merged_ranges:
      if r[0]<=num and num<=r[1]:
        found = True
        break
    if not found:
      rate += num
      is_valid = False
  return (is_valid,rate)

def get_error_rate(merged_ranges, nearby_tickets):
  rate = 0
  for ticket in nearby_tickets:
    rate += is_valid_ticket(merged_ranges, ticket)[1]
  return rate

def discard_invalid_tickets(merged_ranges, nearby_tickets):
  valid_tickets = []
  for ticket in nearby_tickets:
    if is_valid_ticket(merged_ranges, ticket)[0]:
      valid_tickets.append(ticket)
  return valid_tickets

def determine_fields(rules_by_name, fields):
  output = [set() for i in range(len(fields))]
  for i in range(len(fields)):
    field = fields[i]
    for name, rules in rules_by_name.items():
      found = True
      for value in field:
        is_valid = False
        for r in rules:
          if r[0]<=value and value<=r[1]:
            is_valid = True
            break
        if not is_valid:
          found = False
          break
      if found:
        output[i].add(name)

    while True:
      should_break = True
      for o in output:
        if len(o) == 1:
          item = list(o)[0]
          for o2 in output:
            if len(o2) > 1 and item in o2:
              o2.remove(item)
              should_break = False
      if should_break:
        break

  return output 

if __name__=="__main__":
  f = open("day16_input1.txt")
  ranges = []
  rules_by_name = {}
  your_tickets = []
  nearby_tickets = []
  section = "rule"
  for line in f:
    if len(line.rstrip()) == 0:
      continue
    if line.startswith("your ticket"):
      section = "your ticket"
      continue
    elif line.startswith("nearby tickets"):
      section = "nearby tickets"
      continue

    if section == "rule":
      rule_name, rules = line.rstrip().split(":")
      rules_by_name[rule_name] = []
      rule = rules.split("or")
      for r in rule:
        begin, end = [int(n) for n in r.strip().split("-")]
        ranges.append((begin, end))
        rules_by_name[rule_name].append((begin, end))
    elif section == "your ticket":
      your_tickets = [int(n) for n in line.split(",")]
    elif section == "nearby tickets":
      ticket = [int(n) for n in line.split(",")]
      nearby_tickets.append(ticket)
  
  ranges = merge_ranges(ranges)
  error_rate = get_error_rate(ranges, nearby_tickets)
  print(error_rate)
  valid_tickets = discard_invalid_tickets(ranges, nearby_tickets)
  fields = [[ticket[i] for ticket in valid_tickets] for i in range(len(valid_tickets[0]))]
  output = determine_fields(rules_by_name, fields)
  result = 1
  for i in range(len(output)):
    if list(output[i])[0].startswith("departure"):
      result *= your_tickets[i]
  print(result)
  f.close()

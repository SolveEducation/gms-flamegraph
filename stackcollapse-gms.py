import sys

stack = []
frames = []

# generate frames, a frame is a call stack + total time
for line in sys.stdin:
    leading_spaces = len(line) - len(line.lstrip())
    level = leading_spaces // 6
    tok = line.split(',')
 
    if len(tok) < 2 or not tok[1].isnumeric():
        continue
  
    name = tok[0].lstrip()
    time = int(tok[1])
  
    if level < len(stack):
        stack[level] = name
    else:
        stack.append(name)

    frames.append( (stack[:level+1], time) )

# compute time spent in that frame
for i in range(len(frames)):
    stack, total_time = frames[i]
    child_time = 0
    for j in range(i+1,len(frames)):
        cstack, ctotal_time = frames[j]
        if cstack[:len(stack)] != stack:
            break
        elif len(cstack) == len(stack) + 1:
            child_time += ctotal_time

    used_time = total_time - child_time

    print(';'.join(stack), used_time)

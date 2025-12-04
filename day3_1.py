
def getmaxjoltage(line, digits):
    l = len(line)
    d = digits
    max_d = [0] * (d)
    max_d_n = [0] * (d)
    c_num = -1
    for i in range(0, d):
        max_d[i] = int(line[c_num+1])
        max_d_n[i] = c_num +1 
        start = max_d_n[i] + 1
        end = l-d+i
        #print(f"{i}: Start {start} End {end}")
        for c_n, c in enumerate(line[start:end],start):
            if int(c) > max_d[i] :
                max_d[i] = int(c)
                max_d_n[i] = c_n
        c_num = max_d_n[i]
        #print(f"Max_d {i} is {max_d[i]} at {max_d_n[i]} cnum {c_num}")
    max_d_str = [str(n) for n in max_d]
    max_num = int("".join(max_d_str))
    return (max_num)


with open('day3_1-input.txt', 'r') as f:
    lines = f.readlines()
    totaljoltage = 0
    for lineno, line in enumerate(lines,1):
        maxjolt = getmaxjoltage(line, 12)
        print(f"Max on #{lineno} is {maxjolt}")
        totaljoltage += maxjolt
    print(f"Totaljoltage is {totaljoltage}")

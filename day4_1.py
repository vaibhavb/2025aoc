def make_rolls_map(lines):
    rows = int(len(lines))
    cols  = int(len(lines[0].rstrip()))
    map =  [[''] * cols for _ in range(rows)]
    for row_n, line in enumerate(lines, 0):
        for col_n, c in enumerate(line.rstrip(), 0):
            map[row_n][col_n] = c
    return map


def check_role(ch):
    if (ch == '@' or ch == 'x'):
        return True
    else:
        return False

def mark_pickable(map):
    r_n = len(map)
    c_n = len(map[0])
    count_n = 0
    for r in range(r_n):
        for c in range(c_n):
            if map[r][c] == '@':
                #check neighbors
                count = 0
                if (c > 0):
                    if (check_role(map[r][c-1])): #left
                        count += 1
                    if (r < (r_n -1)):
                        if (check_role(map[r+1][c-1])): #cross-bottom-left
                            count += 1
                    if (r > 0):
                        if (check_role(map[r-1][c-1])): #cross-top-left
                            count += 1
                if (c < (c_n - 1)):
                    if (check_role(map[r][c+1])): #right
                        count += 1
                    if (r < (r_n -1)):
                        if (check_role(map[r+1][c+1])): #cross-bottom-right
                            count += 1
                    if (r > 0):
                        if (check_role(map[r-1][c+1])): #cross-top-right
                            count += 1
                if (r < (r_n - 1)):
                    if (check_role(map[r+1][c])): #bottom
                        count += 1
                if (r > 0):
                    if (check_role(map[r-1][c])): #top
                        count +=  1
                if (count < 4):
                    #print(f"Row {r} Col {c} Count {count}")
                    map[r][c] = 'x'
                    count_n += 1
    return map, count_n 

def print_map(map, count_n):
    r_n = len(map)
    for r in range(r_n):
        print("".join(map[r]))
    print(f"Total Count is {count_n}")

def remove_rolls(map):
    print(f"Removing rolls")
    r_n = len(map)
    c_n = len(map[0])
    for r in range(r_n):
        for c in range(c_n):
            if (map[r][c] == 'x'):
                map[r][c] = '.'
    return(map)

with open ('day4_1-input.txt', 'r') as f:
        lines = f.readlines()
        map = make_rolls_map(lines)
        totalcount = 0
        while True:
            map, count = mark_pickable(map)
            print_map(map, count)
            map = remove_rolls(map)
            if (count == 0):
                break
            else :
                totalcount += count
        print(f"Total Rolls Removed {totalcount}")
        

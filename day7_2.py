from functools import lru_cache

with open('day7_1-input.txt', 'r') as f:
    lines = f.readlines()
    colider = [[] for _ in range(len(lines))]
    for row, line in enumerate(lines, 0):
        line = line.strip()
        colider[row] = [ch for ch in line]

    # run the ray, and count splits
    split_count = 0
    for r_no, row in enumerate(colider[1:],1):
        for c_no, col in enumerate(row, 0):
            #print(f"[{r_no}, {c_no}] {col}, above [{r_no-1}, {c_no}] {colider[r_no-1][c_no]}")
            if (col == '.') and (colider[r_no-1][c_no] == '|' or colider[r_no-1][c_no] == 'S'):
                colider[r_no][c_no] = "|"
            if (col == '^') and (colider[r_no-1][c_no] == '|' or colider[r_no-1][c_no] == 'S'):
                if c_no > 0 :
                    colider[r_no][c_no-1] = "|"
                if c_no < len(colider[0]):
                    colider[r_no][c_no+1] = "|"
                split_count += 1

    print(f"Total splits {split_count}")
    for row in range(len(colider[0])):
        print("".join(colider[row]))

    #now do a backtracking algorithm on the colider.    
    def find_paths(colider):
        r, c = len(colider), len(colider[0])
        path = []
        results = []

        start_col = 0
        for c_no, col in enumerate(colider[0], 0):
            if (col == 'S'):
                start_col = c_no
        print(f"Starting at 0,{start_col}")

        def find_path(row, col):
            if (row, col) in path:
                return
            path.append((row, col))
            if (row == r-1) and colider[row][col] == "|":
                results.append(path.copy())
                path.pop()
                return
            if row + 1 < r:
                if colider[row+1][col] == "^":
                    if col > 0:
                        find_path(row+1, col-1)
                    if col < c-1:
                        find_path(row+1, col+1)
                elif colider[row+1][col] == "|":
                    find_path(row+1, col)

            path.pop()

        find_path(0, start_col)
        return results

    # now count all complete paths from row 0 to last row
    r, c = len(colider), len(colider[0])

    start_col = 0
    for c_no, ch in enumerate(colider[0], 0):
        if ch == 'S':
            start_col = c_no
            break
    print(f"Starting at 0,{start_col}")

    @lru_cache(maxsize=None)
    def count_paths(row, col):
        if not (0 <= row < r and 0 <= col < c):
            return 0

        # path is complete if we reached last row from above
        if row == r - 1:
            # we only count if this node is actually on the ray
            if colider[row][col] in ('|'):
                return 1
            return 0

        total = 0
        nr = row + 1
        below = colider[nr][col]

        if below == "^":
            # split to left/right pipes on next row
            if col > 0 and colider[nr][col-1] == "|":
                total += count_paths(nr, col-1)
            if col < c - 1 and colider[nr][col+1] == "|":
                total += count_paths(nr, col+1)
        elif below == "|":
            # continue straight down
            total += count_paths(nr, col)

        return total

    #results = find_paths(colider)
    #print(f"Total paths {len(results)}")
    total_paths = count_paths(0, start_col)
    print(f"Total paths {total_paths}")

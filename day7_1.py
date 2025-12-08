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
                if c_no > 1 :
                    colider[r_no][c_no-1] = "|"
                if c_no < len(colider[0]):
                    colider[r_no][c_no+1] = "|"
                split_count += 1

    print(f"Total splits {split_count}")


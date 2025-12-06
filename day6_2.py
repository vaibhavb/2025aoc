with open('day6_1-input.txt', 'r') as f:
    lines = f.readlines()
    input = []
    for line in lines:
        symbols = [r for r in line.rstrip('\n')]
        input.append(symbols)
    print(input)

    operations = [r for r in lines[-1].split(" ") if r.strip()]
    print(f"operations are {operations}")
    idx = 0
    sumtotal = 0
    nums = []
    for col, symbol in enumerate(input[-1], 0):
        operation = operations[idx]
        x = [input[i][col] for i in range(0, len(input))]
        if ("".join(x).strip() == "") or (col == len(input[0])-1):
            if col == len(input[0])-1:
                num = "".join(x)[0:-1]
                nums.append(int(num))
            else:
                idx += 1
            if operation == '+':
                total = 0
                for i in nums:
                    if (i != " "):
                        total += int(i)
                print(f"Total of {nums} with + is {total}")
                sumtotal += total
                nums = []
            elif operation == '*':
                total = 1
                for i in nums:
                    if (i != " "):
                        total *= int(i)
                print(f"Total of {nums} with * is {total}")
                sumtotal += total
                nums = []
        else:
            num = "".join(x)[0:-1]
            nums.append(int(num))

    print(f"SUMtotal is {sumtotal}")

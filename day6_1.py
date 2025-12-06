with open('day6_1-input.txt', 'r') as f:
    lines = f.readlines()
    input = []
    for line in lines:     
        symbols = [r.strip() for r in line.split(" ") if r.strip()]
        input.append(symbols)
    
    sumtotal = 0
    for col, symbol in enumerate(input[-1], 0):
        if symbol == '+':
            total = 0
            for i in range(0, len(input)-1):
                total += int(input[i][col])
            sumtotal += total
        if symbol == '*':
            total = 1
            for i in range(0, len(input)-1):
                total *= int(input[i][col])
            sumtotal += total
    
    print(f"SUMtotal is {sumtotal}")

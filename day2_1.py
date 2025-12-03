def is_invalid(num):
    if (len(str(num)) % 2 == 0):
        half = len(str(num)) // 2
        num1 = int(str(num)[0:half])
        num2 = int(str(num)[half:])
        if (num1 == num2):
            return True
    for i in range(1,len(str(num)) // 2 + 1 ):
        f = (str(num))[0:i]
        seq = True
        print(f)
        for c in [str(num)[j:i+j] for j in range(i, len(str(num)), i)]:
            print(f"i:{i}, f:{f}, j:{2}, c:{c}")
            if (c != f):
                seq = False
                break
        if (seq == True):
            return True
    return False

def check_invalid(num1, num2):
    invalid_list = []
    num = num1
    while (num <= num2):
        if  (is_invalid(num)):
            invalid_list.append(num)
        num += 1
    return invalid_list

with open('day2_1-input.txt', 'r') as f:
    lines = f.readlines()
    invalids = []
    sum = 0
    for pair in lines[0].split(','):
            num1 = int(pair.split("-")[0])
            num2 = int(pair.split("-")[1])
            nums = check_invalid(num1, num2)
            if (len(nums) > 0):
                for num in nums:
                    invalids.append(num)
                    sum += num
    print(f"For {invalids} Sum is {sum}")

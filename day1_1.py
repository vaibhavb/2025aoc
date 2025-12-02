class Lock:
    def __init__(self, key):
        self.zerocheck = 0
        self.zeropassage = 0
        self.turncount = 0
        self.key = key

    def go_left(self, value):
        start = 0 if (self.key == 0) else 1
        self.key = self.key - value
        if (self.key == 0):
            self.zerocheck  += 1
            self.zeropassage += 1
        elif (self.key < 0):
            passage  = (-self.key) // 100 + start
            self.key = self.key % 100
            if self.key == 0:
                self.zerocheck += 1
                self.zeropassage += passage
                self.turncount += passage -1
            else:
                self.turncount +=  passage
                self.zeropassage += passage

    def go_right(self, value):
        self.key = self.key + value
        if (self.key == 0):
            self.zerocheck += 1
            self.zeropassage += 1
        elif (self.key > 99):
            passage = self.key // 100
            self.key = self.key % 100
            if self.key == 0:
                self.zerocheck += 1
                self.zeropassage += passage
                self.turncount += passage - 1
            else:
                self.zeropassage += passage
                self.turncount += passage

    def __str__(self):
        return (f"{self.key}")

def get_actions():
    with open("day1_1_input.txt", "r") as f:
        lines = f.readlines()
        actions = []
        for line in lines:
            action = {}
            direction =  line[0]
            value = line[1:]
            #print(f"Direction: {direction}, Value: {value}", end='')
            action['direction']=direction
            action['value']=int(value)
            actions.append(action)
        return actions


actions = get_actions()
lock = Lock(50)
print(lock)
for action in actions:
    value = action['value']
    if (action['direction'] == 'L'):
        lock.go_left(value)
    if (action['direction'] == 'R'):
        lock.go_right(value)
    print(f"After {action}, lock at {lock}")

print(f"reset turns: {lock.turncount}, zero pointers: {lock.zerocheck}, passage: {lock.zeropassage}")


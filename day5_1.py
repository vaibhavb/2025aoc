class IngredientRange:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def inrange(self,item):
        if (item>= self.first and item<=self.last):
            return True
        else:
            return False

    def __str__(self):
        return (f"Range[{self.first}:{self.last}]")


with open('day5_1-input.txt') as f:
    lines = f.readlines()
    ranges = []
    items = []
    range_mode = True
    for line in lines:
        if line.rstrip() == '':
            range_mode = False
        else:
            if (range_mode):
                ranges.append(line.rstrip())
            else:
                items.append(line.rstrip())
    print(f"Total ranges {len(ranges)}, and total items {len(items)}")
    range_list = []
    for r in ranges:
        first = int(r.split('-')[0])
        last = int(r.split('-')[1])
        range_list.append(IngredientRange(first, last))
    fresh_list = []
    for i in items:
        for r in range_list:
            if (r.inrange(int(i))):
                fresh_list.append(i)
                break
    print(f"Total fresh item no {len(fresh_list)}")

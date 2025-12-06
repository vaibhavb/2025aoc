class IngredientRange:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def inrange(self,item):
        if (item>= self.first and item<=self.last):
            return True
        else:
            return False

    def get_item_count(self):
        return (self.last - self.first + 1)

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
    #create a non-overlapping ranges
    no_range_list = []
    range_list_sorted = sorted(range_list, key= lambda r : r.first)
    for r in range_list_sorted:
        no_update = True
        for no_r in no_range_list:
            if (no_r.inrange(r.first) and no_r.inrange(r.last)): #range exists
                no_update = False
                break
            elif (no_r.inrange(r.first) and not no_r.inrange(r.last)):
                no_update = False
                no_r.last = r.last
                break
            elif (not no_r.inrange(r.first) and no_r.inrange(r.last)):
                no_update = False
                no_r.first = r.first
                break
            else:
                pass
        if (no_update):
            no_range_list.append(r)
    count = 0
    for r in no_range_list:
       count += r.get_item_count()
    print(f"Total unique items {count}")

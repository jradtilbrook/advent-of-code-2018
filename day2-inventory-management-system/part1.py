import fileinput

if __name__ == '__main__':
    twos = 0
    threes = 0
    for line in fileinput.input(): # each line
        line = line.strip()
        agg = {}
        for c in line: # each character in the line
            if c in agg: # already seen it, increment
                agg[c] = agg[c] + 1
            else: # not seen, add it in
                agg[c] = 1
        # remember if weve seen a 2 because we dont care about duplicates
        seen = None
        for value in sorted(agg.values()):
            if value == 2 and not seen:
                twos = twos + 1
                seen = True
            # if we hit a 3, break since we know we dont care about larger
            if value == 3:
                threes = threes + 1
                break
    print(twos * threes)

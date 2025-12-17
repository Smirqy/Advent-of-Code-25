

def main():
    file = open("Day5Input.txt")
    lines = file.readlines()
    
    is_ranges = True
    ranges = []
    count = 0
    ranges_count = 0
    for line in lines:
        line = line.strip()
        if line == "":
            is_ranges = False
            ranges.sort()
            ranges = combine_ranges(ranges)
            continue
        
        if is_ranges:
            low, high = line.split("-")
            ranges.append((int(low), int(high)))
        else:
            #Part 1
            for low, high in ranges:
                query = int(line)
                
                if query >= low and query <= high:
                    count += 1

    #Part 2
    for low, high in ranges:
        ranges_count += (high - low) + 1
    
    print(ranges)
    print(count)
    print(ranges_count)
    


def combine_ranges(ranges):
    i = 0
    while i < len(ranges):
        curr_low, curr_high = ranges[i]

        if i + 1 < len(ranges) and curr_high >= ranges[i+1][0]:
            ranges[i] = (curr_low, max(curr_high, ranges[i+1][1]))
            ranges.pop(i+1)
        else:
            i += 1
    return ranges

main()
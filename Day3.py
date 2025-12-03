
def find_largest(n, length):
    memo = {}
    memo[len(str(n))] = ""

    def f(i, taken):
        key = (i, taken)
        if key in memo:
            return memo[i, taken]
        if taken >= length:
            return ""
        elif i >= len(str(n)):
            return ""
        
        str_taken = str(n)[i] + f(i+1, taken + 1)
        str_not_taken = f(i + 1, taken)

        num_taken = 0 if str_taken == '' else int(str_taken)
        num_not_taken =  0 if str_not_taken == '' else int(str_not_taken)

        memo[key] = str(max(num_taken, num_not_taken))
        return memo[key]
    
    return int(f(0, 0))




def main():
    # file = open("Day3InputTest.txt")
    file = open("Day3Input.txt")

    lines = file.readlines()

    total = 0
    for line in lines:
        largest = find_largest(line.rstrip('\n'), 12)
        print(largest)
        total += largest

    print(total)



def test():
    print(find_largest(811111111111119, 12))

main()
# test()
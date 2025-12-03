import re

def is_valid(n):
    num_str = str(n)
    if num_str[0] == '0':
        return False
    elif has_pattern(num_str):
        return False
    # elif num_str[:(len(num_str)//2)] == num_str[(len(num_str)//2):]:
    #     return False
    
    return True

def main():
    # file = open("Day2InputTest.txt")
    file = open("Day2Input.txt")

    line = file.readline()

    total = 0
    for range_str in line.split(","):
        lower, upper = range_str.split("-")
        for i in range(int(lower), int(upper)+1):
            if not is_valid(i):
                # print(i)
                total += i

    print(total)

def has_pattern(n_str):
    for length in range(1, len(n_str)//2 + 1):
        pattern = n_str[:length]
        found = True
        for curr in range(length, len(n_str), length):
            check = n_str[curr:(curr + length)]

            if pattern != check:
                found = False
                break

        if found:
            return True
        
    
    return False


def test():
    print(is_valid(101010))
    print(is_valid(111))

main()

# test()
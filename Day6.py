import math
OPERATORS = {'*', '+'}

def main():
    file = open("Day6Input.txt")
    lines = file.readlines()

    total = 0

    columns, operators = get_numbers(lines)

    # print(columns)
    
    for i in range(len(columns)):
        sub_total = 0
        for j in range(len(columns[i])):
            num = int(''.join(columns[i][j]))
            if operators[i] == '+':
                sub_total += num
            else:
                if sub_total == 0:
                    sub_total = num
                else:
                    sub_total *= num
        
        total += sub_total



    # for line in lines:
    #     line = line.strip()
    #     if line[0].isdigit():
    #         row_nums = line.split(" ")
    #         row_nums = [sublist for sublist in row_nums if sublist]
    #         for i in range(len(row_nums)):
    #             if i >= len(nums):
    #                 nums.append([[]])
    #             for j in range(len(row_nums[i])):
    #                 if j >= len(nums[i]):
    #                     nums[i].append([])
    #                 nums[i][j].append(row_nums[i][j])
    #     else:
    #         operators = line.split(" ")
    #         operators = [sublist for sublist in operators if sublist]
            
    #         for i in range(len(operators)):
    #             sub_sum = 0
    #             print()
    #             print("Operator", operators[i])
    #             for num_list in nums[i]:
    #                 num = int("".join(num_list))
    #                 print("Num", num)
    #                 if operators[i] == "+":
    #                     sub_sum += num
    #                 elif operators[i] == "*":
    #                     if sub_sum == 0:
    #                         sub_sum = num
    #                     else:
    #                         sub_sum *= num
    #                 else:
    #                     print("Error: Unhandled operator")
    #                     return
    #             print("Sub_sum", sub_sum)
    #             total += sub_sum
            

    # print(operators)
    print(total)

def get_numbers(lines):
    columns = []
    operators = []
    counts = []
    count = 0

    for i in range(0, len(lines[-1])):
        if lines[-1][i] in OPERATORS:
            if i != 0:
                counts.append(count)
                count = 0
            operators.append(lines[-1][i])
            
        count += 1
    counts.append(count)

    for line in lines:
            i = 0
            index = 0
            while index < len(counts):
                num_length = counts[index] - 1
                if not line[0] in OPERATORS:
                    if index >= len(columns):
                        columns.append([])
                    for j in range(0, num_length):
                        if len(columns[index]) < num_length:
                            for _ in range(num_length):
                                columns[index].append([])
                        # print(i, j, len(line))
                        if line[i+j] != ' ':
                            columns[index][j].append(line[i+j])
                i += counts[index]
                index += 1
                
    return columns, operators

            


main()
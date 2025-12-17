def main():
    file = open("Day4InputTest.txt")

    lines = file.readlines()

    layout = []

    for line in lines:
        to_add = []
        for char in line.strip():
            to_add.append(char)

        layout.append(to_add)

    output = layout.copy()
    remove_total = 0
    while True:
        x_count = 0
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                if output[i][j] == "@":
                    rolls = count_rolls(output, i, j)
                    if rolls < 4:
                        output[i][j] = "X"
                        x_count += 1
                        continue
                elif output[i][j] == "X":
                    output[i][j] = "."
                    continue
        
        if x_count == 0:
            break
        else:
            remove_total += x_count

        for line in output:
            print(line)
        print()
        print("XCount:", x_count)

    print("Remove count", remove_total)

def count_rolls(layout, i, j):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]
    count = 0
    for i_add, j_add in directions:
        i_curr = i + i_add
        j_curr = j + j_add
        if i_curr >= 0 and i_curr < len(layout) and j_curr >= 0 and j_curr < len(layout[i_curr]):
            if layout[i_curr][j_curr] == "@":
                count += 1
    
    return count

main()
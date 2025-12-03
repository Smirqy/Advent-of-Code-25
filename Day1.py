def main():
    file = open("Day1Input.txt")

    lines = file.readlines()

    pointer = 50
    count = 0
    for line in lines:
        amount = int(line[1:])

        if line[0] == 'L':
            amount *= -1
        
        passes = count_passes2(pointer, amount)
        count += passes
        pointer = (pointer + amount) % 100
        if pointer == 0:
            count += 1

    print("Answer:", count)

def count_passes(pointer, amount):
    count = 0
    while True:
        if amount > 100:
            count += 1
            amount -= 100
        elif amount < -100:
            count += 1
            amount += 100
        else:
            if pointer + amount > 100:
                count += 1
                break
            elif pointer + amount < 0:
                if pointer != 0:
                    count += 1
                break
            else:
                break

    return count

def count_passes2(pointer, amount):
    if abs(amount) > 100:
        count = int(amount/100)
        amount = amount % 100
    else:
        count = 0

    if pointer + amount > 100:
        count += 1
    elif pointer + amount < 0:
        if pointer != 0:
            count += 1

    return count


def test():
    print(50 - 68)
    print(-18 % 100)
    print((52 + 48) % 100)


main()
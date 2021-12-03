def digit_counts(numbers):
    counts = [0] * len(numbers[0].strip())
    total = 0
    for line in numbers:
        for i, digit in enumerate(line):
            if digit == "1":
                counts[i] += 1
        total += 1
    return counts, total

with open("day_3/input.txt") as f:

    counts, total = digit_counts(list(f.readlines()))

    print(counts, total)

    gamma = 0
    epsilon = 0

    for count in counts:
        gamma <<= 1
        epsilon <<= 1
        if count > total // 2:
            gamma += 1
        else:
            epsilon += 1

    print(f"{gamma} * {epsilon} = {gamma * epsilon}")

with open("day_3/input.txt") as f:
    oxygen_numbers = list(f.readlines())

    for i in range(len(oxygen_numbers[0])):
        if len(oxygen_numbers) <= 1:
            break

        count, total = 0, len(oxygen_numbers)
        for number in oxygen_numbers:
            if number[i] == "1":
                count += 1
        print(oxygen_numbers, count, total)

        bit_critera = "1" if count > total // 2 else "0"
        if count * 2 == total:
            bit_critera = "1"
        oxygen_numbers = [n for n in oxygen_numbers if n[i] == bit_critera]

    oxygen = int(oxygen_numbers[0],2)
    print(f"oxygen: {oxygen}")

with open("day_3/input.txt") as f:
    co2_numbers = list(f.readlines())

    for i in range(len(co2_numbers[0])):
        if len(co2_numbers) <= 1:
            break

        count, total = 0, len(co2_numbers)
        for number in co2_numbers:
            if number[i] == "0":
                count += 1
        print(co2_numbers, count, total)

        bit_critera = "0" if count <= total // 2 else "1"
        if count * 2 == total:
            bit_critera = "0"
        co2_numbers = [n for n in co2_numbers if n[i] == bit_critera]

    co2 = int(co2_numbers[0],2)
    print(f"co2: {co2}")

print(f"{oxygen} * {co2} = {oxygen * co2}")

# so much duplicate code...
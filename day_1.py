with open("Day1Input.txt") as f:
    previous_depth = float("inf")
    sweep_increases = 0
    for line in f.readlines():
        depth = int(line)
        if depth > previous_depth:
            sweep_increases += 1
        previous_depth = depth
    print(f"Part 1 solution: {sweep_increases}")

    previous_sum = 0
    sum_increases = 0
    window = []
    for line in f.readlines():
        depth = int(line)
        window.append(depth)
        if len(window) > 3:
            sum = previous_sum - window.pop(0) + depth
            if sum > previous_sum:
                sum_increases += 1
            previous_sum = sum
        previous_sum += depth
    print(f"Part 2 solution: {sum_increases}")
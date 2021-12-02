with open("day_2/input.txt") as f:
    position, depth = 0, 0

    for line in f.readlines():
        [direction, magnitude] = line.split()
        
        if direction == "forward":
            position += int(magnitude)
        elif direction == "up":
            depth -= int(magnitude) # Will we get inputs that try to make us fly?
        elif direction == "down":
            depth += int(magnitude)
        else:
            print("This probably shouldn't happen: " + line)                        

    print(f"Part 1: {position} * {depth} = {position * depth}")

with open("day_2/input.txt") as f:
    position, depth, aim = 0, 0, 0

    for line in f.readlines():
        [direction, magnitude] = line.split()
                        
        if direction == "forward":
            position += int(magnitude)
            depth += aim * int(magnitude)
        elif direction == "up":
            aim -= int(magnitude)
        elif direction == "down":
            aim += int(magnitude)
        else:
            print("This probably shouldn't happen: " + line)                        

    print(f"Part 2: {position} * {depth} = {position * depth}")
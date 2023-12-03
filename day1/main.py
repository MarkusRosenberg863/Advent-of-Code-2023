def count_calibrations(lines: list[str]):
    result = 0
    
    for line in lines:
        first_number = next(c for c in line if c.isdigit())
        second_number = next(c for c in reversed(line) if c.isdigit())
        
        result += int(first_number) * 10 + int(second_number)
       
    return result

def part1():
    lines = open("./input.txt", "r").readlines()
    result = count_calibrations(lines)
       
    print(result)

def part2():
    lines = open("./input.txt", "r").readlines()
    
    for (i, line) in enumerate(lines):
        line = (
            line.replace("one", "o1e")
                .replace("two", "t2o")
                .replace("three", "t3e")
                .replace("four", "f4r")
                .replace("five", "f5e")
                .replace("six", "s6x")
                .replace("seven", "s7n")
                .replace("eight", "e8t")
                .replace("nine", "n9e"))
        lines[i] = line
       
    result = count_calibrations(lines)
    print(result)

part1()
part2()
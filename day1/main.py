def part1():
    lines = open("./input.txt", "r").readlines()
    result = 0
    
    for line in lines:
        first_number = next(c for c in line if c.isdigit())
        second_number = next(c for c in reversed(line) if c.isdigit())
        
        result += int(first_number) * 10 + int(second_number)
       
    print(result)

def part2():
    lines = open("./input.txt", "r").readlines()
    result = 0
    
    for line in lines:
        line = (
            line.replace("one", "1")
                .replace("two", "2")
                .replace("three", "3")
                .replace("four", "4")
                .replace("five", "5")
                .replace("six", "6")
                .replace("seven", "7")
                .replace("eight", "8")
                .replace("nine", "9"))
        
        first_number = next(c for c in line if c.isdigit())
        second_number = next(c for c in reversed(line) if c.isdigit())
        
        result += int(first_number) * 10 + int(second_number)
       
    print(result)

       
part1()
part2()
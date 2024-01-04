from functools import reduce
import operator

def part1():
    lines = open("input.txt", "r").readlines()
    
    time_distances = list(zip(map(int, lines[0].split()[1:]), map(int, lines[1].split()[1:])))
    
    results: list[int] = []
    for (time, distance) in time_distances:
        results.append(len(list(filter(lambda t: t * (time-t) > distance, range(time)))))
    
    print(reduce(operator.mul, results))
    
def part2():
    lines = open("input.txt", "r").readlines()
    
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))
    
    print(len(list(filter(lambda t: t * (time-t) > distance, range(time)))))

part1()
part2()
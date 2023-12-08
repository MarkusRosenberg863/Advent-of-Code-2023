from dataclasses import dataclass
import re

@dataclass
class Element:
    content: str
    x0: int
    x1: int
    y: int

def get_elements(lines: list[str], regex: str):
    result: list[Element] = []
    pattern = re.compile(regex)

    for (i, line) in enumerate(lines):
        pos = 0
        match = pattern.search(line, pos)
        while match:
            result.append(Element(match.group(), match.start(), match.end()-1, i))
            pos = match.end()
            match = pattern.search(line, pos)
    
    return result

def distance_point_linesegment(point: Element, line: Element):
    l2 = (line.x0 - line.x1) ** 2
    if l2 == 0: 
        return (point.x0 - line.x0) ** 2 + (point.y - line.y) ** 2

    t = (point.x0 - line.x0) * (line.x1 - line.x0) / l2
    t = max(0, min(1, t))
    
    return (point.x0 - (line.x0 + t * (line.x1 - line.x0))) ** 2 + (point.y - line.y) ** 2

def part1():
    lines = open("./input.txt", "r").readlines()
    result = 0
    numbers = get_elements(lines, r'\d+')
    symbols = get_elements(lines, r'[^\d.\n]')
    
    for number in numbers:
        distances = map(lambda x: distance_point_linesegment(x, number), symbols)
        if list(filter(lambda x: x <= 2, distances)):
            result += int(number.content)
    
    print(result)
   
def part2():
    lines = open("./input.txt", "r").readlines()
    result = 0
    numbers = get_elements(lines, r'\d+')
    symbols = get_elements(lines, r'[^\d.\n]')
    
    for gear in filter(lambda x: x.content == "*", symbols):
        adjacent_numbers = list(filter(lambda x: distance_point_linesegment(gear, x) <= 2, numbers))
        if len(adjacent_numbers) == 2:
            result += int(adjacent_numbers[0].content) * int(adjacent_numbers[1].content)
    
    print(result)
    
part1()
part2()
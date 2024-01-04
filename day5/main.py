import re
from dataclasses import dataclass
from functools import reduce

@dataclass
class Map:
    destination_start: int
    source_start: int
    map_range: int

def parse_maps(lines: list[str]):
    MAP_AMOUNT = 7
    digit_re = re.compile(r'\d+')
    
    maps: list[list[Map]] = []
    
    index = 1
    while(len(maps) < MAP_AMOUNT):
        current_map: list[str] = []
        index += 1
        while(index < len(lines) and lines[index] != "\n"):
            current_map.append(lines[index])
            index += 1
        
        map_numbers = map(lambda x: list(map(int, digit_re.findall(x))), current_map[1:])
        map_numbers = filter(lambda x: x != [], map_numbers)
        map_list = list(map(lambda x: Map(x[0], x[1], x[2]), map_numbers))
        maps.append(map_list)
    
    return maps

def part1():
    lines = open("./input.txt", "r").readlines()
    digit_re = re.compile(r'\d+')
    seeds = list(map(int, digit_re.findall(lines[0])))
    
    maps: list[list[Map]] = parse_maps(lines)
    
    converted_seeds: list[int] = seeds
    for map_group in maps:
        for (count, seed) in enumerate(seeds):
            for conversion_map in map_group:
                if seed in range(conversion_map.source_start, conversion_map.source_start + conversion_map.map_range):
                    converted_seeds[count] = conversion_map.destination_start + seed - conversion_map.source_start

    print(min(converted_seeds))

"""
Part 2 mostly copied from u/daggerdragon
Link to his code:
https://topaz.github.io/paste/#XQAAAQDyAgAAAAAAAAAzHIoib6poHLpewxtGE3pTrRdzrponK6uH8J9SK+0ES1LNdidG34FPT5Z5WfpAJ/epkMmnWNkE3uWVG0Y8HT99F+XNebEMfXdELf9EbJ4kU+4y8Z8mDTo7PYq6+UpBxHW3EhVkOrGX3a+DvB8oTz2hTXJdALhnxjOj4y3tG0GpOl9HlHOht5s9poDZYbVSMAOVoydIcuw6HPI5RHgaj0Dmnf4zU0plUYr3EoKI5ThFrVqKROa/OfWIF2UvFpNQjhWxoE9A1pEE/WsGzUpXdzMxbeUNCAyUDivAxRpAVwehvDQRA+tTYu0KlD1s7ZzjZbesgD+q055DMBD2vWEFXxTS8RaJeZmJXhqifO4l0xwb3NU/jMCEI2odBCcCZwzS6p9uh3Am1pILaAn1HGYLq6s22CWhDBx5BszlI+cy14Zxa5o28HYmiDcE9Q1fODzW5vhJoUt0t4sdraVoaMXTJk7bmgAAlz5+e/4JIbI=
"""

def lookup(inputs: list[tuple[int, int]], mapping: str):
    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else: yield (start, length); break

def part2():
    seeds, *mappings = open('input.txt').read().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))
    
    print(*[min(reduce(lookup, mappings, list(zip(seeds[0::2], seeds[1::2]))))[0]]) # type: ignore

part1()
part2()
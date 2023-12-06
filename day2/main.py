import re

def get_color_maxamount(string: str, color: str):
    pattern = re.compile(fr'\d+ {color}')
    matches = pattern.findall(string)
    
    color_counts = map(lambda x: int(x.replace(color, "").strip()), matches)
    return max(color_counts)

def part1():
    lines = open("./input.txt", "r").readlines()
    result = 0
    
    games = list(map(lambda x: x.split(":")[1], lines))
    for (i, game) in enumerate(games):
        if get_color_maxamount(game, "red") > 12:
            continue
        if get_color_maxamount(game, "green") > 13:
            continue
        if get_color_maxamount(game, "blue") > 14:
            continue
        
        result += i+1
    
    print(result)

def part2():
    lines = open("./input.txt", "r").readlines()
    result = 0
    
    games = list(map(lambda x: x.split(":")[1], lines))
    for game in games:
        result += get_color_maxamount(game, "red") * get_color_maxamount(game, "green") * get_color_maxamount(game, "blue")
    
    print(result)
   
part1()
part2()
# Part 1
def build_network(network: str):
    network_dict: dict[str, tuple[str, str]] = {}
    for n in network.split("\n"):
        position, nodes = n.split("=")
        left, right = nodes.replace("(", "").replace(")", "").split(",")
        network_dict[position.strip()] = (left.strip(), right.strip())
    
    return network_dict

steps, raw_network = open("./input.txt", "r").read().split("\n\n")

network = build_network(raw_network)

moves = 0
current_position = "AAA"

while current_position != "ZZZ":
    direction = 0 if steps[moves % len(steps)] == "L" else 1
    current_position = network[current_position][direction]
    moves += 1

print(moves)

"""
Part 2
by u/4HbQ
Link:
https://topaz.github.io/paste/#XQAAAQCCAQAAAAAAAAA0m0pnuFI8c+fPp4HB1KcQKm7zPB1cp0R347tusXTI33WNPUd3vJD/tYCJtXhbqwWoJGs5sCu+eDxbA6Ar/0ljLq9aIWuzbKakiSrqp1nIj/g4n1hJGb/jJHyUcim835XVEPTqkHXeohMjokZU34QKXAmGyHEbChX+S6moQK18jDlIcPfxDF9YgtHtGaHUvgfoJNm+yP1rC1rd54gCsribbl1UTKz8FJUu8T98Ul58GmUMLrFtpjUzMul3j6XnG8UwK2ba2zrlP8abKj12R0/+6Hszct5Cs9mp02gqR9rgC9hSegHUBcrwY0A/aKQBYhc1cd0R+zHudaXlbxRsZTBo9bi/y/k2l+weMFi/IizxfpS7+fr/0dkMRA==
"""
import math, re

dirs, _, *graph = open("./input.txt").read().split('\n')
graph = {n: d for n, *d in [re.findall(r'\w+', s) for s in graph]}
start = [n for n in graph if n.endswith('A')]

def solve(pos: str, i: int = 0):
    while not pos.endswith('Z'):
        dir = dirs[i % len(dirs)]
        pos = graph[pos][dir=='R']
        i += 1
    return i

print(math.lcm(*map(solve, start)))
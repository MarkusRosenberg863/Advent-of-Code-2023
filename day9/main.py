from functools import reduce
import operator

def generate_differences(sequence: list[int]) -> list[list[int]]:
    if sequence.count(0) == len(sequence):
        return [sequence]
    
    differences = list(map(lambda x: x[1] - x[0], zip(sequence[0:], sequence[1:])))
    return [sequence, *generate_differences(differences)]

def get_next(differences: list[list[int]]) -> int:
    return reduce(operator.add, list(map(lambda x: x[-1], differences)))    

def get_past(differences: list[list[int]]) -> int:
    return reduce(operator.add, list(map(lambda x: x[0], differences)))

lines = open("./input.txt", "r").readlines()
sequences = list(map(lambda x: list(map(int, x.split())), lines))
next_numbers = list(map(lambda x: get_next(generate_differences(x)), sequences))

print(reduce(operator.add, next_numbers))

past_numbers = [
    get_past(
        [list(map(lambda x: -x, d)) if i % 2 == 1 else d for i, d in enumerate(generate_differences(s))]
    ) for s in sequences]

print(reduce(operator.add, past_numbers))
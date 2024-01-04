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

past_numbers: list[int] = []
for s in sequences:
    differences = generate_differences(s)
    for i in range(len(differences)):
        if i % 2 == 1:
            differences[i] = list(map(lambda x: -x, differences[i]))
    
    past_numbers.append(get_past(differences))
    
print(reduce(operator.add, past_numbers))
from dataclasses import dataclass
import re

@dataclass
class Scratchcard:
    amount: int
    value: int

def part1():
    lines = open("./input.txt", "r").readlines()
    result = 0
    
    lines = list(map(lambda x: x.split(":")[1], lines))
    pattern = re.compile(r'\d+')
    
    for line in lines:
        (winning_numbers, numbers) = list(map(lambda x: pattern.findall(x), line.split("|")))
        winning_numbers = list(map(lambda x: int(x), winning_numbers)) 
        numbers = list(map(lambda x: int(x), numbers))
        
        value = 0
        for number in numbers:
            if number in winning_numbers and value == 0:
                value = 1
            elif number in winning_numbers and value != 0:
                value *= 2
        
        result += value
    
    print(result)

def part2():
    lines = open("./input.txt", "r").readlines()
    
    lines = list(map(lambda x: x.split(":")[1], lines))
    pattern = re.compile(r'\d+')
    scratchcards : list[Scratchcard]= []
    
    for line in lines:
        (winning_numbers, numbers) = list(map(lambda x: pattern.findall(x), line.split("|")))
        winning_numbers = list(map(lambda x: int(x), winning_numbers)) 
        numbers = list(map(lambda x: int(x), numbers))
        
        value = 0
        for number in numbers:
            if number in winning_numbers:
                value += 1
        
        scratchcards.append(Scratchcard(1, value)) 

    for (i, card) in enumerate(scratchcards):
        if card.value == 0:
            continue
        
        max_range = min(i + card.value + 1, len(scratchcards))
        for j in range(i+1, max_range):
            scratchcards[j].amount += card.amount
    
    result = sum(map(lambda x: x.amount, scratchcards))
    print(result)
    
part1()
part2()
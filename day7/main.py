from dataclasses import dataclass
from functools import reduce
import operator

@dataclass
class Round:
    card_values: list[int]
    bid: int
    
def map_card(card: str):
    match card:
        case "J": return 1 # Part 2 mapping
        case "2": return 2
        case "3": return 3
        case "4": return 4
        case "5": return 5
        case "6": return 6
        case "7": return 7
        case "8": return 8
        case "9": return 9
        case "T": return 10
        #case "J": return 11 # Part 1 mapping
        case "Q": return 12
        case "K": return 13
        case "A": return 14
        case _: return 0

def count_same_cards(cards: list[int]):
    counts = [cards.count(card) for card in set(cards) if card != 1]
    # case if all cards are "J" in part 2
    if len(counts) == 0:
        return [5]
    
    index_highest_count = counts.index(max(counts))
    counts[index_highest_count] += cards.count(1)
    return counts

def map_type(matches: list[int]):
    if 5 in matches:
        return 7
    if 4 in matches:
        return 6
    if 3 in matches and 2 in matches:
        return 5
    if 3 in matches:
        return 4
    if 2 in matches and 2 in set([matches.count(n) for n in matches]):
        return 3
    if 2 in matches:
        return 2
    else:
        return 1

def sort_key(input: tuple[Round, int]):
    return (input[1], *input[0].card_values)

def sort(rounds: list[Round]):
    values = list(map(lambda x: (x, map_type(count_same_cards(x.card_values))), rounds))
    values.sort(key=sort_key)
    return list(map(lambda x: x[0], values))

lines = open("./input.txt", "r").readlines()

raw_rounds = list(map(lambda x: x.split(), lines))
rounds = list(map(lambda x: Round(list(map(map_card, list(x[0]))), int(x[1])), raw_rounds))
rounds = sort(rounds)

winnings = [bid * (i+1) for i, bid in enumerate(list(map(lambda x: x.bid, rounds)))]

print(reduce(operator.add, winnings))
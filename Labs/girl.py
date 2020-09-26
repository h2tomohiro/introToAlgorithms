import random

def run_one_family() -> [int]:
    boys = 0
    girls = 0
    while girls == 0:
        if random.choice([0, 1]) == 0:
            girls += 1
        else:
            boys += 1
    return [girls, boys]

run_one_family()
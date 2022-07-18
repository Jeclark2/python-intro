import random 

def cornhole_score_counter():
    total = 0
    while total <= 21:
        total += random.randint(1, 6)
        print(total)
    print(f"final total: {total}")

cornhole_score_counter()
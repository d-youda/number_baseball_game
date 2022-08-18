import random
def generate_numbers():
    num = []
    while len(num)<3:
        n = random.randint(0,9)
        if n not in num:
            num.append(n)
    return num

#print(generate_numbers())
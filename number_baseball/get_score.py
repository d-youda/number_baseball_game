def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    i = 0
    while i<len(guesses) :
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1
        i += 1
    return strike_count, ball_count

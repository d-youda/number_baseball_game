def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    i = 1
    while i <= 3:
        num = int(input("{}번째 수를 입력하세요:".format(i)))
        
        if num>9 or num<0 :
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        
        for j in range(0,len(new_guess)):
            if new_guess[j] == num:
                print("중복되는 숫자입니다. 다시 입력하세요.")
                continue
        
        else:
            new_guess.append(num)
            i += 1
        if len(new_guess) == 3:
            break
    return new_guess
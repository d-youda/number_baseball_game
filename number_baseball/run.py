import generate_numbers #무작위 번호 3개 받기
import get_score #유저가 번호 3개 입력
import take_guess #스트라이크 볼 판정

#정답 번호 만들기
ANSWER = generate_numbers.generate_numbers()
tries = 0



#번호 비교하기

while 1:
    #유저가 번호 입력
    user_ans = take_guess.take_guess()

    #strike, ball 입력 후 출력
    strike,ball = get_score.get_score(user_ans,ANSWER)
    print("{}B {}S".format(ball,strike))

    tries += 1

    if strike==3 :
        break
print("축하합니다. {}번만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))

import random

score = 0
total_questions = 5

print("구구단 퀴즈 게임을 시작합니다!")
print(f"총 {total_questions}문제가 출제됩니다.\n")

for i in range(total_questions):
    a = random.randint(2, 9)
    b = random.randint(1, 9)
    correct_answer = a * b

    print(f"문제 {i+1}: {a} x {b} = ?")
    user_input = input("정답을 입력하세요: ")

    # 입력이 숫자인지 체크
    if user_input.isdigit():
        if int(user_input) == correct_answer:
            print("정답입니다!\n")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 {correct_answer}입니다.\n")
    else:
        print(f"잘못된 입력입니다. 정답은 {correct_answer}입니다.\n")

print(f"게임이 끝났습니다. 당신의 점수는 {score}/{total_questions} 입니다!")

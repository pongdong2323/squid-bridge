import random

a=random.randrange(1,11)
print("오징어 게임을 시작하겠습니다.")
print("구슬갯수:{}".format(a))
my_marble = 10

for i in range(2):
    my = input("홀or짝 choice하세요:  ")
    betting = int(input("베팅할 구슬갯수를 입력하세요: "))

    if my == "홀" or my == "짝":
        dab = ""
        if a % 2 == 0:
            dab = "짝"
        else:
            dab = "홀"

        if my == dab:
            print("내꺼")
            my_marble = my_marble + betting
            print("내구슬 갯수: {}".format(my_marble))
            break
        
        else:
            print("옛다")
            my_marble = my_marble - betting
            print("내구슬 갯수: {}".format(my_marble))
            break
    else:
        print("다시 입력")
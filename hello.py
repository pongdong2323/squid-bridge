import random

a=random.randrange(1,11)
print("오징어 게임을 시작하겠습니다.")
print("내기 구슬갯수:{}".format(a))
my_marble = 10

for i in range(50):
    my = input("홀or짝 choice하세요:  ")
    try:
        # 구슬의 갯수 베팅
        betting = int(input("구슬 몇 개 베팅? "))
    except:
        print("숫자만 입력해라~")
        continue


    if my_marble < betting:
        print("구슬 모자름요. {}개 안에서 베팅하세요.".format(my_marble))
        continue

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
            continue
        
        else:
            print("옛다")
            my_marble = my_marble - betting
            print("내구슬 갯수: {}".format(my_marble))
            continue

        if my_marble == 0 or my_marble == 20:
            print("끝~")
            break

    else:
        print("다시 입력")
import random

a=random.randrange(1,11)
print("구슬갯수:",a)

for i in range(2):
    my = input("홀or짝 choice:  ")

    if my == "홀" or my == "짝":
        dab = ""
        if a % 2 == 0:
            dab = "짝"
        else:
            dab = "홀"

        if my == dab:
            print("딩동댕")
            break
        
        else:
            print("땡")

    else:
        print("다시 입력")
import random

a=random.randrange(1,11)
print("구슬갯수:",a)

my =input("홀or짝 choice: ")
print(my)

dab=""
if a%2==0:
    print("짝")
    dab ="짝"
else:
    print("홀")
    dab ="홀"

if my == dab:
    print("맞다")
else:
    print("빵")
    print("QKd")
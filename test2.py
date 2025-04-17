from sys import set_coroutine_origin_tracking_depth

from pyexpat.errors import messages

money = True

if money:
    print("택시를 타세요.")
else:
    print("걸어가세요.")

money = 3000
card = True
print(card)
print(money >=5000 or card)
if money >= 5000 or card:
    print("택시를 타고 가세요")
else:
    print("걸어가세요")

pocket = ['money','phone','key','card']
if ('money' in pocket) or ('card' in pocket):
    print("택시")
else:
    print("걸어가세요")

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내세요.")

if 'money' not in pocket:
    print("카드를 꺼내세요.")
print("\n새로운 실습")
pocket = ['id', 'phone']
card = True

# pocket에 money가 있으면 택시, money가 없다면, card가 있을 때 택시, 아니면 걸어가라

if ('money' in pocket) or card:
    print("택시")
else:
    if card:
        print("택시2")
    else:
        print("걸어가세요")

if 'money' in pocket:
    print("택시3")
elif card:
    print("택시4")
else:
    print("걸어가세요")

score = 70

if score >= 60:
    message = "성공"
else:
    message = "실패"

print(message)

message2 = "성공" if score >= 60 else "실패"
print(message2)

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")
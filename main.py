import random

letters = ["r", "p", "s"]
exit = "q"

while True:
    user = input("Введите букву r(ock),p(aper) или s(cissors); Нажмите q для выхода.")
    resp = random.choice(letters)
    if user == exit:
        break
    elif user == resp:
        print("ничья")
    elif user == "r" and resp == "s":
        print("победа")
    elif user == "p" and resp == "r":
        print("победа")
    elif user == "s" and resp == "p":
        print("победа")
    else:
        print("поражение")


def homework():
    down = 0
    up = 1000
    while (True):
        mid = (down + up) // 2
        print(f"Ваше число больше {mid}?")
        answer = input()
        if (answer.lower() == "да"):
            down = mid + 1
        elif (answer.lower() == "нет"):
            up = mid
        else:
            print("Неккоректный ответ")
        if (down == up):
            print(f"Ваше число - {down}")
            break

homework()
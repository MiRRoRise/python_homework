import threading
import time
import chime
from colorama import init, Fore
import re

init(autoreset=True)

def parse(times):
    """При помощи регулярного выражения считываем строку и возвращаем количество секунд для таймера"""

    sec = 0
    #Регулярное выражение
    res = re.compile(r'(\d+(?:\.\d+)?)\s*(час(?:ов)?|минут|секунд?)') #Нецелые тоже можно
    count = res.findall(times)
    for value, current in count:
        value = float(value)
        if "час" in current:
            sec += int(value * 3600)
        elif "минут" in current:
            sec += int(value * 60)
        else:
            sec += int(value)
    return sec

def timer(count, i, all_timers):
    """Создаем конкретный таймер и запускаем его"""

    while count > 0:
        time.sleep(1)
        count -= 1
        all_timers[i] = count
    chime.success()

def formats(seconds):
    """Преобразуем количество секунд в строку из часов, минут и секунд"""

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def main():
    all_timers = {}
    timers = []
    count_timers = int(input("Введите количество таймеров (1-10): "))
    for i in range(1, count_timers + 1):
        while True:
            count = parse(input(f"Введите время для {i} таймера: "))
            if count > 0:
                all_timers[i] = count
                break
            else:
                print(Fore.RED + "Некорректный ввод, попробуйте еще раз")
    for i in range(1, count_timers + 1):
        t = threading.Thread(target=timer, args=(all_timers[i], i, all_timers))
        timers.append(t)
        t.start()
    while any(t > 0 for t in all_timers.values()):
        print()
        print(Fore.BLUE + "Оставшееся время:")
        for i in range(1, count_timers + 1):
            if all_timers.get(i, 0) <= 0:
                print(Fore.GREEN + f"Таймер {i}: сработал")
            else:
                print(Fore.RED + f"Таймер {i}: {formats(all_timers.get(i, 0))}")
        time.sleep(1)
    for t in timers:
        t.join()
    print()
    print(Fore.BLUE + "Оставшееся время:")
    for i in range(1, count_timers + 1):
        print(Fore.GREEN + f"Таймер {i}: сработал")
    time.sleep(2) #Задержка, чтобы звук успел воспроизвестись

if __name__ == "__main__":
    main()

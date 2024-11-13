def q_haiku(haiku):
    """Проверка на то, является ли строка хайку"""

    correct = [5, 7, 5]
    if len(haiku) != 3:
        return "Не хайку. Должно быть 3 строки."

    for i, s in enumerate(haiku):
        count = 0
        for char in s:
            if char in "аеёиоуыэюяАЕЁИОУЫЭЮЯ":
                count += 1
        if count != correct[i]:
            return f"Не хайку. В {i + 1} строке слогов не {correct[i]}, а {count}."
    return "Хайку!"

def main():
    results = []

    with open("haiku.txt", 'r', encoding='utf-8') as f:
        strs = f.readlines()

    for s in strs:
        s = s.strip()
        haiku_result = q_haiku(s.split(' / '))
        results.append(f"{s}\n{haiku_result}\n\n")
        print(f"{s}\n{haiku_result}")

    with open("test_haiku.txt", 'w', encoding='utf-8') as f:
        f.writelines(results)

if __name__ == "__main__":
    main()


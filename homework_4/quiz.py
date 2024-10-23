import json

def load(file):
    """Загружаем список тестов"""
    with open(file, 'r', encoding="utf-8") as f:
        vocabulary = json.load(f)
    return vocabulary["tests"]

def print_test(tests):
    """Вывод списка тестов"""
    print("Выберите тест:")
    for num, test in enumerate(tests, 1):
        print(f"{num}) {test['name']}")

def print_question(question):
    """Вывод для вопросов"""
    print(question["question"])
    for num, variant in enumerate(question["variants"], 1):
        print(f"{num}) {variant}")

def get_test(tests):
    """Узнаем, какой тест был выбран"""
    while (True):
        try:
            var = int(input("Выберите номер теста: "))
            if (1 <= var <= len(tests)):
                return tests[var - 1]
            else:
                raise ValueError
        except ValueError:
            print("Неверный номер, выберите другой")

def get_answer(count):
    """Получаем вариант ответа"""
    while (True):
        try:
            var = int(input("Выберите номер ответа: "))
            if (1 <= var <= count):
                return var
            else:
                raise ValueError
        except ValueError:
            print("Неверный номер, выберите другой")

def main():
    tests = load('tests.json')
    print_test(tests)
    test = get_test(tests)
    score = count = answers = 0
    results = [] #Для записи вывода
    for question in test["questions"]:
        print_question(question)
        answer = get_answer(len(question["variants"]))
        if (question["variants"][answer - 1] == question["answer"]):
            correct = True
        else:
            correct = False
        points = question["points"]
        count += points
        if (correct):
            score += points
            answers += 1
        #Сохраняем для отчета
        results.append({
            'question': question["question"],
            'variant': question["variants"][answer - 1],
            'answer': question["answer"],
            'correct': correct,
            'points': points
        })

    #Вывод результатов
    print(f"\nТест завершен, правильных ответов {answers} из {len(test['questions'])}\nВы набрали: {score} из {count} баллов\n\nВаши ответы:")
    for result in results:
        print(f"{result['question']}\nВаш ответ - {result['variant']} (Правильный ответ - {result['answer']})")
        if (result["correct"]):
            print(f"Получено баллов за вопрос: {result['points']}/{result['points']}\n")
        else:
            print(f"Получено баллов за вопрос: 0/{result['points']}\n")

if __name__ == "__main__":
    main()

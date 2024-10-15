import random

def translate(word):
    result = ""

    trans = {
        'а': 'f', 'б': ',', 'в': 'd', 'г': 'u', 'д': 'l', 'е': 't', 'ё': '`',
        'ж': ';', 'з': 'p', 'и': 'b', 'й': 'q', 'к': 'r', 'л': 'k', 'м': 'v',
        'н': 'y', 'о': 'j', 'п': 'g', 'р': 'h', 'с': 'c', 'т': 'n',
        'у': 'e', 'ф': 'a', 'х': '[', 'ц': 'w', 'ч': 'x', 'ш': 'i',
        'щ': 'o', 'ъ': ']', 'ы': 's', 'ь': 'm', 'э': '\'', 'ю': '.',
        'я': 'z'
    }

    for y in word:
        result += trans[y]
    return result

def gen_pass(l, lang):
    password = ""

    english = {
        "actor", "bubble", "castle", "danger", "eagle", "flame", "ghost", "hazard", "igloo", "jelly",
        "kite", "lake", "moon", "nurse", "ocean", "piano", "queen", "rainbow", "sunflower", "tiger",
        "umbrella", "victory", "water", "cat", "you", "zoo", "apple", "bread", "cloud", "dance",
        "rock", "flute", "game", "honey", "island", "joke", "kangaroo", "lemon", "mouse", "noodle",
        "oak", "paint", "queen", "rain", "sail", "tune", "unicorn", "vase", "waterfall", "xenon",
        "yogurt", "zebra"
    }

    russian = {
        "аист", "баба", "ваза", "гора", "дверь", "ёж", "жена", "забор", "игра", "йога",
        "кабан", "лампа", "мама", "нога", "океан", "папа", "дом", "радар", "сова",
        "танк", "улица", "фаза", "хата", "цена", "чашка", "школа", "экран", "юбилей",
        "яблоко", "якорь", "акула", "банан", "весло", "гусь", "дама", "ежевика", "жук",
        "забава", "игрушка", "йод", "кабель", "лама", "мама", "награда", "облако", "паприка",
        "банан", "радость", "санки", "танец", "университет", "чай", "химия",
        "царь", "человек", "шахта", "энергия", "юрист", "ярмарка"
    }

    if (lang == "english"):
        for y in range(l):
            if (l - y == 1):
                password += random.choice(list(english))
            else:
                password += random.choice(list(english)) + '-'
        return password
    elif (lang == "russian"):
        for y in range(l):
            if (l - y == 1):
                password += translate(random.choice(list(russian)))
            else:
                password += translate(random.choice(list(russian))) + '-'
        return password
    else:
        return 1

count = int(input("Сколько паролей необходимо? "))
l = int(input("Какова длина пароля? "))
lang = input("Какой использовать язык? (english/russian) ").lower()
print("Ваши пароли:")

for i in range(count):
    if (gen_pass(l, lang) == 1):
        print("Неверный язык")
        break
    else:
        print(gen_pass(l, lang))




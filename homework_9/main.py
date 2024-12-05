from enigma_machine import EnigmaMachine
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
import sys
import os

def load(path):
    """Открываем файл с конфигурацией"""
    if not os.path.exists(path):
        print(f"Файл не найден: {path}")
        sys.exit(1)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config = f.read().splitlines()
    except Exception as e:
        print(f"Не удалось открыть файл: {e}")
        sys.exit(1)
    if len(config) != 4:
        print("В конфигурации должно быть 4 строки")
        sys.exit(1)
    # Записываем и возвращаем конфигурацию роторов и рефлектора
    rotors = config[:3]
    reflector = config[3]
    return rotors, reflector

def start_enigma(rotor_input, reflector_input, rotor_pos, plugboard_input, text_input):
    """Запускаем машину с заданными параметрами"""
    try:
        rotors = []
        if len(rotor_pos) != 3 or not all(c in [chr(i) for i in range(ord('A'), ord('Z') + 1)] for c in rotor_pos):
            raise ValueError("Положения роторов должны состоять из 3 заглавных символов латиницы")
        if not all(c in [chr(i) for i in range(ord('A'), ord('Z') + 1)] or c.isspace() for c in plugboard_input):
            raise ValueError("Конфигурация соединительной панели должна состоять только из заглавных символов латиницы и пробелов")
        if not all(c in [chr(i) for i in range(ord('A'), ord('Z') + 1)] or c.isspace() for c in text_input):
            raise ValueError("Текст для шифрования должен состоять только из заглавных символов латиницы и пробелов")

        for i in range(len(rotor_input)):
            rotors.append(Rotor(rotor_input[i], rotor_pos[i]))
        reflector = Reflector(reflector_input)
        plugboard = Plugboard(plugboard_input)
        enigma_machine = EnigmaMachine(rotors, reflector, plugboard)
        res = enigma_machine.process(text_input)

        print(f"Зашифрованный текст: {res}")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    if len(sys.argv) > 1 and len(sys.argv) != 5:
        print(sys.argv)
        print("Введите данные в формате: python main.py положение_роторов соединительная_панель текст_для_шифрования путь_к_конфигурации")
    elif len(sys.argv) == 5:
        rotor_pos = sys.argv[1]
        plugboard = sys.argv[2]
        text = sys.argv[3]
        path = sys.argv[4]

        rotor, reflector = load(path)
        start_enigma(rotor, reflector, rotor_pos, plugboard, text)
    else:
        print("Для работы с машиной необходимо ввести некоторые данные")
        rotor_pos = input("Введите начальное положение роторов: ")
        plugboard = input("Введите настройки соединительной панели (через пробел, например: AB CD): ")
        text = input("Введите текст для шифрования: ")
        path = input("Введите путь к файлу с конфигурацией: ")

        rotor, reflector = load(path)
        start_enigma(rotor, reflector, rotor_pos, plugboard, text)

if __name__ == '__main__':
    main()

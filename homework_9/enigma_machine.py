class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def process(self, text):
        """Основная функция работы Энигмы"""

        # Проверка на некорректный ввод
        if not isinstance(text, str) or text == "":
            raise ValueError("Ввод должен быть не пустой строкой")
        if any(not ('A' <= char <= 'Z' or char.isspace()) for char in text):
            raise ValueError("Текст не должен содержать ничего помимо заглавных букв и пробелов")

        result = []
        for char in text:
            if not ('A' <= char <= 'Z'):
                result.append(char)
                continue

            # Проходим соединительную панель
            char = self.plugboard.code(char)

            # Прямой проход через роторы
            for rotor in self.rotors:
                char = rotor.code(char)

            # Проходим через рефлектор
            char = self.reflector.code(char)

            # Обратный проход через роторы
            for rotor in reversed(self.rotors):
                char = rotor.decode(char)

            # Проходим соединительную панель
            char = self.plugboard.code(char)

            result.append(char)

            # Вращаем роторы
            self.rotors[0].rotate()
            if self.rotors[0].full():
                self.rotors[1].rotate()
                if self.rotors[1].full():
                    self.rotors[2].rotate()

        return ''.join(result)

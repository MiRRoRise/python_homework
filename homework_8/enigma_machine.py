class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def process(self, text):
        result = []
        for char in text:
            if not ('А' <= char <= 'Я'):
                result.append(char)
                continue

            # Применение соединительной панели
            char = self.plugboard.code(char)

            # Прямой проход через роторы
            for rotor in self.rotors:
                char = rotor.code(char)

            # Проход через рефлектор
            char = self.reflector.code(char)

            # Обратный проход через роторы
            for rotor in reversed(self.rotors):
                char = rotor.decode(char)

            # Применение соединительной панели
            char = self.plugboard.code(char)

            result.append(char)

            # Вращение роторов
            self.rotors[0].rotate()
            if self.rotors[0].full():
                self.rotors[1].rotate()
                if self.rotors[1].full():
                    self.rotors[2].rotate()

        return ''.join(result)

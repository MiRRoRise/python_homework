class Rotor:
    def __init__(self, value, position='A'):
        self.value = value
        self.size = len(value)
        self.pos = ord(position) - ord('A')
    # Прямое шифрование
    def code(self, char):
        index = (ord(char) - ord('A') + self.pos) % self.size
        return self.value[index]
    # Обратное шифрование
    def decode(self, char):
        index = self.value.index(char)
        return chr((index - self.pos) % self.size + ord('A'))
    # Вращение роторов
    def rotate(self):
        self.value = self.value[1:] + self.value[0]  # Циклический сдвиг
        self.pos = (self.pos + 1) % self.size
    # Проверка на возвращение в начало
    def full(self):
        return self.pos == 0
class Rotor:
    def __init__(self, value, position='А'):
        self.value = value
        self.size = len(value)
        self.pos = ord(position) - ord('А')

    def code(self, char):
        index = (ord(char) - ord('А') + self.pos) % self.size
        return self.value[index]

    def decode(self, char):
        index = self.value.index(char)
        return chr((index - self.pos) % self.size + ord('А'))

    def rotate(self):
        self.value = self.value[1:] + self.value[0]  # Циклический сдвиг
        self.pos = (self.pos + 1) % self.size

    def full(self):
        return self.pos == 0  # Проверяем, вернулся ли ротор в начальное положение

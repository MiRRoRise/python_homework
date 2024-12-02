class Rotor:
    def __init__(self, value, st, in_pos = 'А'):
        self.value = value
        self.size = len(value)
        self.st = st
        self.pos = ord(in_pos) - ord('А')

    def code(self, char):
        index = (ord(char) - ord('А') + self.pos) % self.size
        return self.value[index]

    def decode(self, char):
        index = self.value.index(char)
        return chr((index - self.pos) % self.size + ord('А'))

    def rotate(self):
        self.pos = (self.pos + 1) % self.size
        return self.value[self.pos] == self.st
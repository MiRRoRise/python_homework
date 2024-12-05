class Reflector:
    def __init__(self, value):
        self.value = value

    def code(self, char):
        index = ord(char) - ord('A')
        return self.value[index]
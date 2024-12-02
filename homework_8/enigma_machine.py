class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    def process(self, text):
        result = []
        for char in text:
            if char not in [chr(i) for i in range(ord('А'), ord('Я') + 1)]:
                result.append(char)
                continue
            char = self.plugboard.code(char)

            for rotor in self.rotors:
                char = rotor.code(char)
            char = self.reflector.code(char)

            for rotor in reversed(self.rotors):
                char = rotor.decode(char)
            char = self.plugboard.code(char)
            result.append(char)
            rotate_next = True

            for rotor in self.rotors:
                if rotate_next:
                    rotate_next = rotor.rotate()
                else:
                    break
        return ''.join(result)
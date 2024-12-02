def create_pairs(input_pairs):
    pairs = []
    for pair in input_pairs.split():
        a, b = pair
        pairs.append((a, b))
    return pairs

class Plugboard:
    def __init__(self, input_pairs):
        self.pairs = create_pairs(input_pairs)

    def code(self, char):
        for a, b in self.pairs:
            if char == a:
                return b
            elif char == b:
                return a
        return char
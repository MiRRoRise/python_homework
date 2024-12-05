def create_pairs(input_pairs):
    """Создаем пары из символов, записанных слитно"""
    pairs = []
    for pair in input_pairs.split():
        a, b = pair[0], pair[1]
        pairs.append((a, b))
    return pairs

class Plugboard:
    def __init__(self, input_pairs):
        self.pairs = create_pairs(input_pairs)
    # Замена символов
    def code(self, char):
        for a, b in self.pairs:
            if char == a:
                return b
            elif char == b:
                return a
        return char
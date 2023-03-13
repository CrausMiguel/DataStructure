class Deck:
    def __init__(self):
        self.items = []

    def is_empty(self):
        print("Is list empty? " + str(self.items == []))

    def get_size(self):
        return len(self.items)

    def insert_front(self, item):
        self.items.append(item)
        print("Inserted into front " + str(self.items))

    def insert_rear(self, item):
        self.items.insert(0, item)
        print("Inserted into rear " + str(self.items))

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def palindromo(self, palavra):
        deck = Deck()
        for c in range(0, len(palavra)):
            deck.insert_front(palavra[c].lower())
        iguais = True
        while deck.get_size() > 1 and iguais:
            first_word = deck.remove_rear()
            last_word = deck.remove_front()
            if first_word != last_word:
                iguais = False
        return iguais
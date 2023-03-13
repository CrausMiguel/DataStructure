from binary_tree import BinaryTree
from deck import Deck

if __name__ == "__main__":

    # Deck
    deck = Deck()
    print("\n--Deck--")
    deck.is_empty()
    deck.insert_front(1)
    deck.insert_front(2)
    deck.insert_rear(3)
    deck.remove_front()
    print("Front removed " + str(deck.items))
    deck.remove_rear()
    print("Rear removed " + str(deck.items))
    deck.is_empty()

    # Palindromo
    print("\n--Palindromo--")
    print(deck.palindromo("arara"))

    # BinaryTree
    print("\n--Binary Tree--")
    root = BinaryTree("A")
    root.insert_left("B")
    root.insert_right("C")

    root.get_left_child().insert_left("D")
    root.get_left_child().insert_right("E")

    root.get_right_child().insert_left("F")
    root.get_right_child().insert_right("G")

    root.get_left_child().get_left_child().insert_left("H")
    root.get_left_child().get_left_child().insert_right("I")

    root.get_left_child().get_right_child().insert_left("J")

    root.pre_order()
    print("-" * 10)
    root.in_order()
    print("-" * 10)
    root.pos_order()

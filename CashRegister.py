class Wallet:
    # A class that represents a mutable store of cash
    # Will be used as the Vending Machine's cash register
    def __init__(self):
        # money should be an array that stores identifier, value, and inventory
        money = {'W':20,
                 'T':10,
                 'F':5,
                 'O':1,
                 'Q':0.25,
                 'D':0.10,
                 'N':0.05,
                 'P':0.01}
        pass

    def add_cash(self):
        pass

    def remove_cash(self):
        pass

class CashBundle:
    # A sum of cash broken down into exact components.
    # will be used for payments, and the Wallet class
    # The distinct different between this and Wallet is that it is not persistent

# Consider moving all payment-related functions to this module

import numpy as np

usd_denominations = np.array([('W', 20), ('T', 10), ('F', 5), ('O', 1), ('Q', .25), ('D', .10), ('N', .05), ('P', .01)],
                             dtype=[('id','U1'), ('cash_value', 'f4')])

class Wallet:
    # A class that represents a mutable store of cash
    # Will be used as the Vending Machine's cash register
    def __init__(self):
        # money should be an array that stores identifier, value, and inventory
        self.money = {d['id']:0 for d in denominations}

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

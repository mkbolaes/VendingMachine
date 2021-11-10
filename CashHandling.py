import numpy as np

usd_denominations = np.array([('W', 20), ('T', 10), ('F', 5), ('O', 1),
                              ('Q', .25), ('D', .10), ('N', .05), ('P', .01)],
                             dtype=[('id','U1'), ('cash_value', 'f4')])

class Wallet:
    # A class that represents a mutable store of cash
    # Will be used as the Vending Machine's cash register
    def __init__(self, denominations):
        # money should be an array that stores identifier, value, and inventory
        self.money = {d['id']:0 for d in denominations}

        pass

    def add_cash(self, _cash_bundle):
        for i, q in _cash_bundle:
            self.money[i] += q
        pass

    def remove_cash(self, _cash_bundle):
        # check that there's enough cash to remove
        if diff_cash(_cash_bundle):
            for i, q in _cash_bundle:
                self.money[i] += q
                return
        else:
            print('Not enough cash.')
            return

    def diff_cash(self, _cash_bundle):
        # Compares current money to _cash_bundle. Returns True if _cash_bundle
        # is an existing subset of money.
        _cash_deficit = [int((self.money[i] - q) >=0) for i,q in _cash_bundle]
        return len(_cash_deficit) == sum(_cash_deficit)

class CashBundle:
    # A sum of cash broken down into exact components.
    # will be used for payments, and the Wallet class
    # The distinct different between this and Wallet is that it is not persistent
    def __init__(self, id_quantity_tuples):
        self.cash = np.array(id_quantity_tuples, dtype=[('id','U1'), ('quantity', 'i4')])

# Consider moving all payment-related functions to this module

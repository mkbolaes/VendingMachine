import pandas as pd

usd_denominations = np.array([('W', 2000), ('T', 1000), ('F', 500), ('O', 100), ('Q', 25), ('D', 10), ('N', 5), ('P', 1)],
                             dtype=[('id','U1'), ('value', 'i4')])

usd_dict = {}
for ud in usd_denominations:
    usd_dict[ud['id']] = ud['value']

class VendingMachine:
    item_max_inventory = 20
    stock_max_entries = 30

    def __init__(self):
        self._cash_register = Wallet()
        _stocklist_frame = np.ndarray((30,), dtype=[('name','U16'), ('quantity','i4'), ('price', 'f8')])
        self._stocklist = pd.DataFrame(_stocklist_frame, index=self._generate_keypad_indicies())
        pass

    def display_stocklist(self):
        available_spaces = self.check_stock()
        if available_spaces == self.stock_max_entries:
            print('Vending machine is out of stock.')
        else:
            print(self._stocklist[self._products_in_stock])
        pass

    def check_stock(self):
        # Returns the available number of spaces for new products
        self._products_in_stock = self._stocklist['quantity'] > 0
        return self.stock_max_entries - sum(self._products_in_stock)

    def check_inventory(self, name):
        if name in self._stocklist['name']:
            #return number of open spots for inventory
            pass
        else:
            #return None
            pass

    def purchase_item(self, stock_number):
        # get stock item's price
        # run payment buffer
        # subtract stock_item_price from payment_total
        # return change
        # deposit item
        # decrement inventory
        # say thank you
        # run get_stocklist
        pass

    def add_stock_item(self, name, quantity, price):
        if name not in self._stocklist['name']:
            if self.check_stock() > 0:
                # grabs first empty row
                idx,_,_,_=self._stocklist[~self._products_in_stock][0]
                self._stocklist[idx] = np.array([name, quantity, price],
                                                dtype=[('name','U16'), ('quantity','i4'), ('price', 'f8')])
                # TODO: add_item up until max inventory limit, return extra
        else:
            if self.check_inventory():
                # TODO: add_item up until max inventory limit, return extra
                pass

    def remove_stock_item(self, name, quantity):
        #remove quantity
        pass

    def _operating_buffer(self):
        # run get_stocklist
        # format print stocklist
        # prompt user to enter stock number for purchase
        # if empty, print "out of stock"
        pass

    def _generate_keypad_indicies(self, alphas='ABC', nums=range(10)):
        # Generates
        _stock_indicies = []
        for a in alphas:
            _stock_indicies += [a+str(n) for n in nums]
        return _stock_indicies[:self.stock_max_entries]

    def _payment_buffer(self, amount_due):
        accepting_payment = True
        running_total = 0
        cash_bundle = []
        while accepting_payment:
            cash_id = input('Submit payment. Submit * when payment is complete.\n')
            if cash_id == '*':
                accepting_payment = False
                return None
            elif cash_id not in accepted_denominations['id']:
                print('Invalid cash submission. Try again.')
            else:
                running_total += usd_dict[cash_id]
            if running_total >= amount_due:
                accepting_payment = False
                return cash_bundle, running_total
            else:
                print(F"Money accepted: {running_total/100:.2f}")

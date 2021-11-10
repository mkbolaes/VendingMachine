import pandas as pd

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

    def add_stock_item(self):
        #check for existence
        #if existing, check for inventory space
            #add stock or reject some
        #if doesn't exist, check for stock space
            #add new product
            #assign new stock number
        pass

    def _operating_buffer(self):
        # run get_stocklist
        # format print stocklist
        # prompt user to enter stock number for purchase
        # if empty, print "out of stock"
        pass

    def _payment_buffer(self):
        # prompt for user input, loop until "enter" is pressed
        # return payment_total
        pass

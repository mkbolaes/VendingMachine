def add_stock(name, price, number):
    pass

def purchase_item(underpay=False):
    # generate selection
    # if underpay, subtract random number between 0 and total
    # else generate payment
    # purchase item(stock_number, payment)
    # test complete prompt
    pass

def generate_selection(stocklist):
    # randomly select from integer range from stocklist length
    # get stock_number associated with selection
    # return stock_number
    pass

def generate_payment(amount):
    # modulo decrement in decreasing denominations
    # twenty, ten, five, one, quarter, dime, nickel
    # enter
    pass

def run_test_assortment():
    # add_stock, maximize inventory
    # add_stock
        # check that Vending Machine refuses stock
        # indicate success/failure
    # purchase_item, overpay with denominator
        # check that Vending Machine refuses payment if it cannot provide the change
    # add_cash
    # purchase_item, 3 levels of payment
    # drain single stock item (A1)
    # attempt to purchase the drained item
    # add new stock item
    # attempt to purchase new item
    pass

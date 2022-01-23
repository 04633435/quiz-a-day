from sortedcontainers import SortedList

class StockPrice:
    def __init__(self):
        self.price = SortedList()
        self.stockprice = {}
        self.cur = 0



    def update(self, timestamp, price):
        if timestamp in self.stockprice:
            self.price.discard(self.stockprice[timestamp])
        self.stockprice[timestamp] = price
        self.cur = max(self.cur, timestamp)


    def current(self):
        return self.stockprice[self.cur]


    def maximum(self):
        return self.price[-1]


    def minimum(self):
        return self.price[0]


if __name__ == '__main__':
    obj = StockPrice()
    stock_price_operation =  ["update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
    stock_price_stream = [[1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
    for op, val in zip(stock_price_operation, stock_price_stream):
        ob_op = getattr(obj, op)
        if op == "update":
            print(ob_op(val[0], val[1]))
        else:
            print(ob_op())

    a = {}
    
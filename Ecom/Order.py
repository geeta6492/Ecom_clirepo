
class Order:
    number=1110
    all_orders = []
    def __init__(self,pid,pric,pqty,bill,status):
        Order.number+=1
        self.orderNo=Order.number
        self.orderProductId = pid
        self.orderProductPrice=pric
        self.orderQty=pqty
        self.totalBill=bill
        self.orderStatus = status

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

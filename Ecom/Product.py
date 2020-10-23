

class Product:

    def __init__(self,pid,pnm,pcat,pqty,pprice):
        self.productId=pid
        self.productName=pnm
        self.productCategory=pcat
        self.productQuantity=pqty
        self.productPrice=pprice

    def __str__(self):
        return f'\n{self.__dict__}'

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return self.productName.__hash__()

    def __eq__(self, other):
        return self.productName==other.productName

class Customer:

    def __init__(self,cid,cnm,caddress,account):
        self.customerId=cid
        self.customerName=cnm
        self.customerAddress=caddress
        self.customerAccount=account
        self.purchasedProducts=set()

    def __str__(self):
        #return f'\n{self.__dict__}'
        return '''
            Cust Id : {}
            Cust Name: {}
            Cust Address : {}
            Cust Account : {}
            Cust Products : {}
        '''.format(self.customerId,self.customerName,self.customerAddress,self.customerAccount,self.purchasedProducts)
    def __repr__(self):
        return str(self)


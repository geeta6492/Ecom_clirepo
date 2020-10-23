
class Address:

    def __init__(self,aid,city,state,pin):
        self.addressId=aid
        self.addressCity=city
        self.addressState=state
        self.addressPincode=pin

    def __str__(self):
        #return f'\n{self.__dict__}'
        return '''
                Id : {}
                City : {}
                State : {}
                Pincode : {}
        '''.format(self.addressId,self.addressCity,self.addressState,self.addressPincode)

    def __repr__(self):
        return str(self)

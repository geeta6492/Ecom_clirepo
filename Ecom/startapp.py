
from Ecom.application_data import *
from Ecom.ShoppingService import ServiceImpl
from Ecom.application_data import *
if __name__ == '__main__':
    owner = generate_owner_info()
    cust = generate_customer_info()


    print('Owner balance ',owner.venAccount.accountBalance)
    print('Customer balance ',cust.customerAccount.accountBalance)

    service = ServiceImpl()
    service.purchase_product('Remote','B',3,owner,cust)

    print('Owner balance ', owner.venAccount.accountBalance)
    print('Customer balance ', cust.customerAccount.accountBalance)

    service.refund_product(Order.all_orders[0],owner,cust)


    print(Order.all_orders)

    print('Owner balance ', owner.venAccount.accountBalance)
    print('Customer balance ', cust.customerAccount.accountBalance)

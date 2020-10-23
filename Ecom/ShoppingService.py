
from abc import ABC,abstractmethod
from Ecom.application_data import *
import copy

class Service(ABC):

    @abstractmethod
    def purchase_product(self):
        pass

    @abstractmethod
    def refund_product(self):
        pass

    @abstractmethod
    def product_inquiry(self):
        pass

class ServiceImpl(Service):

    def purchase_product(self,pnm,cat,pqty,ownerinfo,custinfo):

        productAvlb = False
        productCat = False
        productQty =False
        balancepass=False
        for prod in ownerinfo.vendorInventory:
            if prod.productName==pnm:
                productAvlb=True
                if prod.productCategory==cat:
                    productCat=True
                    if prod.productQuantity>=pqty:
                        productQty=True
                        totalBill = pqty*prod.productPrice
                        if custinfo.customerAccount.accountBalance>=totalBill+5000:
                          balancepass=True

                          custinfo.customerAccount.accountBalance-=totalBill
                          ownerinfo.venAccount.accountBalance+=totalBill


                          prod.productQuantity-=pqty
                          uprod = copy.deepcopy(prod)
                          uprod.productQuantity=pqty
                          custinfo.purchasedProducts.add(uprod)
                          order1 = Order(pid=prod.productId,pric=prod.productPrice,
                                  pqty=pqty,bill=totalBill,status='Completed')
                          Order.all_orders.append(order1)
                          print('Order placed Successfully...',order1.orderNo)
                        else:
                            print('Insufficient Balance...!cannot process the order')
                            break
                    else:
                        print('Quantities not avaiable')
                        break
                else:
                    print("category not found")
                    break

        if productAvlb==False:
            print("product not avaiable with vendor...!")

    def refund_product(self,order,ownerinfo,custinfo):
        print('Processing refund for ',order.orderNo)
        for prod in ownerinfo.vendorInventory:
            if order.orderProductId== prod.productId:
                prod.productQuantity+=order.orderQty
                for cprod in custinfo.purchasedProducts:
                    if cprod.productId==order.orderProductId:
                        custinfo.purchasedProducts.remove(cprod)
                        custinfo.customerAccount.accountBalance+=order.totalBill
                        ownerinfo.venAccount.accountBalance-=order.totalBill
                        print('Refund processed...!')
                        order1 = copy.deepcopy(order)
                        order1.orderNo=9999
                        order1.orderStatus='Refund Proceessed'
                        Order.all_orders.append(order1)
                        break

    def product_inquiry(self):
        pass


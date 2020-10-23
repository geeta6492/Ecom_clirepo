import unittest
from Ecom.ShoppingService import ServiceImpl

class Test_authenticatefun(unittest.TestCase):

    def setUp(self):
        self.service=ServiceImpl()

    def test_valid_product(self):
        self.assertEqual(self.service.purchase_product("Mobile", "Mobile"),"Quantities not available")

    def test_invalid_product(self):
        self.assertEqual(self.service.purchase_product("charger", "USB"), "category not found")

    def test_invalid_balance(self):
        self.assertEqual(self.service.purchase_product("accountbalance", "bill"), "order placed successfully")



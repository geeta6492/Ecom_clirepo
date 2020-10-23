import unittest
from Ecom.Unit_Testing.Login_services import LoginserviceImpl

class Test_authenticatefun(unittest.TestCase):

    def setUp(self):
        self.service=LoginserviceImpl()

    def test_valid_username_password(self):
        self.assertEqual(self.service.authenticate("root", "root"),"Login Sucessfully")

    def test_invalid_username(self):
        self.assertEqual(self.service.authenticate("Geeta", "root"), "Invalid Username or password")

    def test_invalid_password(self):
        self.assertEqual(self.service.authenticate("root", "geeta"), "Invalid Username or password")

    def test_invalid_username_password(self):
        self.assertEqual(self.service.authenticate("Geeta", "roott"), "Invalid Username or password")

    def test_empty_username(self):
        self.assertEqual(self.service.authenticate(None, "root"), "Invalid creadientials")

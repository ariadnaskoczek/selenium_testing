import unittest

# Pobierz testy, które chcesz uruchomić
from my_project.page_object_pattern.tests.login_page_test import LoginTest
from my_project.page_object_pattern.tests.product_page_test import TestProduct

login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
product_tests = unittest.TestLoader().loadTestsFromTestCase(TestProduct)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([login_tests, product_tests])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
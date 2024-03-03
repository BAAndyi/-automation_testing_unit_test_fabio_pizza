import unittest

import HtmlTestRunner

from test_categorie_combo import Categorie_combo
from test_contact import Contact
from test_homepage import Test_homepage
from test_log_in import Test_login
from test_scoatem_ingredient import Test_scoatem_ingredient
from test_search import Test_search
from test_shopping_cart import Test_shopping



class TestSuite(unittest.TestCase):

        def test_suite(self):
                teste_de_rulat = unittest.TestSuite()
                teste_de_rulat.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(Categorie_combo),
                unittest.defaultTestLoader.loadTestsFromTestCase(Contact),
                unittest.defaultTestLoader.loadTestsFromTestCase(Test_homepage),
                unittest.defaultTestLoader.loadTestsFromTestCase(Test_login),
                unittest.defaultTestLoader.loadTestsFromTestCase(Test_scoatem_ingredient),
                unittest.defaultTestLoader.loadTestsFromTestCase(Test_search),
                unittest.defaultTestLoader.loadTestsFromTestCase(Test_shopping)])

                runner = HtmlTestRunner.HTMLTestRunner\
                                (
                combine_reports=True,
                report_title = "Test execution report",
                report_name = "Test results"
        )

                runner.run(teste_de_rulat)
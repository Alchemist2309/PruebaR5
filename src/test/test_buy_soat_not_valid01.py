import unittest
import time
from selenium import webdriver


class TestBuyNotValid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_02(self):
        # Ingreso a la plataforma de falabella
        self.driver.get("https://soat.segurosfalabella.com.co")

        # ingresar placa y aceptar termino
        self.driver.find_element_by_xpath("//input[@id='mat-input-1']").clear()
        self.driver.find_element_by_id("mat-input-1").click()
        self.driver.find_element_by_id("mat-input-1").clear()
        self.driver.find_element_by_id("mat-input-1").send_keys("55552")
        self.driver.find_element_by_css_selector("#mat-slide-toggle-1").click()
        time.sleep(5)
        self.assertEqual("No se encuentran datos relacionados con la placa", self.driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-0']/app-error/div/h2").text)
        self.driver.save_screenshot("test_buy_soat_not_valid01.png")

    def tearDown(self):
        self.driver.quit()
        


if __name__ == '__main__':
    unittest.main()
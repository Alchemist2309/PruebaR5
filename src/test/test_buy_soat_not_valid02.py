import unittest
import time
from selenium import webdriver


class TestBuyNotValid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_01(self):
        # Ingreso a la plataforma de falabella
        self.driver.get("https://soat.segurosfalabella.com.co")

        # ingresar placa y aceptar termino
        self.driver.find_element_by_xpath("//input[@id='mat-input-1']").clear()
        self.driver.find_element_by_xpath("//input[@id='mat-input-1']").send_keys("XIY70C")
        self.driver.find_element_by_xpath("//form").click()
        self.driver.find_element_by_css_selector("div.mat-slide-toggle-thumb").click()
        self.driver.find_element_by_xpath("//div[4]/button/span").click()
        self.driver.find_element_by_xpath(
            "//body/app-root[1]/app-sale[1]/app-step0[1]/app-sidenav-menu[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/div[1]/div[1]/div[1]/app-quotation-form[1]/div[1]/div[3]/form[1]/div[4]/div[1]/div[1]/mat-slide-toggle[1]/label[1]/div[1]/div[1]/div[1]")
        time.sleep(5)

        # accediendo a la siguiente pestaña
        self.Enlace = self.driver.find_element_by_xpath(
            "//body/app-root[1]/app-sale[1]/app-step0[1]/app-sidenav-menu[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/div[1]/div[1]/div[1]/app-quotation-form[1]/div[1]/div[4]/button[1]")
        self.Enlace.click()

        # seleccionando beneficio
        self.driver.find_element_by_xpath("//div[@id='cdk-accordion-child-12']/div/div/app-gift-chooser/div/div[2]/div/div[3]/button/span").click()

        # ingresando informacion
        self.driver.find_element_by_css_selector("svg.mat-datepicker-toggle-default-icon.ng-star-inserted").click()
        self.driver.find_element_by_xpath("//mat-calendar[@id='mat-datepicker-0']/mat-calendar-header/div/div/button/span").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        self.driver.find_element_by_xpath("//mat-calendar[@id='mat-datepicker-0']/div/mat-multi-year-view/table/tbody/tr/td/div").click()
        self.driver.find_element_by_xpath("//mat-calendar[@id='mat-datepicker-0']/div/mat-year-view/table/tbody/tr[2]/td/div").click()
        self.driver.find_element_by_xpath("//mat-calendar[@id='mat-datepicker-0']/div/mat-month-view/table/tbody/tr[2]/td/div").click()
        self.driver.find_element_by_xpath("//div[@id='cdk-accordion-child-10']/div/div/div[4]/div[2]/mat-form-field/div/div/div[3]").click()
        self.driver.find_element_by_xpath("//mat-option[@id='mat-option-0']/span").click()
        self.driver.find_element_by_xpath("//input[@id='mat-input-3']").clear()
        self.driver.find_element_by_xpath("//input[@id='mat-input-3']").send_keys("1231273123")
        self.driver.find_element_by_xpath("//input[@id='mat-input-4']").clear()
        self.driver.find_element_by_xpath("//input[@id='mat-input-4']").send_keys("alchemist23091102@gmail.com")
        self.driver.find_element_by_xpath("//input[@id='mat-input-5']").clear()
        self.driver.find_element_by_xpath("//input[@id='mat-input-5']").send_keys("3000000000")

        # boton continuar
        self.driver.find_element_by_xpath("//body/app-root[1]/app-sale[1]/app-step0[1]/section[1]/div[1]/section[1]/div[1]/app-vehicle-form[1]/form[1]/div[2]/button[1]").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
from excel_lib import read_locators
from selenium_wrapper import SeleniumWrapper

class HomePage(SeleniumWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        
    locators = read_locators("homepage")
    def click_login(self):
        element = HomePage.locators['lnk_login']
        self.click_element(element)
    
    def click_register(self):
        element = HomePage.locators['lnk_register']
        self.click_element(element)

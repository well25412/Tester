from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from homepage import HomePage
from loginpage import LoginPage
from selenium_wrapper import SeleniumWrapper
from config import Config  


def test_login(setup):
    hp = HomePage(setup)
    hp.click_login()
    lp = LoginPage(setup)
    lp.enter_email("helloworld@gmail.com")
    lp.enter_password("password123")
    lp.click_login()
    

    

                   

##class TestSpam:
##    def test_spam(self):
##        print("Executing spam.......")
##
##class TestDemo:
##    def test_demo(self):
##        print("Executing Demo.....")

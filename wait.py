from selenium.webdriver.support.select import Select
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from config import Config
from selenium import webdriver

class Visible(visibility_of_element_located):

    def __init__(self,locator):
        super().__init__(locator)

    def __call__(self,driver):
        result = super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:return False


def _wait(func):
     def wrapper(*args,**kwargs):
        instance = args[0]
        locator  = args[1]
        w = WebDriverWait(instance.driver,Config.MAX_TIME)
        v = Visible(locator)
        w.until(v,message = "wait................")
        return func(*args,**kwargs)
     return wrapper



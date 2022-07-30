from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium_wrapper import SeleniumWrapper
from config import Config
from pytest import fixture


@fixture()
def setup():
    print("Running setup.....")
    driver = Chrome(Config.DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    sleep(3)
    yield driver
    print("Closing Browser....")
    driver.close()

@fixture(scope ="class")
def hello():
    print("hello")
    yield("hi there")
    print("bye")

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_by_id(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    input_box = driver.find_element(By.ID, "user-message")
    input_box.send_keys("Hola mundo")
    assert input_box.get_attribute("value") == "Hola mundo"

def test_by_name(driver):
    driver.get("https://testautomationpractice.blogspot.com/")
    element = driver.find_element(By.NAME, "1307673142697428135")
    assert element.tag_name == "a"

def test_by_xpath(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    element = driver.find_element(By.XPATH, "//input[@id='username']")
    element.send_keys("admin")
    assert element.get_attribute("value") == "admin"

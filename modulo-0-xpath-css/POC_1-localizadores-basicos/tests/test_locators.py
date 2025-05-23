
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
    try:
        input_box = driver.find_element(By.ID, "user-message")
        input_box.send_keys("Prueba ID")
        assert input_box.get_attribute("value") == "Prueba ID"
    except Exception as e:
        pytest.fail(f"By.ID test failed: {e}")

def test_by_name(driver):
    driver.get("https://testautomationpractice.blogspot.com/")
    try:
        search_input = driver.find_element(By.NAME, "q")
        search_input.send_keys("Selenium")
        assert search_input.get_attribute("value") == "Selenium"
    except Exception as e:
        pytest.fail(f"By.NAME test failed: {e}")

def test_by_class_name(driver):
    driver.get("https://www.demoblaze.com/")
    try:
        element = driver.find_element(By.CLASS_NAME, "navbar-brand")
        assert "PRODUCT STORE" in element.text
    except Exception as e:
        pytest.fail(f"By.CLASS_NAME test failed: {e}")

def test_by_xpath(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    try:
        username_input = driver.find_element(By.XPATH, "//input[@id='username']")
        username_input.send_keys("admin")
        assert username_input.get_attribute("value") == "admin"
    except Exception as e:
        pytest.fail(f"By.XPATH test failed: {e}")

def test_by_css_selector(driver):
    driver.get("https://www.demoblaze.com/")
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".navbar-brand")
        assert element.text.strip() == "PRODUCT STORE"
    except Exception as e:
        pytest.fail(f"By.CSS_SELECTOR test failed: {e}")

def test_by_link_text(driver):
    driver.get("https://the-internet.herokuapp.com/")
    try:
        link = driver.find_element(By.LINK_TEXT, "Form Authentication")
        assert link.get_attribute("href").endswith("/login")
    except Exception as e:
        pytest.fail(f"By.LINK_TEXT test failed: {e}")

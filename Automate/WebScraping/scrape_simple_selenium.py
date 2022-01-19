from selenium import webdriver
from selenium.webdriver.edge.service import Service
# set uptions to make browsing easier


def get_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("excludeSwitches")
    options.add_argument("disable-blink-features=AutomationControlled")

    s = Service('/Users/christopherbeier/edgedriver_mac64/msedgedriver')
    driver = webdriver.Edge(service=s, options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(
        by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text


print(main())

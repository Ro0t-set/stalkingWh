from selenium import webdriver

driver = webdriver.Remote(
    desired_capabilities=webdriver.DesiredCapabilities.CHROME,
    command_executor='http://127.0.0.1:4444/wd/hub')
driver.get('http://www.google.com')

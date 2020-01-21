import time
from selenium import webdriver
from selenium.webdriver import ActionChains

try:
    s = 11
    driver = webdriver.Chrome(executable_path="D:\\Downloaded\\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")

    driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
    driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
    driver.find_element_by_xpath("//input[@id='btnLogin']").click()

    admin = driver.find_element_by_xpath("//b[contains(text(),'Admin')]")
    usermanagement = driver.find_element_by_xpath("//a[@id='menu_admin_UserManagement']")
    users = driver.find_element_by_xpath("//a[@id='menu_admin_viewSystemUsers']")

    action = ActionChains(driver)
    action.move_to_element(admin).move_to_element(usermanagement).move_to_element(users).click().perform()
    driver.close()
    driver.quit()
except ActionChains:
    print('ActionChains error')



from selenium import webdriver
from selenium.webdriver import ActionChains

driver= webdriver.Chrome(executable_path="D:\\Downloaded\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

drag = driver.find_element_by_xpath("//p[contains(text(),'Drag me to my target')]")
drop = driver.find_element_by_xpath("//div[@id='droppable']")
actions = ActionChains(driver)
actions.drag_and_drop(drag, drop).perform()
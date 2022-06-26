import time
from selenium import webdriver
from selenium.webdriver.common.by import By


full_name = 'userName'
email = 'userEmail'
current_address = 'currentAddress'
permanent_address = 'permanentAddress'
submit_btn = 'submit'
name_result = '//p[@id="name"]'
email_result = '//p[@id="email"]'
permanent_result = '//p[@id="permanentAddress"]'
current_result = '//p[@id="currentAddress"]'

driver = webdriver.Chrome('C:/Users/User/PycharmProjects/selenium_tasks/chromedriver.exe')

try:
    driver.get('https://demoqa.com/text-box')
    driver.find_element(By.ID, full_name).send_keys('Max')
    driver.find_element(By.ID, email).send_keys('max@mail.com')
    driver.find_element(By.ID, current_address).send_keys('street 123')
    driver.find_element(By.ID, permanent_address).send_keys('street 1210')
    time.sleep(5)
    driver.find_element(By.ID, submit_btn).click()
    time.sleep(2)
    em_res = driver.find_element(By.XPATH, email_result)
    name_res = driver.find_element(By.XPATH, name_result)
    current_res = driver.find_element(By.XPATH, current_result)
    per_res = driver.find_element(By.XPATH, permanent_result)

    assert em_res.text == 'Email:max@mail.com', 'Invalid Email'
    assert name_res.text == 'Name:Max', 'Invalid name'
    assert current_res == 'Current Address :street123', 'Invalid Current Address'
    assert per_res.text == 'Permananet Address :street 1210', 'Invalid Permanent Address'
finally:
    driver.quit()



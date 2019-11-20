import time

from selenium import webdriver

driver = webdriver.Chrome("../../drivers/chromedriver.exe")

#driver.fullscreen_window()

driver.get("http://google.com")
driver.find_element_by_class_name("gb_g").click()

driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a").click()

if len(driver.window_handles) > 1:
    driver.switch_to_window(driver.window_handles[1])
    driver.find_element_by_css_selector("input[name='identifier']").send_keys("eversoftnepal@gmail.com")
    #driver.find_element_by_id("identifierId").send_keys("thejune23rd@gmail.com")
    driver.find_element_by_class_name("RveJvd").click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("input[name='password']").send_keys("yourpassword")
    driver.find_element_by_class_name("RveJvd").click()

    # val = driver.find_element_by_css_selector(".J-KU.J-KU-KO.a65").get_attribute("aria-selected")
    contacts = driver.find_element_by_css_selector("div[tabid='contacts']").get_attribute("aria-selected")
    chat = driver.find_element_by_css_selector("div[tabid='chat']").get_attribute("aria-selected")

    if contacts != "true":
        driver.find_element_by_css_selector("div[tabid='contacts']").click()

    # if driver.find_element_by_css_selector(".HfhnEf").get_attribute("hovercard-email") == "Dhpradeep25@gmail.com":
    #     driver.find_element_by_css_selector(".HfhnEf").click()

    menu = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[3]/div/div[1]/div/div/a")
    menu.click()
    hangout = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[3]/header/div[2]/div[4]/ul[2]/li[5]/a/span[1]")
    hangout.click()


time.sleep(122)
driver.quit()

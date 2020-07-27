from selenium import webdriver
import time


# driver = webdriver.Chrome(r"Ibrahim\Proje\Drivers\chromedriver.exe")
driver = webdriver.Firefox(executable_path=r"Egzersizler\Sinan\Proje2\Drivers\geckodriver.exe")
url = "http://www.vektorelakademi.com"

driver.get(url)
time.sleep(2)

driver.maximize_window()
driver.save_screenshot("deneme.png")

time.sleep(3)
driver.get(r"http://www.sahibinden.com")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
driver.close()
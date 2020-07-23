from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("https://www.instagram.com")
time.sleep(4)

browser.find_element_by_name( 'username' ).send_keys( "xxx" )
browser.find_element_by_name( 'password' ).send_keys( "xxx" )
Giris_yap_buton= browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
Giris_yap_buton.click()
time.sleep(9)
cikis_buton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
cikis_buton.click()

time.sleep(4)
browser.close()

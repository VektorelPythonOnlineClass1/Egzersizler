from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username1 = input("kullanıcı adınız: ")
password1 = input("şifreniz: ")
aramak = input("aramak istediğiniz kişi : ")

browser = webdriver.Firefox()
browser.get("https://www.instagram.com")
time.sleep(3)


kllnci = browser.find_element_by_name("username")
sfre = browser.find_element_by_name("password")
kllnci.send_keys(username1)
sfre.send_keys(password1)

giris_yap = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div")
giris_yap.click()

time.sleep(4)


simdi_degil = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
simdi_degil.click()

time.sleep(2)

simdi_degil2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
simdi_degil2.click()

time.sleep(2)

arama = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
arama.send_keys(aramak)


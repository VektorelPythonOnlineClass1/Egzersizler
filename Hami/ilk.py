from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\hamik\Desktop\Vektörel Bilişim\KendiNotlarım\projelerim\boot\chromedriver.exe")

browser.get('http://www.hamikeserci.com/')

sleep(5)

browser.close()
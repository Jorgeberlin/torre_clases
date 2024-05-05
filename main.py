from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

usuario = 'jorpeberlin@gmail.com'
pwd = 'D5l8EHD9Jr$Y'


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def click(xpath):
    time.sleep(2)
    element = driver.find_element(By.XPATH, xpath)
    element.click()


def write(xpath, text):
    time.sleep(0.1)
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)


service = Service("chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get("https://deportesweb.madrid.es/DeportesWeb/Login")
click('/html/body/div[1]/div/a')
click('//*[@id="ContentFixedSection_uSecciones_divSections"]/section/div[2]/div/div/div[2]/article[1]/div')
write('//*[@id="ContentFixedSection_uLogin_txtIdentificador"]', usuario)
write('//*[@id="ContentFixedSection_uLogin_txtContrasena"]', pwd)
click('//*[@id="ContentFixedSection_uLogin_btnLogin"]')
time.sleep(1)
click('//*[@id="ContentFixedSection_uSecciones_divSections"]/section[4]/div[2]/div/div/div[2]/article[3]/div')
click('//*[@id="ContentFixedSection_uSecciones_divSections"]/section/div[2]/div/div/div[2]/article[3]/div')
click('//*[@id="ContentFixedSection_uReservaEspacios_uCentrosSeleccionar_divCentros"]/ul/li[41]/a/div[1]/img')
click('//*[@id="ContentFixedSection_uReservaEspacios_uUsosSeleccionar_divUsos"]/ul/li/a/div[2]')
time.sleep(200)

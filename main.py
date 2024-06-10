from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#### CONFIG ZONE ####
usuario = 'jorpeberlin@gmail.com'
pwd = 'D5l8EHD9Jr$Y'
dia = 1                                 # Cambiar esto para jugar el día que se dese

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

#### CONFIG ZONE ####

def click(xpath):
    time.sleep(2)
    element = driver.find_element(By.XPATH, xpath)
    element.click()


def write(xpath, text):
    time.sleep(3)
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)

# Entro en el calendario
service = Service("chromedriver.exe")  
driver = webdriver.Chrome(service=service)
driver.get("https://deportesweb.madrid.es/DeportesWeb/Login")
click('/html/body/div[1]/div/a')
click('//*[@id="ContentFixedSection_uSecciones_divSections"]/section/div[2]/div/div/div[2]/article[1]/div')
write('//*[@id="ContentFixedSection_uLogin_txtIdentificador"]', usuario)
write('//*[@id="ContentFixedSection_uLogin_txtContrasena"]', pwd)
click('//*[@id="ContentFixedSection_uLogin_btnLogin"]')
click('//*[@id="ContentFixedSection_uSecciones_divSections"]/section[4]/div[2]/div/div/div[2]/article[3]/div')
click('//*[@id="ContentFixedSection_uSecciones_divSections"]/section/div[2]/div/div/div[2]/article[3]/div')
click('//*[@id="ContentFixedSection_uReservaEspacios_uCentrosSeleccionar_divCentros"]/ul/li[41]/a/div[1]/img')
click('//*[@id="ContentFixedSection_uReservaEspacios_uUsosSeleccionar_divUsos"]/ul/li/a/div[2]')

for i in range(6, 0, -1):
    # Pincho en la fecha disponible
    print(f'Pincho en la fila{i}')
    click(f'//*[@id="ContentFixedSection_uReservaEspacios_uFechaSeleccionar_datetimepicker"]/div/ul/li[1]/div/div[1]/table/tbody/tr[{i}]/td[{dia}]')
    time.sleep(0.2)

# Pincho en continuar
click('//*[@id="ContentFixedSection_uReservaEspacios_uFechaSeleccionar_btnContinuar"]')
time.sleep(1)

# Reservo 2 horas en la pista 3
hora_1 = "1630"                  # Importante dejar espacio antes para que fucione bien.
hora_2 = "2030"
pista_1 = "19"
pista_2 = "20"
pista_3 = "21"

click(f'//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003{pista_3}{hora_2}"]')
     
# Reservo luz
alert = driver.switch_to.alert

# Accept the alert
alert.accept()
time.sleep(1)
# Reservo la pista
click('//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_btnReservar"]')

# Pago la pista
click('//*[@id="ContentFixedSection_uCarritoConfirmar_btnConfirmCart"]')

#//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003 19 1430"]
#//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003 19 1530"]
#//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003 20 1530"]
#//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003 21 1530"]
#//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003 19 1530"]
#//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003 21 1630"]


#19,20,21 es pista (1,2,3)
# 1430 y 1530 son las horas


#<img id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003191630" blnignorarluz="False" estado="Libre" onclick="javascript:celdaCuadrante('1003191630','100319','16:30','¿Desea que la reserva lleve iluminación?')" src="../../../Images/libre.jpg" alt="img1003191630" style="cursor:pointer;">
#<img id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003191630" blnignorarluz="False" estado="Libre" onclick="javascript:celdaCuadrante('1003191630','100319','16:30','¿Desea que la reserva lleve iluminación?')" src="../../../Images/libre.jpg" alt="img1003191630" style="cursor:pointer;">
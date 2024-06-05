import math
import datetime


# Miro qué día es hoy
today = datetime.date.today()

# Miro en qué año estoy
current_year = datetime.date.today().year
fecha_current_year = datetime.date(current_year, 1, 1)  # June 1, 2024

# Calculo cuantos días han pasado desde el 1 de enero del año en el que estoy
diferencia = today - fecha_current_year
dias = diferencia.days

bloques_mes = dias/7
fila_calendario_completo = math.ceil(bloques_mes)
fila_calendario_web = math.floor(fila_calendario_completo%6)

print(fecha_current_year, today, bloques_mes, fila_calendario_completo, fila_calendario_web)





hora_1 = " 1630"
hora_2 = " 2030"
pista_3 = " 21"

print(f'//*[@id="ContentFixedSection_uReservaEspacios_uReservaCuadrante_img1003{pista_3}{hora_1}"]')
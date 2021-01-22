#en los programas de selenium desde python
import time

from selenium import webdriver #navegador
from selenium.webdriver.firefox.options import Options

#config del driver que en este caso el navegador es firefox


opciones=Options()
opciones.headless = True #hacer el trabajo sin ver pantalla del ordenador

navegador= webdriver.Firefox(executable_path='./drivers/geckodriver', options=opciones)
navegador.set_window_position(0,0)
navegador.set_window_size(800,500)
#abrir navegador en una ruta
navegador.get('https://google.es')
##para tener tiempo para ver 5 segundos

#identificar elementos y actuacion
navegador.find_element_by_xpath("//input[@name='q'").send_keys('Sevilla')

time.sleep(2)
#navegador.find_element_by_xpath("//input[@name='btnK'").click()
time.sleep(3)
estadisticas=navegador.find_element_by_xpath("//div[@id='resul-stats']").text
print(estadisticas)
#cerrar navegador
navegador.quit()

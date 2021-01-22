#en los programas de selenium desde python
import time
from selenium import webdriver #navegador
from selenium.webdriver.firefox.options import Options
import os
#config del driver que en este caso el navegador es firefox

def hacer_login(usu, clave,nombre_prueba, carpeta):

    opciones=Options()
    opciones.headless = True #hacer el trabajo sin ver pantalla del ordenador

    navegador= webdriver.Firefox(executable_path='./drivers/geckodriver', options=opciones)
    navegador.set_window_position(0,0)
    navegador.set_window_size(1000,500)
    #abrir navegador en una ruta
    navegador.get('http://testing-ground.scraping.pro/login')


    #identificar elementos y actuacion
    navegador.find_element_by_xpath("//input[@id='usr'").send_keys(usu)
    navegador.find_element_by_xpath("//input[@name='pwd'").send_keys(clave)
    #crear carpeta
    directorio = carpeta + '/capturas/' + nombre_prueba
    try:
        os.stat(directorio)
    except:
        os.makedirs(directorio)

    #foto antes de submit en carpeta fija
    #navegador.save_screenshot('./capturas/'+nombre_prueba+'antes_del_login.png')

    #foto con los datos rellenos pero con scroll para asegurar foto
    ubicacion=navegador.find_element_by_xpath("//input[@id='usr'").location_once_scrolled_into_view
    #pongo borde a todo el formulario
    remarcar_elemento(navegador,"//form")
    navegador.save_screenshot(directorio + '/antes_del_login.png')

    #time.sleep(2)
    navegador.find_element_by_xpath("//input[@type='submit']").click()
    #time.sleep(3)
    #resultado = navegador.find_element_by_xpath("//h3[@class='success']").text
    resultado = navegador.find_element_by_xpath("//h3[@class='success' or @class='success'] ").text
    #navegador.save_screenshot('./capturas/' + nombre_prueba + 'despues_del_login.png')
    navegador.save_screenshot(directorio + '/despues_del_login.png')
    print(resultado)

    #foto despues
    #scroll al sitio
    ubicacion = navegador.find_element_by_xpath("//h3[@class='success' or @class='error']").location_once_scrolled_into_view
    # Hacer borde alrededor del texto
    borde_original = remarcar_elemento(navegador, "//h3[@class='success' or @class='error']")
    navegador.save_screenshot(directorio + '/despues_del_login_con_borde.png')
    # Restituyo el borde original
    remarcar_elemento(navegador, "//h3[@class='success' or @class='error']", borde_original)
    navegador.save_screenshot(directorio + '/despues_del_login.png')
    # Cerrar el navegador
    #cerrar navegador
    navegador.quit()

    return resultado

def remarcar_elemento(navegador, xpath, estilo='4px solid red'):
    # Buscamos el elemento
    elemento = navegador.find_element_by_xpath(xpath)
    # Recuperamos el borde que tenia
    original=navegador.execute_script("return arguments[0].style.border;",elemento)
    # Ponemos el nuevo borde
    navegador.execute_script("arguments[0].style.border = '" + estilo + "';",elemento)
    return original
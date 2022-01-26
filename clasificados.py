from selenium import webdriver  
import time
from selenium.webdriver.common import keys  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def postClasificado(quote):
    #VARIABLES DEL ANUNCIO
    titulo = 'Ram 1500!!'
    marca = 'Ram'
    modelo = 'Ram Laramie'
    ano = str(2019)
    transmision = 'Transmision Automatica'
    millaje = str(0)
    precio = '2000'
    descripcion = quote




    print("sample test case started")  

    #file_path, file_name, descripcion, count = download_email()
    
    #Instancia de la clase Webdriver.
    driver = webdriver.Chrome() 
    #titulo = file_name
    #Objeto busca website
    driver.get("https://www.clasificadosonline.com/D/C/Ads/AdminNuevospr.asp")
    driver.find_element_by_name("UserName").send_keys("jcmeji1772@yahoo.com")
    driver.find_element_by_name("Password").send_keys("sold1969")
    driver.find_element_by_name("Login").send_keys(Keys.ENTER)
    time.sleep(3)

    driver.find_element_by_link_text("Puerto Rico - Auto, Camiones Venta").send_keys(Keys.ENTER) 
    time.sleep(3)  

    #titulo
    driver.find_element_by_name("ctl00$mc$txtAreaComment").send_keys(titulo)
    time.sleep(3)

    #marca
    sel1 = Select(driver.find_element_by_id("mc_ddlMake"))
    sel1.select_by_visible_text(marca)
    time.sleep(3)

    #Modelo
    sel2 = Select(driver.find_element_by_id("mc_ddlModel"))
    sel2.select_by_visible_text(modelo)

    #Año
    sel3 = Select(driver.find_element_by_id("mc_ddlYear"))
    sel3.select_by_value(ano)


    #Transmision
    sel4 = Select(driver.find_element_by_id("mc_ddlTransmission"))
    sel4.select_by_value('Transmision Automatica')

    #Precio
    driver.find_element_by_id("mc_txtPrice").send_keys(precio)

    #Pueblo
    sel5 = Select(driver.find_element_by_id("mc_ddlTown"))
    sel5.select_by_value("1864")
    time.sleep(5)

    #descripcion
    driver.find_element_by_id("mc_txtDesc").send_keys(descripcion)


    fcount = 0
    for x in range(1, count+1):
        print(x)
        file = f'C:/Users/cas/Pictures/Carros/{file_name}{x}.jpeg'
        driver.find_element_by_id(f'ctl00_mc_RauMainfile{fcount}').send_keys(file)
        time.sleep(3)
        print(x)
        fcount +=1

    driver.find_element_by_id("mc_btnGuardar").send_keys(Keys.ENTER)

    print("sample test case successfully completed")  

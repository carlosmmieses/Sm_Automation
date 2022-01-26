#########################################################################
### Creador: Carlos Andres Mejias Mieses                              ###
### Fecha: 2021 12 27                                                 ###
### Proposito: Crear un script que automatice CRUD.                   ###
###                                                                   ###
###                                                                   ###
###                                                                   ###
#########################################################################

from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.tiktok.com')
###PROBLEMA: TIK TOK Tiene captcha contra bots.
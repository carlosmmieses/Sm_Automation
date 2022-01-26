#########################################################################
### Creador: Carlos Andres Mejias Mieses                              ###
### Fecha: 2021 12 27                                                 ###
### Proposito: Crear un script que automatice CRUD.                   ###
###                                                                   ###
###                                                                   ###
###                                                                   ###
#########################################################################

from os import path
from pickle import TRUE
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#Variables:
username = 'MejiMotorsPR'
password = 'Cm841164818!%'

# print('test started')
# driver = webdriver.Chrome()
# driver.get('https://www.instagram.com/create/select/')
# time.sleep(3)

# driver.find_element(By.NAME, 'username').send_keys(username)
# driver.find_element(By.NAME, 'password').send_keys(password)
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF').send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, 'aOOlW.HoLwm').send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, 'wpO6b.ZQScA').send_keys(Keys.ENTER)
# time.sleep(3)
# print('test successful!')


# time.sleep(5)
#driver.find_element_by_class_name('_2hvTZ pexuQ zyHYP').send_keys(username)
#driver.find_element_by_name('username').send_keys(username)

# from instabot import Bot
# import os 
# import glob
# from PIL import Image
# #cookie_del = glob.glob("config/*cookie.json")
# #os.remove(cookie_del[0])
# path = r'C:\Users\cas\Documents\MejiMotorsPR\imagenes\venta00.jpg'
# image = Image.open(path)
# print(image.size)
# new_img = image.resize((1080, 1080)) 
# new_img.save('venta0.jpg')
# path = r'C:\Users\cas\Downloads\car.jpeg'
# bot = Bot()
# bot.login(username='MejiMotorsPr', password='Cm841164818!%', is_threaded=TRUE)
# bot.upload_photo(path, caption='Cliente satisfecho!')

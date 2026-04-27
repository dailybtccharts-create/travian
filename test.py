import numpy as np
import random
from selenium import webdriver 
from selenium.webdriver.common.by import By

from threading import Thread

import time


driver = webdriver.Chrome()


def normal (mean,var,min, max):
    a = np.random.normal(mean,var)
    time = np.clip(a,min,max)
    return time

driver.get('https://rof.x2.europe.travian.com/dorf1.php')

time.sleep(normal(4,0.8,1.9,8))

mail = driver.find_element(By.NAME,"name")
password = driver.find_element(By.NAME,"password")

mail.send_keys("enguerrendmoimabiere@gmail.com")
password.send_keys("azertyuiop")

time.sleep(normal(2.6,0.2,1.4,6))
summit = driver.find_element(By.CLASS_NAME,"textButtonV2.buttonFramed.rectangle.withText.withLoadingIndicator.green")
summit.click()

time.sleep(normal(2,0.5,1,4))

time.sleep(5)


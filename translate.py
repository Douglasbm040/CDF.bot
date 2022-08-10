from lib2to3.pgen2 import driver
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("https://translate.google.com.br/?hl=pt-BR")
time.sleep(20)
elem = driver.find_element(By.XPATH,"//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
elem.clear()
time.sleep(10)
elem.send_keys("i see you ")
time.sleep(10)                             
batatinha = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]/span/span") 
batatinha= batatinha.get_attribute("innerHTML")
soup = BeautifulSoup(batatinha, 'html.parser')
text = soup.get_text()
print(text)

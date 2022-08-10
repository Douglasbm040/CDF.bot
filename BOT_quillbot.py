from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
def bot ():
    driver = webdriver.Firefox()
    driver.get("https://quillbot.com/")
    time.sleep(10)
    print("entrar no campo")
    elem = driver.find_element(By.XPATH, "//*[@id=\"inputText\"]") 
    print("limpar o campo")
    elem.clear()
    time.sleep(10)
    print("escrever")
    elem.send_keys("eu nao sou maluco ")
    print("clicado")
    time.sleep(20)
    elem.send_keys(Keys.CONTROL + Keys.ENTER)
    print("webscraping")
    time.sleep(40)
    html = driver.find_element(By.XPATH,"//*[@id=\"outputText\"]")
    html= html.get_attribute("innerHTML")
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text 
    
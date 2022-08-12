from mimetypes import init
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from utilquillbot import UtilBot
            
class Bot():
    def __init__(self):
        self.elem = ""
        self.driver = webdriver.Firefox()
        
    def OpenPage(self,link):
        self.driver.get(link)
         

    def searchinput(self,input):
        time.sleep(40)
        print("entrar no campo")
        self.elem = self.driver.find_element(By.XPATH,input)

    def writerinput(self,text):
        print("limpar o campo")
        self.elem.clear()
        time.sleep(40)
        print("escrever")
        self.elem.send_keys(text)
        

    def SendText(self,xpathButton):
        time.sleep(40)
        button = self.driver.find_element(By.XPATH,xpathButton)
        button.click()
        print("clicado")
        

    def Scraping(self,output):
        time.sleep(40)
        print("iniciar webscraping")
        html =  self.driver.find_element(By.XPATH,output)
        html= html.get_attribute("innerHTML")
        soup = BeautifulSoup(html, 'html.parser')
        self.text = soup.get_text()
        print(self.text)
        return self.text
    
        


Bot_quillbot = Bot()
Bot_quillbot.OpenPage(UtilBot.mapquillbot["link"])
Bot_quillbot.searchinput(UtilBot.mapquillbot["xpathinput"])
Bot_quillbot.writerinput("eu sou louco")
Bot_quillbot.SendText(UtilBot.mapquillbot["xpathbutton"])
Bot_quillbot.Scraping(UtilBot.mapquillbot["xpathoutput"])


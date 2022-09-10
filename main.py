
from bot import Bot
from utilquillbot import UtilBot

def initbotquillbot(text):
    Bot_quillbot = Bot()
    Bot_quillbot.OpenPage(UtilBot.mapquillbot["link"])
    Bot_quillbot.searchinput(UtilBot.mapquillbot["xpathinput"])
    Bot_quillbot.writerinput(text)
    Bot_quillbot.SendText(UtilBot.mapquillbot["xpathbutton"])
    resulttext = Bot_quillbot.Scraping(UtilBot.mapquillbot["xpathoutput"])
    return resulttext

    
def initBotTranslate(text):
    Bot_Translate = Bot()
    Bot_Translate.OpenPage(UtilBot.maptranslatebot["link"])
    Bot_Translate.searchinput(UtilBot.maptranslatebot["xpathinput"])
    Bot_Translate.writerinput(text)
    resulttext = Bot_Translate.Scraping(UtilBot.maptranslatebot["xpathoutput"])
    return resulttext

initBotTranslate(initbotquillbot("A Física quântica, também conhecida como mecânica quântica, é uma grande área de estudo que se dedica em analisar e descrever o comportamento dos sistemas físicos de dimensões reduzidas, próximos dos tamanhos de moléculas, átomos e partículas subatômicas."))

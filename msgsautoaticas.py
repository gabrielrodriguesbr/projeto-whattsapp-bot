from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver= webdriver.Edge(executable_path="D:\\edgedriver_win32\\msedgedriver.exe")
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
time.sleep(15)

contatos=['Suzi', 'AM Angel']
mensagem= 'Opa eae blz? Um teste de automação rapidão, naquele estilo!'

def buscar_contato(contato):
    campo_pesquisa=driver.find_element_by_xpath('//div[contains(@class, "copyable-text-selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem=driver.find_elements_by_xpath('//div[contains(@class, "copyable-text-selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.expected_conditions import presence_of_element_located
import pyautogui

chrome_options = webdriver.ChromeOptions()
# 1 to allow, 2 to block
prefs = {
  "profile.default_content_setting_values.cookies": 2,
  "profile.block_third_party_cookies": True
}
chrome_options.add_experimental_option("prefs",prefs)

from datetime import datetime

today = datetime.today()
days = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

str_month = months[today.month-1] # obtemos o numero do mês e subtraímos 1 para que haja a correspondência correta com a nossa lista de meses
str_weekday = days[today.weekday()] # obtemos o numero do dia da semana, neste caso o numero 0 é segunda feira e coincide com os indexes da nossa lista
mesAtual = str_month
anoAtual = today.year



with webdriver.Chrome() as driver:
    #wait = WebDriverWait(driver, 10)
    driver.get("https://atende.cemig.com.br/Login")
    driver.maximize_window()

    time.sleep(1)
    try:
        start = pyautogui.locateCenterOnScreen('img.png')
        if start:
            pyautogui.click(start)
        else:
            print("Não foi encontrado mensagens de permissão de cookies.")

    except:
        print("Não foi encontrado mensagens de permissão de cookies.")


    print("PREENCHE USUÁRIO")
    time.sleep(3)
    campo_usuario = driver.find_element(By.XPATH, "//input[@id='acesso']")
    campo_usuario.send_keys("11036437620")
    print("PREENCHE A SENHA")
    time.sleep(2)
    campo_senha = driver.find_element(By.XPATH, "//input[@id='senha']")
    campo_senha.send_keys("Cunha@2030")
    time.sleep(8)

    try:
        captcha = pyautogui.locateCenterOnScreen('img_1.png')
        if start:
            pyautogui.click(captcha)
        else:
            print("Não foi encontrado captcha.")

    except:
        print("Não foi encontrado mensagens de captcha.")


    time.sleep(4)
    print("Clicar em entrar")
    botao_entrar = driver.find_element(By.XPATH, "//button[contains(text(),'Entrar')]")
    botao_entrar.click()

    try:
        contas = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Contas')]")))

        print("Realizou login com Sucesso.")

        print("Clicar em Contas")
        time.sleep(10)
        try:
            start = pyautogui.locateCenterOnScreen('img_3.png')
            if start:
                pyautogui.click(start)
            else:
                print("Não foi encontrado mensagens de permissão de cookies.")

        except:
            print("Não foi encontrado mensagens de permissão de cookies.")
            driver.quit()

        time.sleep(1)
        contas.click();

        selecionar_mes_ano_Atual = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{mesAtual} {anoAtual}')]")))
        time.sleep(2)
        print(f"Localizou o mês/ano: {mesAtual} {anoAtual}")
        print("Clicar no mês e ano atual.")
        selecionar_mes_ano_Atual = driver.find_element(By.XPATH, f"//div[contains(text(),'{mesAtual} {anoAtual}')]")
        selecionar_mes_ano_Atual.click()

        baixar_PDF = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Baixar PDF')]")))
        time.sleep(2)
        print("Clicar em Baixar PDF")
        # selecionar_mes_ano_Atual = driver.find_element(By.XPATH, f"//div[contains(text(),'{mesAtual} {anoAtual}')]")
        baixar_PDF.click()
        time.sleep(2)
        driver.quit()

    except:
        print("Provável captcha avançado detectado. Não foi possível achar condições gratuitas para a quebra.")
        driver.quit()

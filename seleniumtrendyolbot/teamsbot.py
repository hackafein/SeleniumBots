import os, time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import timeit
import re
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
class Teamsbot:
    def __init__(self):
        self.path = f'{os.getcwd()}/chromedriver'
        chrome_options = Options()
        mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
        #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(self.path, chrome_options=chrome_options)
        self.user="f.ceran@live.com"
        self.password="1998-147"

    def login(self):
        try:
            self.driver.get("https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=ba4b3a9d-3c4b-45b8-93a0-3dbbf94c0a18&&client-request-id=c27cdf9d-a3a4-409a-bbad-c1566a75aae7&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=7ec26c1c-c8be-4a2e-8fc3-cbd9f5c59779&domain_hint=")
            
            
            user= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')))#username
            user.send_keys(self.user)

            button= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input')))#loginbutton
            button.click()

            passw= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input')))#passw
            passw.send_keys(self.password)
            
            button= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input')))#loginbutton2
            button.click()
    
            #self.driver.get("https://teams.microsoft.com/_?culture=tr-tr&country=TR&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn&tenantId=b25c434e-6acf-492a-99fe-b7144e777cba#/conversations/19:032e0f667360406c985625e344b84769@thread.v2?ctx=chat")
            button= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[3]/button')))#kurulus sec
            button.click()
            button= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div[1]/ul/li[1]')))#autodidactic
            button.click()       
            button= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[4]/button')))#autodidactic
            button.click()       
            time.sleep(5)
            self.driver.get("https://teams.microsoft.com/_?culture=tr-tr&country=TR&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn&tenantId=b25c434e-6acf-492a-99fe-b7144e777cba#/conversations/19:a989da8113ef47cfbd17f1eb8b6d1e94@thread.v2?ctx=chat")
            return True
        except:
            return False
    def sendmessage(self,message):
        
        mssgbox= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/div/messages-header/div[2]/div/message-pane/div/div[3]/new-message/div/div[2]/form/div[4]/div[1]/div[2]/div/div/div[2]/div/div/div/div')))
        mssgbox.send_keys(Keys.COMMAND+"B")
        mssgbox.send_keys(message)
        
        mssgbox.send_keys(Keys.ENTER)                   
        time.sleep(5)

    def messagecontrol(self):
        try:
            soup = BeautifulSoup(self.driver.page_source)

            mydivs = soup.findAll("div", {"class": "message-body-content clearfix html text-to-html"})
            lastmessage=str(mydivs[-1])
            header=lastmessage.find("!")
            if header!=-1:
                endline=lastmessage.find("<",header)
                lastmessage=lastmessage[header:endline]

            print(lastmessage)
            if "!BOTKONTROL" in lastmessage  :
                message=" Yapay Zeka Kontrol Botu = Bot Durumu Aktif "
                self.sendmessage(message)
            elif "!HELP" in lastmessage :
                message="""
                Bot komutları:
                [! BOTKONTROL     = Bot aktifmi ?]
                [! EGITIMDURUMU   = Eğitim durumunu bildirir]
                [! KAPAT          = Bot Programını Kapatır]
                [! AGKONTROL      = Bilgisayarların Ağ durumunu özetler]
                [! EGITIMKONTROLU (SIKLIK) = Girilen dakika cinsinden eğitim kontrolü yapar]
                """
                self.sendmessage(message)
            elif "!KAPAT" in lastmessage :
                message=" Yapay Zeka Kontrol Botu = Bot Programı Kapatılıyor.... "
                self.sendmessage(message)
            elif "!AGKONTROL" in lastmessage :
                message=" Ağ durumu kontrol ediliyor "
                self.sendmessage(message)
            elif "!EGITIMDURUMU" in lastmessage :
                message=" Aktif Eğitim Yok  "
                self.sendmessage(message)
            elif "!EGITIMKONTROLU" in lastmessage:
                param=lastmessage.split(" ")
                self.sendmessage("Eğitim Kontrol sıklığı "+str(param[1])+" dakikaya ayarlandı")
            time.sleep(1)
        except:
            print("Bir hata oluştu")
        self.resetpage()

    def resetpage(self):
        self.driver.get("https://teams.microsoft.com/_?culture=tr-tr&country=TR&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn&tenantId=b25c434e-6acf-492a-99fe-b7144e777cba#/conversations/19:a989da8113ef47cfbd17f1eb8b6d1e94@thread.v2?ctx=chat")
        time.sleep(4)
    def menu(self):
        cond=self.login()
        if cond== True:
            while 1:
                time.sleep(15)
                self.messagecontrol()
if __name__ == '__main__':
    Teamsbot().menu()  

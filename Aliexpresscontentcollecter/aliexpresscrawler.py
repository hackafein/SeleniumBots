import os, time, random
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import timeit
import re

class Aliexcrawler:
    def __init__(self):
        self.path = f'{os.getcwd()}/chromedriver'
        chrome_options = Options()
        mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(self.path, chrome_options=chrome_options)
        self.sayfalar=''
        self.seed=''
        self.urunliste=[]
        self.baslikseed=''
        self.basliklar=''
        self.urunbaslikliste=[]
    def getproducts(self,link,sayfa):
        self.driver.get(str(link))
        durum=0
        while durum<sayfa+1:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.1)
            durum+=1
        if sayfa==0:
            while 1:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.1)
        urun=1

        
        self.a=(self.driver.find_elements_by_class_name("product-dot"))
        for i in self.a:
            self.seed=i.get_attribute('href')
            self.urunliste.append(self.seed)
            
        self.basliklar=(self.driver.find_elements_by_class_name("product-title"))
        for j in self.a:
            self.baslikseed=j.find_element_by_css_selector('span').get_attribute('textContent')
            self.urunbaslikliste.append(self.baslikseed)
        
        self.crawlerinside()




    def crawlerinside(self):
        b=0
        time.sleep(0.1)
        for i in self.urunliste:
            
            b=b+1
            self.gotoproduct(i,b)





        

    def gotoproduct(self,seed,urunno):
        self.driver.get(seed)
        time.sleep(1)
        try:
            button = self.driver.find_element_by_xpath('//*[@id="smartbanner-main"]/div[2]/div/div/img')
            button.click()
        except:
            time.sleep(0.001)
       
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,1000)") 
        time.sleep(1.3)
        button2 = self.driver.find_element_by_xpath('/html/body/div[1]/div[6]')
        button2.click()
        
        time.sleep(1)
        a=0
        b=3
        c=42

        yorumlar=[]
        
        yorumlar.append("Ürün İsmi ="+str(self.urunbaslikliste[b-1])+"\n \n Ürün Numarası ="+str(urunno)+"\n \n")
        start = timeit.default_timer()
        time.sleep(1000)
        while True:
            try:
                try:
                    time.sleep(0.1)
                    if ''!=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(b)+']/p').get_attribute('textContent'):
                        button1 = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(b)+']/div[4]/span[2]')
                        button1.click()
                    
                    yorum = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(b)+']/p').get_attribute('textContent')

                    tarih= self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(b)+']/div[1]/span[3]').get_attribute('textContent')
                    if yorum != '':
                        yorumlar.append("Tarih="+tarih+" /--/ "+yorum)
                    

                    a=a+1
                    b=b+2


                    
                except:
                    
                    print("Sayfa bitti")
                    print(c)
                    
                    button2 = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(c)+']')
                    button2.click()
           
                    c+=40
                    self.driver.execute_script("window.scrollTo(0,3000)") 
                    time.sleep(1)
                    
            
            except:
                print("Tüm yorumlar çekildi")
                break
        stop = timeit.default_timer()
        if stop-start<5:
            print( "Olmaması gereken bir durum oluştu sayfa tekrar taranıyor....")    
            self.gotoproduct(seed,urunno)
           
        file1 = open(str(urunno)+".txt","a") 
        for i in yorumlar:
            file1.writelines('\n'+i)
        file1.close() 


    def menu(self):
        while 1:
                
            print("""
    ▄▀█ █░░ █   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀   █▀▀ █▀█ ▄▀█ █░█░█ █░░ █▀▀ █▀█
    █▀█ █▄▄ █   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█   █▄▄ █▀▄ █▀█ ▀▄▀▄▀ █▄▄ ██▄ █▀▄ 

        Lütfen seçim yapınız=
            1-) Ürünleri tara ve yazdır
            2-) Performans ayarları
            3-) İletişim
            4-) Çıkış
            
            """)
            secim=int(input(' '))
            
            if secim==1:
                link=input("Lütfen kategori linki giriniz= ")
                sayfa=int(input("Kaç sayfa tarayalım (0=tümünütara,1,2,3,4,5..)= "))
                self.getproducts(link,sayfa)
            elif secim==2:
                print('Performans ayarları')
                perf=input('Sisteminizin ve internetinizin yavaşlığını 1 den 5 e kadar derecelendirin (1 en hızlı 5 en yavaş)')
                if 0<=perf<6:
                    print('Program sisteminize göre ayarlanıyor')
                else:
                    print('Eksik yada yanlış tuşladınız.')
            elif secim==3:
                print('İletişim adresim= 05511529179 / f.ceran@live.com')
            elif secim==4:
                print("Uygulamadan çıkış yapıluyor")
                break
if __name__ == '__main__':
    Aliexcrawler().menu()  
    #Aliexcrawler().gotoproduct()  


    #   https://tr.aliexpress.com/category/34/automobiles-motorcycles.html

# coding: utf-8


import time
import sys, io
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *
from googlelogin import LOGIN, PASSWORD
import os




class PlayStoreHacker:
    def __init__(self):
        self.keylist=[]
        file1 = open('reedemcodes.txt', 'r') 
        Lines = file1.readlines() 
        count = 0
        for line in Lines: 
            self.keylist.append(line.strip())
        print(self.keylist)
        self.googlemail=LOGIN
        self.googlepass=PASSWORD
        self.setup()
        return
    def setup(self):
        no_of_reviews = 1000

        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        self.driver = webdriver.Chrome("/Users/furkanceran/Desktop/chromedriver")

        wait = WebDriverWait( self.driver, 10 )
        self.driver.get("https://stackoverflow.com/")
        time.sleep(2)
        self.page = self.driver.page_source
        
        self.loginbutton=self.driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]')
        time.sleep(1)
        self.loginbutton.click()
        self.stacklog=self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/button[1]')
        self.stacklog.click()
        time.sleep(2)
        self.emailarea=self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        
        self.emailarea.send_keys(self.googlemail)
        self.nextbutton=self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
        time.sleep(0.1)
        self.nextbutton.click()
        time.sleep(2)
        self.passarea=self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.googlepass)

        self.nextbutton=self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
        time.sleep(0.1)
        self.nextbutton.click() 
        time.sleep(2)
        self.driver.get("https://play.google.com/redeem")
        time.sleep(2)
        self.keyenterer()
        return
        
    def keyenterer(self):
        a=4
        self.resultlist=[]
        outF = open("resultlist.txt", "w")
        for i in self.keylist:
            self.reedemcode=self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div['+str(a)+']/div/div[2]/span/div/div[1]/div[1]/div/div[1]/input')
            self.reedemcode.clear()
            self.reedemcode.send_keys(str(i))
            self.reedemcodebutton=self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div['+str(a)+']/div/div[2]/div[3]/div/button[2]')

            time.sleep(0.3)
            self.reedemcodebutton.click()
            time.sleep(2)
            self.result=self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[6]/div/div[2]/span/div/div[2]').get_attribute('textContent')
            
            outF.write(str(i+":  "+self.result))
            outF.write("\n")
            if a==4:
                a+=2

        outF.close()
        self.driver.quit()
        return
PlayStoreHacker().__init__()





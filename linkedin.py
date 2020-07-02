from selenium import webdriver
from time import sleep
from credentials import email,password

class linkedinBot():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def addfriend(self):

        cnx_btn_class = self.driver.find_element_by_xpath('//*[@class="full-width artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view"]')
        cnx_btn_class.click()
        sleep(2)
        dismiss_btn = self.driver.find_element_by_xpath('//*[@class="artdeco-card__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]')
        dismiss_btn.click()
        sleep(2)
    def add10friend(self):
        for x in range(10):
            self.addfriend()

    def login(self):
        self.driver.get('https://linkedin.com')
        sleep(2)
        ln_btn = self.driver.find_element_by_xpath('/html/body/nav/a[3]')
        ln_btn.click()

        sleep(2)
        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(email)
        sleep(2)
        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        pw_in.send_keys(password)

        signin_btn = self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
        signin_btn.click()
        
        sleep(2)

        cnx_btn = self.driver.find_element_by_xpath('//*[@id="mynetwork-tab-icon"]')
        cnx_btn.click()

        sleep(8)
        

        
self = linkedinBot()
self.login()
self.add10friend()


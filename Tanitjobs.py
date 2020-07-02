from selenium import webdriver
from time import sleep
from TanitjobsCred import email,password
from selenium.webdriver.common.keys import Keys
from motivation import motivationText

formUrl=[]

class TanitjobsBot():
    
    
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

    
    def login(self):
        self.driver.get('https://www.tanitjobs.com/')

        sleep(1)
        ln_btn = self.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/ul/li[1]/a')
        ln_btn.click()

        sleep(1)
        email_in = self.driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/input')
        email_in.send_keys(email)
        sleep(1)
        pw_in = self.driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/input')
        pw_in.send_keys(password)

        signin_btn = self.driver.find_element_by_xpath('//*[@id="bouton-con"]')
        signin_btn.click()
        
        sleep(1)

        cnx_btn = self.driver.find_element_by_xpath('//*[@id="navbar-collapse"]/div[2]/ul/li[1]/a/span')
        cnx_btn.click()

        sleep(1)
    def search(self):
        search_bar = self.driver.find_element_by_xpath('//*[@id="keywords"]')
        search_bar.send_keys("Developpeur")
        sleep(1)

        srch_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/form/div[3]/button')
        srch_btn.click()
    
    def ListPosts(self):
        
        def getFormUrl(self):
            link = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div/div[3]/div[1]/div[1]/div[3]/div/div[1]/button')
            link = link.get_attribute("data-href")
            cleanLink = link.replace('\t\t\t\t\t\t', '')
            cleanLink = cleanLink.replace('\n', '')
            formUrl.append(cleanLink)    

        addr = self.driver.find_elements_by_css_selector('div.media-body > div.media-heading.listing-item__title > a')
        urls = [v.get_attribute("href") for v in addr]
        window_handle=[]
        
        for x in range(1, len(urls) + 1):
        #for x in range(1,2):
            self.driver.get(urls[x - 1])
            sleep(1)
            getFormUrl(self)
           #self.driver.execute_script("window.open();")
           #self.driver.switch_to.window(self.driver.window_handles[x])
           
           #self.driver.execute_script("window.close();")
           #sleep(1)
            #count=post_list.index(i)
            #print(post_list[count])            
            
            #sleep(3)
            #self.driver.back()
    #def turnPage(self):
    

    def fillForm(self):
        for i in formUrl:
            self.driver.get(i)
            sleep(1)
            self.driver.find_element_by_name('file_tmp').send_keys("C:/Users/Wael/Documents/bot/cv.pdf")
            self.driver.find_element_by_xpath('//*[@id="apply-form"]/div[5]/textarea').send_keys(motivationText)
            self.driver.find_element_by_xpath('//*[@id="apply-form"]/div[6]/input').click()
    def hailMary(self):
        self.driver.get('https://www.tanitjobs.com/apply-now/?listing_id=662030&ajaxRelocate=1')
        for i in range(0,100):
            url_nbr= 662030 + i            
            url= 'https://www.tanitjobs.com/apply-now/?listing_id='+ str(url_nbr) +'&ajaxRelocate=1'
            self.driver.get(url)
            sleep(1)
    

        
self = TanitjobsBot()
self.login()
self.search()
self.ListPosts()
#self.hailMary()


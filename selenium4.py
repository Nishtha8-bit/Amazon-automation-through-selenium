from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchWindowException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import smtplib
import os
from email.mime.image import MIMEImage



class Amazon:
    #base_url='http://www.amazon.in'
    search_term='shoes'

    def setup(self):
        self.driver=webdriver.Chrome('C://Users//smart//Desktop//chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://www.amazon.in')
#use to login process
    def login(self):
           
        signinelement=self.driver.find_element_by_xpath('//*[@id="ap_email"]')
        signinelement.send_keys('email_id') #amazon email id
        self.driver.implicitly_wait(10)

        cont=self.driver.find_element_by_xpath('//*[@id="continue"]')
        cont.click()
        self.driver.implicitly_wait(10)

        passwordelement=self.driver.find_element_by_xpath('//*[@id="ap_password"]')
        passwordelement.send_keys('password')#password of amazon
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    
            
        self.driver.implicitly_wait(10)
        number=self.driver.find_element_by_xpath('//*[@id="cvf-page-content"]/div/div/div/form/div[1]/div/div[2]/div/div[2]/input')
        number.send_keys('contact number') 
        cont1=self.driver.find_element_by_xpath('//*[@id="a-autoid-0"]/span/input')
        cont1.click()
        self.driver.implicitly_wait(10)

    def SendMail(self,ImgFileName):
        img_data = open(ImgFileName, 'rb').read()
        msg = MIMEMultipart()
        msg['Subject'] = 'screenshot'
        msg['From'] = 'fromadd'
        msg['To'] = 'toadd'

        text = MIMEText("test")
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)

        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('From', 'password')
        s.sendmail('From','To', msg.as_string())
        s.quit()
    

    def search(self):
        flag=1
        for i in range(3):
            if(flag==1 ):
                searchTextBox=self.driver.find_element_by_id('twotabsearchtextbox')
                searchTextBox.clear()
                try:
                    
                    searchTextBox.send_keys(self.search_term)
                    searchTextBox.send_keys(Keys.RETURN)
                    self.driver.implicitly_wait(10)
                    flag=0
                    
                except NoSuchElementException :
                    print('element not found')     
                #counter=0
                try:
                    self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/div/div/div[2]/div/span/a/div/img').click()
                except NoSuchElementException :
                    flag=1
                    print("not found")
                    
        if flag==1:
                
                self.driver.save_screenshot("screenshot.png")
                self.SendMail("screenshot.png")
                #counter+=1
        #print(counter)
            
    def add_to_cart(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_id('add-to-cart-button').click()
        self.driver.find_element_by_id('hlb-ptc-btn-native').click() #used to click on proceed to buy
   
    
    

if __name__ == "__main__":
    amazon=Amazon()
    amazon.setup()
    
    amazon.search()
    #amazon.send_message()
    amazon.add_to_cart()
    amazon.login()


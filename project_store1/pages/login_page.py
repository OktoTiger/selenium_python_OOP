from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("C..\\project_store1\\")
from base.base_class import Base 
from utilities.logger import Logger

class Login_page (Base):
    
    link = "https://shop.candy.ru" 
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        
    locator_auth_button = "//div[@class='pre-header__cell pre-header__cell-3']//a[2]"
    locator_login =  "//input[@id='email']"
    locator_password = "//input[@id='password']"
    locator_button_enter = "//button[@name='commit']"
    
    # Getters
    """Получение локаторов для авторизации"""
    def get_auth_button(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_auth_button)))  
       
    def get_input_login(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_login)))     
    
    def get_input_password(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_password)))  
    
    def get_button_enter(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_button_enter)))            
    
    # Actions
    
    def click_auth_button(self):
        self.get_auth_button().click()
        print ("Click auth_button")   
        
    def input_login(self, email):
        self.get_input_login().send_keys(email)
        print ("Input email")
        
    def input_password(self, password):
        self.get_input_password().send_keys(password)
        print ("Input password")       

    def click_button_enter(self):
        self.get_button_enter().click()
        print ("Click button enter")   
        
        
        # Methods
    def authorization(self):
        Logger.add_start_step(method="authorization")
        self.browser.get(self.link)
        self.click_auth_button()
        self.input_login("seleniumautotest99@yandex.ru")
        self.input_password("Qq12345")
        self.click_button_enter()
        Logger.add_end_step(url=self.browser.current_url, method="authorization")






# 
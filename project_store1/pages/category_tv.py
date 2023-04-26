from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver import ActionChains
sys.path.append("..\\project_store1\\")
from base.base_class import Base 
import time

class Category_tv (Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        
    # Locarors
    locator_checkbox_diagonal = "//input[@value='137165204']/..//span[1]"
    locator_link_smarttv = "//span[@data-tab-anchor='35714955']"
    locator_checkbox_smarttv = "//input[@value='134981538']/../span[1]"
    locator_choose_tv = "/html/body/div[2]/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div/form/div[1]/div/a"
    
    # Getters   
    """Получение локаторов в панели фильтров"""
    def get_checkbox_diagonal(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_checkbox_diagonal)))  

    def get_link_smarttv(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_link_smarttv)))  

    def get_checkbox_smarttv(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_checkbox_smarttv)))  

    def get_choose_tv(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_choose_tv)))
    
    # Actions
        
    def click_checkbox_diagonal(self):
        self.get_checkbox_diagonal().click()
        print ("Click checkbox diagonal") 
    
    def click_link_smarttv(self):
        self.get_link_smarttv().click()
        print ("Click link_smarttv")    
    
    def click_checkbox_smarttv(self):
        self.get_checkbox_smarttv().click()
        print ("Click checkbox smarttv")  
    
    def click_choose_tv(self):
        self.get_choose_tv().click()
        print ("Click choose tv")  
    
    # Methods
    
    def choose_price(self):
        self.get_current_url()
        self.click_checkbox_diagonal()
        self.click_link_smarttv()
        self.click_checkbox_smarttv()
        self.click_choose_tv()

        












# 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
sys.path.append("..\\project_store1\\")
from base.base_class import Base 

class Catalog_page (Base):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locarors
    locator_tv = "//img[@title='Телевизоры']"
    
    # Getters
    """Получение локатора названия телевизора"""
    def get_tv(self):
        return WebDriverWait(self.browser,30).until(EC.element_to_be_clickable((By.XPATH, self.locator_tv)))  
    
    # Actions
    
    def click_tv(self):
        self.get_tv().click()
        print ("Click button to products")
        
    def category_tv(self):
        self.get_current_url()
        self.click_tv()














# 